from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv
import os

# Schemas
from schemas.games_schema import GameSchema
from schemas.level_schema import LevelSchema
from schemas.character_schema import CharacterSchema
from schemas.enemy_schema import EnemySchema

load_dotenv()


def create_app():
    app = Flask(__name__)

    # =========================
    # BANCO DE DADOS
    # =========================
    from database import init_db
    init_db(app)

    # =========================
    # AMBIENTE
    # =========================
    db_url = os.getenv('DATABASE_URL', '')
    env_label = 'Supabase' if 'supabase' in db_url else 'Local (Docker)'

    # =========================
    # SWAGGER CONFIG
    # =========================
    app.config['SWAGGER'] = {
        'title': 'Game API 🎮',
        'uiversion': 3,
        'description': f'API de jogos ({env_label})',
        'specs_route': '/apidocs/'
    }

    swagger_template = {
        "tags": [
            {"name": "Health"},
            {"name": "Games"},
            {"name": "Levels"},
            {"name": "Characters"},
            {"name": "Enemies"}
        ],
        "definitions": {
            "Game": GameSchema.model_json_schema(),
            "Level": LevelSchema.model_json_schema(),
            "Character": CharacterSchema.model_json_schema(),
            "Enemy": EnemySchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {
                    "error": {"type": "string"}
                }
            }
        }
    }

    Swagger(app, template=swagger_template)

    # =========================
    # BLUEPRINTS (ROTAS)
    # =========================
    from routes.games import games_bp
    from routes.level import levels_bp
    from routes.character import characters_bp
    from routes.enemies import enemies_bp
    from routes.health import health_bp

    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(games_bp, url_prefix='/api/games')
    app.register_blueprint(levels_bp, url_prefix='/api/levels')
    app.register_blueprint(characters_bp, url_prefix='/api/characters')
    app.register_blueprint(enemies_bp, url_prefix='/api/enemies')

    return app


# =========================
# RUN (CORRIGIDO PARA DOCKER)
# =========================
if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0", 
        port=5000,
        debug=True
    )