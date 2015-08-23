from config import db


def create_db():
    db.create_all()


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    position = db.Column(db.String(10), unique=False)
    team = db.Column(db.Integer, unique=False)
    points = db.Column(db.Float, unique=False)
    available = db.Column(db.Boolean, unique=False)
    bye_week = db.Column(db.Integer, unique=False)
    roster_spot = db.relationship("RosterSpot", uselist=False, backref="player")
    draft_pick = db.relationship("DraftPick",  uselist=False, backref="player")


    def __init__(self, name, position, team, points, bye_week):
        self.name = name
        self.position = position
        self.team = team
        self.points = points
        self.bye_week = bye_week



class RosterSpot(db.Model):
    __tablename__ = "roster_spots"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.ForeignKey("teams.id"))
    player_id = db.Column(db.ForeignKey("players.id"))
    roster_position = db.Column(db.String(10), unique=False)


    def __init__(self, team_id, roster_position):
        self.team_id = team_id
        self.roster_position = roster_position



class DraftPick(db.Model):
    __tablename__ = "draft_picks"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.ForeignKey("teams.id"))
    player_id = db.Column(db.ForeignKey("players.id"))
    round_number = db.Column(db.Integer, unique=False)
    

    def __init__(self, team_id, round_number):
        self.team_id = team_id
        self.round_number = round_number

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(25), unique=True)
    owner_name = db.Column(db.String(25), unique=True)
    picks = db.relationship("DraftPick", backref="team")
    roster = db.relationship("RosterSpot", backref="team")

    def __init__(self, team_name, owner_name):
        self.team_name = team_name
        self.owner_name = owner_name

