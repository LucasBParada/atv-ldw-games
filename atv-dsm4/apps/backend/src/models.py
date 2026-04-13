from database import db


# =========================
# GAME
# =========================
class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    # Relacionamento: um game tem vários levels
    levels = db.relationship(
        'Level',
        backref='game',
        cascade='all, delete-orphan',
        lazy=True
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }


# =========================
# LEVEL
# =========================
class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer)

    # Relacionamento: um level pode ter vários inimigos
    enemies = db.relationship(
        'Enemy',
        backref='level',
        cascade='all, delete-orphan',
        lazy=True
    )

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'title': self.title,
            'order': self.order,
        }


# =========================
# CHARACTER
# =========================
class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    level = db.Column(db.Integer)
    power = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'level': self.level,
            'power': self.power,
        }


# =========================
# ENEMY
# =========================
class Enemy(db.Model):
    __tablename__ = 'enemies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    health = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)

    # Relacionamento com Level
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'health': self.health,
            'attack': self.attack,
            'defense': self.defense,
            'level_id': self.level_id,
        }


# =========================
# USER
# =========================
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }