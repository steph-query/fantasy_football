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
    for (l in max(0,i-6):min(5,i)) {
      prob <- prob + dbinom(l,n,weightMatrix[dRound,playPos]) * dbinom(i-l,m-n,weightMatrix[(dRound + 1),playPos])
    }
    weights <- append(weights, prob)
  }
  
  ##Calculate expected loss and print the result
  loss <- sum(diff*weights)
  print(loss)
}

##Calculate the probabilities of each of the next ten players being available next round
next10 <- function(playPos,dRound) {
  prob <- c()
  for (i in 0:10) {
    prob <- append(prob, pbinom(i,10,weightMatrix[dRound,playPos]))
  }
  print(prob)
}