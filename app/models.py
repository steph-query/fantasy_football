from config import db

def create_db():
  db.create_all()

class Player(db.Model):

  __tablename__ = "players"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False)
  position = db.Column(db.string(10), unique=False)
  team = db.Column(db.Integer, unique=False)
  points = db.Column(db.Float, unique=False)
  available = db.Column(db.Boolean, unique=False)

  def __init__(self, name, position, team, points):
    self.name = name
    self.position = position
    self.team = team
    self.points = points

  def __repr__(self):
    return '<Player {0}, Position {1}'.format(self.name, self.position)


class RosterSpot(db.Model):

  __tablename__ = "roster_spots"

  id = db.Column(db.Integer, primary_key=True)
  team_id = db.Column(db.Integer, unique=False)
  player_id = db.Column(db.Integer, unique=True)
  roster_position = db.Column(db.String(10), unique=False)

  def __init__(self, team_id, roster_position):
    self.team_id = team_id
    self.roster_position = roster_position

  def __repr__(self):
    return "<Team {0}'s {1} spot filled by player #{2}".format(self.team_id, self.player_id)

class DraftPick(db.Model):

  __tablename__ = "draft_picks"

  id = db.Column(db.Integer, primary_key=True)
  team_id = db.Column(db.Integer, unique=False)
  player_id = db.Column(db.Integer, unique=True)
  round_number = db.Column(db.Integer, unique=False)

  def __init__(self, team_id, round_number):
    self.team_id = team_id
    self.round_number = round_number

  def __repr__(self):
    return "<Round #{0}: With overall pick number {1} Team #{2} selects player #{3}".format(self.round_number, self.id, self.team_id, player_id)










