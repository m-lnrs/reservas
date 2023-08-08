import sys
import locale
import argparse

from loguru import logger

from reservas.configuration import app
from reservas.flask_app import application
from reservas.controllers import HomeController

application.config["SECRET_KEY"] = app["secret_key"]

#set the locale for the application
try:
	locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
except:
	logger.warning("impossible to set locale")

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description='starts the flask application')
	parser.add_argument('--dev', action='store_true', help='run the server on dev mode with debuger on')
	parser.add_argument('--host', default='127.0.0.1', help='the host ip')
	args, unknown = parser.parse_known_args()

	application.config["DEBUG"] = args.dev
	application.run(host=args.host)
