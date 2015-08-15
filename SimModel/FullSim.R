##Go through the draft team by team (NB: This is not "snake"-style, it will just go team by team)
for (team in levels(myRoster$team)) {
  ##Now go through the player dataframe line by line
  for (i in 1:nrow(offense2)) {
    ##If the best player is taken, keep going until you find one that's available
    if (offense2$available[i] == "unavailable") {
      next()
    }
    ##Find all of the roster spots for the current team that match the best player's position
    else  {
      posIndex <- grep(offense2$position[i], myRoster$position[myRoster$team == team])
      ##Find out whether those spots are open, and add the player if so
      for (j in posIndex) {
        if (is.na(myRoster$name[j]) == TRUE) {
          myRoster$name[j] <- offense2$name[i]
          offense2$available[i] <- "unavailable"
        }
        else {
          break
        }  
      }
    }
    break
  }
  next()
}