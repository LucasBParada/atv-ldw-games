import os
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = SQLAlchemy()

def init_db(app):

    USER = os.getenv("DB_USER", "root")
    PASSWORD = os.getenv("DB_PASSWORD", "root")
    HOST = os.getenv("DB_HOST", "db")   
    PORT = 3306
    DB_NAME = os.getenv("DB_NAME", "game_db")

    # aguarda MySQL ficar pronto
    import time
    time.sleep(10)

    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=PORT
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"✅ Banco '{DB_NAME}' verificado/criado")
    finally:
        connection.close()

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from models import Game, Level, Character, Enemy, User
        db.create_all()

        print("✅ Tabelas criadas")