import sys
import os

# Adiciona a pasta src ao path
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
))

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from database import db
from models import Game, Level, Character, Enemy, User

# =========================
# USUÁRIOS
# =========================
USERS = [
    {"id": 1, "username": "player1"},
    {"id": 2, "username": "player2"}
]

# =========================
# GAMES
# =========================
GAMES = [
    {
        "id": 1,
        "name": "Aventura Épica",
        "description": "Um RPG cheio de desafios"
    },
    {
        "id": 2,
        "name": "Dungeon Escape",
        "description": "Fuja das masmorras derrotando inimigos"
    }
]

# =========================
# LEVELS
# =========================
LEVELS = [
    {"id": 1, "game_id": 1, "title": "Fase 1 - Início", "order": 1},
    {"id": 2, "game_id": 1, "title": "Fase 2 - Floresta", "order": 2},
    {"id": 3, "game_id": 2, "title": "Fase 1 - Dungeon", "order": 1},
]

# =========================
# CHARACTERS
# =========================
CHARACTERS = [
    {
        "id": 1,
        "name": "Guerreiro",
        "description": "Forte e resistente",
        "level": 1,
        "power": 100
    },
    {
        "id": 2,
        "name": "Mago",
        "description": "Ataques mágicos poderosos",
        "level": 1,
        "power": 120
    }
]

# =========================
# ENEMIES
# =========================
ENEMIES = [
    {
        "id": 1,
        "name": "Goblin",
        "type": "Terrestre",
        "health": 80,
        "attack": 15,
        "defense": 5
    },
    {
        "id": 2,
        "name": "Dragão",
        "type": "Fogo",
        "health": 300,
        "attack": 50,
        "defense": 30
    }
]


def seed():
    """Popula o banco de dados com dados iniciais do game"""
    app = create_app()

    with app.app_context():

        # Verifica se já existem dados
        if Game.query.first():
            print("Banco já possui dados. Pulando seed.")
            return

        print("Populando banco de dados...")

        # USERS
        for u in USERS:
            db.session.add(User(**u))
        print(f"  {len(USERS)} usuários inseridos")

        # GAMES
        for g in GAMES:
            db.session.add(Game(**g))
        print(f"  {len(GAMES)} games inseridos")

        # LEVELS
        for l in LEVELS:
            db.session.add(Level(**l))
        print(f"  {len(LEVELS)} levels inseridos")

        # CHARACTERS
        for c in CHARACTERS:
            db.session.add(Character(**c))
        print(f"  {len(CHARACTERS)} personagens inseridos")

        # ENEMIES
        for e in ENEMIES:
            db.session.add(Enemy(**e))
        print(f"  {len(ENEMIES)} inimigos inseridos")

        db.session.commit()
        print("Seed concluído com sucesso!")


if __name__ == '__main__':
    seed()