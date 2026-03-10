from flask_sqlalchemy import SQLAlchemy
from app import db

db.session

#INSERTAR
db.session.add(juego)
db.session.commit()

#LISTAR
Juego.query.all()

#OBTENER POR LA ID
Juego.query.get(id)

#ACTUALIZACIÓN
db.session.commit()

#ELIMINAR 
db.session.delete(juego)
db.session.commit() 