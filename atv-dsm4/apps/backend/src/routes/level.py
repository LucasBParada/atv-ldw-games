from flask import Blueprint, jsonify, request
from schemas.level_schema import LevelSchema
from models import Level, db

levels_bp = Blueprint('levels', __name__)

# =========================
# GET - LISTAR TODOS LEVELS
# =========================
@levels_bp.route('/', methods=['GET'])
def get_all_levels():
    levels = Level.query.all()
    result = [LevelSchema(**l.to_dict()).model_dump() for l in levels]
    return jsonify(result)


# =========================
# GET - LEVEL POR ID
# =========================
@levels_bp.route('/<int:level_id>', methods=['GET'])
def get_level_by_id(level_id):
    level = Level.query.get(level_id)

    if not level:
        return jsonify({"error": "Nível não encontrado"}), 404

    result = LevelSchema(**level.to_dict()).model_dump()
    return jsonify(result)


# =========================
# POST - CRIAR LEVEL
# =========================
@levels_bp.route('/', methods=['POST'])
def create_level():
    data = request.json

    new_level = Level(
        title=data.get("title"),
        order=data.get("order"),
        game_id=data.get("game_id")
    )

    db.session.add(new_level)
    db.session.commit()

    result = LevelSchema(**new_level.to_dict()).model_dump()
    return jsonify(result), 201


# =========================
# PUT - ATUALIZAR LEVEL
# =========================
@levels_bp.route('/<int:level_id>', methods=['PUT'])
def update_level(level_id):
    level = Level.query.get(level_id)

    if not level:
        return jsonify({"error": "Nível não encontrado"}), 404

    data = request.json

    level.title = data.get("title", level.title)
    level.order = data.get("order", level.order)
    level.game_id = data.get("game_id", level.game_id)

    db.session.commit()

    result = LevelSchema(**level.to_dict()).model_dump()
    return jsonify(result)


# =========================
# DELETE - REMOVER LEVEL
# =========================
@levels_bp.route('/<int:level_id>', methods=['DELETE'])
def delete_level(level_id):
    level = Level.query.get(level_id)

    if not level:
        return jsonify({"error": "Nível não encontrado"}), 404

    db.session.delete(level)
    db.session.commit()

    return jsonify({"message": "Nível deletado com sucesso"})