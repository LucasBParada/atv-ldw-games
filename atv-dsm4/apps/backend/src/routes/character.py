from flask import Blueprint, jsonify, request
from schemas.character_schema import CharacterSchema
from models import Character, db

characters_bp = Blueprint('characters', __name__)

# =====================================
# GET - LISTAR TODOS PERSONAGENS
# =====================================
@characters_bp.route('/', methods=['GET'])
def get_all_characters():
    """
    Lista todos os personagens disponíveis
    """
    characters = Character.query.all()
    result = [CharacterSchema(**c.to_dict()).model_dump() for c in characters]
    return jsonify(result)


# =====================================
# GET - PERSONAGEM POR ID
# =====================================
@characters_bp.route('/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    """
    Obtém detalhes de um personagem
    """
    character = Character.query.get(character_id)

    if not character:
        return jsonify({"error": "Personagem não encontrado"}), 404

    result = CharacterSchema(**character.to_dict()).model_dump()
    return jsonify(result)


# =====================================
# POST - CRIAR PERSONAGEM
# =====================================
@characters_bp.route('/', methods=['POST'])
def create_character():
    """
    Cria um novo personagem
    """
    data = request.json

    new_character = Character(
        name=data.get("name"),
        description=data.get("description"),
        level=data.get("level"),
        power=data.get("power")
    )

    db.session.add(new_character)
    db.session.commit()

    result = CharacterSchema(**new_character.to_dict()).model_dump()
    return jsonify(result), 201


# =====================================
# PUT - ATUALIZAR PERSONAGEM
# =====================================
@characters_bp.route('/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    """
    Atualiza um personagem
    """
    character = Character.query.get(character_id)

    if not character:
        return jsonify({"error": "Personagem não encontrado"}), 404

    data = request.json

    character.name = data.get("name", character.name)
    character.description = data.get("description", character.description)
    character.level = data.get("level", character.level)
    character.power = data.get("power", character.power)

    db.session.commit()

    result = CharacterSchema(**character.to_dict()).model_dump()
    return jsonify(result)


# =====================================
# DELETE - REMOVER PERSONAGEM
# =====================================
@characters_bp.route('/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    """
    Remove um personagem
    """
    character = Character.query.get(character_id)

    if not character:
        return jsonify({"error": "Personagem não encontrado"}), 404

    db.session.delete(character)
    db.session.commit()

    return jsonify({"message": "Personagem deletado com sucesso"})