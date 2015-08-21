from flask import Flask, render_template, request, redirect, url_for, session
from flask.ext.login import LoginManager
from forms import DraftPlayerForm
from config import app, db
from models import Player, RosterSpot, DraftPick

@app.route("/", methods=["GET", "POST"])
def draft():
  print('drafting')
  draft_player_form = DraftPlayerForm(request.form)
  error = None
  
  teams = db.session.query(RosterSpot.roster_position, Player.name).filter(RosterSpot.player_id == Player.id).filter(RosterSpot.team_id == 0)

  players = Player.query.filter_by(available=True).order_by(Player.points.desc())

  if request.method == "POST":
    print('drafter')
    if draft_player_form.validate_on_submit():
      print("player selected")
      pick = DraftPick.query.filter_by(player_id = '').first()
      player = Player.query.filter_by(name=draft_player_form.name.data).first()
      
      player.available = False
      pick.player_id = player.id 
      roster_spots = RosterSpot.query.filter_by(team_id=pick.team_id)
      open_spots = roster_spots.filter(RosterSpot.roster_position.like('%{}%'.format(player.position))).filter(RosterSpot.player_id == '')
      if len(open_spots) >= 1:
        open_spots[0].player_id = player.id
      else:
        bench = roster_spots.filter(RosterSpot.roster_position.like('%B%').filter(RosterSpot.player_id == ''))
        if len(bench.all()) >= 1:
          bench[0].player_id = player.id
        else:
          return "Cannot draft player!"
      db.session.commit()
      

  return render_template("draft_player.html", roster=teams.all(), draft_player_form=draft_player_form, players=players.all(), error=error)




if __name__ == '__main__':
  app.run(debug=True)