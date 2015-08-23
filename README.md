# fantasy_football

Don't forget to use your .gitignore file in the home directory of the project so we're not committing extraneous files that may mess with namespaces!


This app aims to do the following:

1. Keep a record of every pick in the draft.
2. Update team rosters as players are selected.
3. Analyze the remaining players pool to recommend a draft pick, as well as offer the probability that a player will be on the board at your next pick.


Current status 
  1. Functional record updates based on data entry
  2. Top 30 players rendered on home screen
  3. 1 roster rendered
  4. Displays current pick
  5. Updated current pick display to include "On the Clock" + Team name, owner

Next Steps

  1. Refresh page after each pick entered
    a. Have page load all data upon refresh
  2. Write JS to fill tables with relevant team data
    a. check espn's javascript/html/css for how they do it!
  3. Show count of players at each bye week on team
  4. Build queue feature
    a. list of players 
  5. Change data entry method to button click

  6. Add filters to available player pool
  7. Add flag to players we want to mark in the database
    a. Use JS to add css class to the table row if player flagged
  8. Import matplotlib for rendering distribution charts
    a. convert all R scripting to Python
    b. Use JS to render PNG files produced by matplotlib
  9. Add functionality to enter keepers before the draft and entail all appropriate effects