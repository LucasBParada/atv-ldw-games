from typing import Union, Tuple
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from database import db
from models import Enemy
from schemas.enemy_schema import EnemySchema

enemies_bp = Blueprint('enemies', __name__)

# =====================================
# GET - LISTAR TODOS INIMIGOS
# =====================================
@enemies_bp.route('/', methods=['GET'])
def get_all_enemies():
    """
    Lista todos os inimigos disponíveis
    """
    enemies = Enemy.query.all()
    result = [EnemySchema(**e.to_dict()).model_dump() for e in enemies]
    return jsonify(result)


# =====================================
# GET - INIMIGO POR ID
# =====================================
@enemies_bp.route('/<int:enemy_id>', methods=['GET'])
def get_enemy_by_id(enemy_id):
    """
    Obtém detalhes de um inimigo
    """
    enemy = Enemy.query.get(enemy_id)

    if not enemy:
        return jsonify({"error": "Inimigo não encontrado"}), 404

    result = EnemySchema(**enemy.to_dict()).model_dump()
    return jsonify(result)


# =====================================
# POST - CRIAR INIMIGO
# =====================================
@enemies_bp.route('/', methods=['POST'])
def create_enemy() -> Union[dict, Tuple[dict, int]]:
    """
    Cria um novo inimigo
    """
    try:
        data = EnemySchema(**request.json)
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

    new_enemy = Enemy(
        name=data.name,
        type=data.type,
        health=data.health,
        attack=data.attack,
        defense=data.defense
    )

    db.session.add(new_enemy)
    db.session.commit()

    result = EnemySchema(**new_enemy.to_dict()).model_dump()
    return jsonify(result), 201


# =====================================
# PUT - ATUALIZAR INIMIGO
# =====================================
@enemies_bp.route('/<int:enemy_id>', methods=['PUT'])
def update_enemy(enemy_id):
    """
    Atualiza um inimigo
    """
    enemy = Enemy.query.get(enemy_id)

    if not enemy:
        return jsonify({"error": "Inimigo não encontrado"}), 404

    data = request.json

    enemy.name = data.get("name", enemy.name)
    enemy.type = data.get("type", enemy.type)
    enemy.health = data.get("health", enemy.health)
    enemy.attack = data.get("attack", enemy.attack)
    enemy.defense = data.get("defense", enemy.defense)

    db.session.commit()

    result = EnemySchema(**enemy.to_dict()).model_dump()
    return jsonify(result)


# =====================================
# DELETE - REMOVER INIMIGO
# =====================================
@enemies_bp.route('/<int:enemy_id>', methods=['DELETE'])
def delete_enemy(enemy_id):
    """
    Remove um inimigo
    """
    enemy = Enemy.query.get(enemy_id)

    if not enemy:
        return jsonify({"error": "Inimigo não encontrado"}), 404

    db.session.delete(enemy)
    db.session.commit()

    return jsonify({"message": "Inimigo deletado com sucesso"})