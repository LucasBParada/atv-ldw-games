from flask import Blueprint, jsonify, request
from schemas.games_schema import GameSchema
from schemas.level_schema import LevelSchema
from models import Game, Level, db

games_bp = Blueprint('games', __name__)

# =========================
# GET - LISTAR TODOS GAMES
# =========================
@games_bp.route('/', methods=['GET'])
def get_games():
    games = Game.query.all()
    result = [GameSchema(**g.to_dict()).model_dump() for g in games]
    return jsonify(result)


# =========================
# GET - GAME POR ID
# =========================
@games_bp.route('/<int:game_id>', methods=['GET'])
def get_game_by_id(game_id):
    game = Game.query.get(game_id)
    
    if not game:
        return jsonify({"error": "Game não encontrado"}), 404

    return jsonify(GameSchema(**game.to_dict()).model_dump())


# =========================
# POST - CRIAR GAME
# =========================
@games_bp.route('/', methods=['POST'])
def create_game():
    data = request.json

    if not data or not data.get("name"):
        return jsonify({"error": "Nome é obrigatório"}), 400

    new_game = Game(
        name=data.get("name"),
        description=data.get("description")
    )

    db.session.add(new_game)
    db.session.commit()

    return jsonify(GameSchema(**new_game.to_dict()).model_dump()), 201


# =========================
# PUT - UPDATE GAME
# =========================
@games_bp.route('/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    game = Game.query.get(game_id)

    if not game:
        return jsonify({"error": "Game não encontrado"}), 404

    data = request.json

    game.name = data.get("name", game.name)
    game.description = data.get("description", game.description)

    db.session.commit()

    return jsonify(GameSchema(**game.to_dict()).model_dump())


# =========================
# DELETE - GAME
# =========================
@games_bp.route('/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get(game_id)

    if not game:
        return jsonify({"error": "Game não encontrado"}), 404

    db.session.delete(game)
    db.session.commit()

    return jsonify({"message": "Game deletado com sucesso"})


# =========================
# GET - LEVELS POR GAME
# =========================
@games_bp.route('/<int:game_id>/levels', methods=['GET'])
def get_levels_by_game(game_id):
    game = Game.query.get(game_id)
    
    if not game:
        return jsonify({"error": "Game não encontrado"}), 404
        
    levels = Level.query.filter_by(game_id=game_id).order_by(Level.order).all()

    result = [LevelSchema(**l.to_dict()).model_dump() for l in levels]
    return jsonify(result)


# =========================
# PUT - UPDATE LEVEL
# =========================
@games_bp.route('/levels/<int:level_id>', methods=['PUT'])
def update_level(level_id):
    level = Level.query.get(level_id)

    if not level:
        return jsonify({"error": "Nível não encontrado"}), 404

    data = request.json

    level.title = data.get("title", level.title)
    level.order = data.get("order", level.order)

    db.session.commit()

    return jsonify(LevelSchema(**level.to_dict()).model_dump())


# =========================
# DELETE - LEVEL
# =========================
@games_bp.route('/levels/<int:level_id>', methods=['DELETE'])
def delete_level(level_id):
    level = Level.query.get(level_id)

    if not level:
        return jsonify({"error": "Nível não encontrado"}), 404

    db.session.delete(level)
    db.session.commit()

    return jsonify({"message": "Nível deletado com sucesso"})