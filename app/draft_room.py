from flask import Flask, render_template, request, redirect, url_for, session
from flask.ext.login import LoginManager
from forms import DraftPlayerForm
from config import app, db#, api
from models import Player, RosterSpot, DraftPick, Team

# from flask_restful import Resource, API, reqparse, abort

@app.route("/", methods=["GET", "POST"])
def draft():
  print('drafting')
  draft_player_form = DraftPlayerForm(request.form)
  error = None
  

  def grab_player_name(roster_spot):
    try:
      return roster_spot.player.name
    except:
      return "Empty"

  # Use a query like this to make the app more transposable across leagues
  # team_ids = Team.query.with_entities(Team.id).all()
  team_ids = list(range(1,11))

  teams = {}
  for team_id in team_ids:
      team_roster = []
      roster = RosterSpot.query.filter_by(team_id=team_id).all()
      for roster_spot in roster:
        team_roster.append((roster_spot.roster_position, grab_player_name(roster_spot)))
      teams[team_id] = team_roster

  bye_counter = {
                  4: 0,
                  5: 0,
                  6: 0,
                  7: 0,
                  8: 0,
                  9: 0,
                  10: 0,
                  11: 0
                }                  

  players = Player.query.filter_by(available=True).order_by(Player.points.desc())
  
  pick = DraftPick.query.filter_by(player_id = '').first()
  
  if request.method == "POST":
    print('drafter')
    if draft_player_form.validate_on_submit():
      print("player selected")

      player = Player.query.filter_by(name=draft_player_form.name.data).first()
      
      player.available = False
      pick.player_id = player.id 
      roster_spots = RosterSpot.query.filter_by(team_id=pick.team_id)
      open_spots = roster_spots.filter(RosterSpot.roster_position.like('%{}%'.format(player.position))).filter(RosterSpot.player_id == '').all()
      bench = roster_spots.filter(RosterSpot.roster_position.like('%B%')).filter(RosterSpot.player_id == '')
      if len(open_spots) >= 1:
        open_spots[0].player_id = player.id
      else:
        if len(bench.all()) >= 1:
          bench[0].player_id = player.id
        else:
          return "Cannot draft player!"
      db.session.commit()
    return redirect("/")
      

  return render_template("draft_player.html", teams=teams, Player=Player, draft_player_form=draft_player_form, players=players, pick=pick, bye_counter=bye_counter, error=error)

# api.add_resource(Teams, '/<string:todo_id>')


if __name__ == '__main__':
  app.run(debug=True)




