from sqlalchemy.orm import Session

from reservas.model import Reserva
from reservas.flask_app import engine

def persist_requisition(reserva):
	with Session(engine) as session:
		session.merge(reserva)
		session.commit()

def fetch_requisition(code):
	with Session(engine) as session:
		return session.query(Reserva).get(code)

def delete(reserva):
	with Session(engine) as session:
		session.delete(reserva)
		session.commit()

def list_requisition():
	with Session(engine) as session:
		return session.query(Reserva).all()

