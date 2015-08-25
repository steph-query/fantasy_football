##




##A matrix/data frame of weights by position and round should be created here
##Create a variable here for the # picks between this round and next

##Creating a function to calculate expected loss by waiting a round (NB: The data
##frame input CANNOT have NAs. Column names are important, but can be easily changed
##to fit our needs.)
lossCalc <- function(d.frame, playPos, dRound) {
  d.frame <- d.frame[d.frame$position == playPos,c("name","ppg")]
  
  ##Setting variables for number of picks till next pick and picks left in the round
  if (dRound %% 2 == 0) {m <- 9; n <- 4}
  else {m <- 11; n  <- 5}
  
  ##Calculate the 1st ten differences for the top player at each position
  diff <- c()
  for (i in 0:m) { #These loops should end at the number of picks between rounds
    diff <- append(diff, d.frame$ppg[1]-d.frame$ppg[(1+i)])
  }
  
  ##Calculate weights based on binomial probability
  weights <- c()
  for (i in 0:m) {
    prob <- 0
    for (l in max(0,i-5):min(5,i)) {
      prob <- prob + dbinom(l,n,weightMatrix[dRound,playPos]) * dbinom(i-l,m-n,weightMatrix[(dRound + 1),playPos])
    }
    weights <- append(weights, prob)
  }
  
  ##Calculate expected loss and print the result
  loss <- sum(diff*weights)
  loss
}

##Calculate the probabilities of each of the top players being available next round
nextRound <- function(playPos,dRound) {
  
  ##Set number of picks
  if (dRound %% 2 == 0) {m <- 9; n <- 4}
  else {m <- 11; n  <- 5}
  
  ##Run through weighting system a la lossCalc
  pickProb <- c()
  for (i in 0:m) {
    prob <- 0
    for (l in max(0,i-6):min(5,i)) {
      prob <- prob + dbinom(l,n,weightMatrix[dRound,playPos]) * dbinom(i-l,m-n,weightMatrix[(dRound + 1),playPos])
    }
    pickProb <- append(pickProb, prob)
  }
  
  ##Set probabilities to be cumulative to show the probability that player will be around next round
  for (i in 2:length(pickProb)) {
    pickProb[i] <- pickProb[i-1] + pickProb[i]
  }
  paste(round(pickProb*100,2),"%",sep="")
}