# 🎮 LDW Merge Skills API

API RESTful desenvolvida na disciplina de **Laboratório de Desenvolvimento Web (LDW)** da FATEC.

O projeto simula um backend de jogos, com entidades como **Games, Levels, Characters e Enemies**, utilizando **Flask, MySQL e Docker**.

---

## 🚀 Tecnologias

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8-blue?logo=mysql)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Swagger](https://img.shields.io/badge/Swagger-Docs-green?logo=swagger)

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura modular baseada em **Flask + Docker + MySQL**.


apps/backend/
│── src/
│ ├── app.py
│ ├── database.py
│ ├── models/
│ ├── routes/
│ ├── schemas/
│
docker-compose.yml
Dockerfile


---

## 🐳 Como rodar o projeto

### 1. Subir o ambiente com Docker

```bash
docker compose up --build
🌐 Serviços disponíveis
Serviço	URL
API	http://localhost:5000

Swagger UI	http://localhost:5000/apidocs

MySQL	localhost:3307
🧪 Endpoints da API
❤️ Health Check
GET /api/health
🎮 Games
Listar games
GET /api/games
Criar game
POST /api/games
{
  "name": "Zelda Clone",
  "description": "Jogo de aventura épico"
}
Buscar game
GET /api/games/{id}
Atualizar game
PUT /api/games/{id}
Deletar game
DELETE /api/games/{id}
🧩 Levels
Listar levels de um game
GET /api/levels/{game_id}
Criar level
POST /api/levels
{
  "game_id": 1,
  "title": "Floresta Sombria",
  "order": 1
}
Atualizar level
PUT /api/levels/{level_id}
Deletar level
DELETE /api/levels/{level_id}
👾 Characters
GET /api/characters
POST /api/characters
PUT /api/characters/{id}
DELETE /api/characters/{id}
Exemplo
{
  "name": "Link",
  "description": "Herói principal",
  "level": 10,
  "power": 200
}
👹 Enemies
GET /api/enemies
POST /api/enemies
PUT /api/enemies/{id}
DELETE /api/enemies/{id}
Exemplo
{
  "name": "Goblin",
  "type": "monster",
  "health": 50,
  "attack": 10,
  "defense": 5,
  "level_id": 1
}
🗃 Banco de Dados
MySQL 8 rodando via Docker
Banco criado automaticamente: game_db
Tabelas geradas via SQLAlchemy (db.create_all())
⚠️ Problemas comuns
API não acessa
host="0.0.0.0"
MySQL não conecta
DB_HOST=db
Reset completo
docker compose down -v
docker compose up --build
