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
  if request.method == "POST":
    print('drafter')
    if draft_player_form.validate_on_submit():
      print("player selected")
      player = Player.query.filter_by(name=draft_player_form.name.data).first()
      player.available = False
      
      db.session.commit()

      return render_template("draft_player.html", draft_player_form=draft_player_form, error=error)

    else:
      print(error)

  else:
    return render_template("draft_player.html", draft_player_form=draft_player_form, error=error)




if __name__ == '__main__':
  app.run(debug=True)