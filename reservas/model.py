from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, Text, ForeignKey

from reservas.flask_app import engine

Base = declarative_base()

class Person():
	def __init__(self, **entries):
		self.__dict__.update(entries)

	def __init__(self, codigo=None, nome=None, email=None):
		self.code = codigo
		self.name = nome
		self.email = email

class User():
	def __init__(self, **entries):
		self.__dict__.update(entries)

	def __init__(self, codigo=None, pessoa=None, tipo=None, situacao=None, grupo=None):
		self.code = codigo
		self.person = Person(**pessoa)
		self.type = tipo
		self.status = situacao
		self.group = grupo

class Reserva(Base):
	__tablename__ = "reserva"

	code = Column(Integer, primary_key=True)
	person = Person()

	def __init__(self, **entries):
		self.__dict__.update(entries)

	def __init__(self, code=None):
		self.code = code

