from flask import render_template, request, post, redirect, url_for
from forms import DraftPlayerForm
from config import app, db
from models import Player, RosterSpot, DraftPick


@app.route("/", methods=["GET", "POST"])
def draft():
  print('draft')
  draft_form = DraftPlayerForm(request.form)
  if request.method == "POST":
    print('drafter')
    if signup_form.validate_on_submit():
      print("player selected")

      player = Player.name
