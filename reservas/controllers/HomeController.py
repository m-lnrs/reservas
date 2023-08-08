import os
import csv
import json
import requests

from loguru import logger
from jinja2 import Template
from io import BytesIO, StringIO
from flask_weasyprint import HTML
from werkzeug.utils import secure_filename
from flask import render_template, flash, request, redirect, url_for, send_file, session

from reservas.model import User
from reservas.security import auth
from reservas.configuration import api
from reservas.flask_app import application, engine

TOMCAT_PORT = os.environ.get("TOMCAT_PORT", default="8080")
TOMCAT_HOST = os.environ.get("TOMCAT_HOST", default="127.0.0.1")

@application.route('/', methods = ['GET', 'POST'])
def dispatcher():
	return redirect(url_for("index"), code=307)

@application.route("/reservas/", methods = ['GET', 'POST'])
def index():
	if "user" not in session or not session["user"]:
		return render_template("index")

	return redirect(url_for("panel"), code=307)

@application.route("/reservas/login", methods = ['POST'])
def login():
	if "user" not in session or not session["user"]:
		url = "http://{0}:{1}/academico/autenticar/json".format(TOMCAT_HOST, TOMCAT_PORT)
		authentication = { "login": request.form["login"], "senha": request.form["passphrase"] }
		response = requests.post(url, authentication, auth=(api["user"], api["passphrase"]))

		if response.status_code == 404 or response.status_code == 401:
			return redirect(url_for("index"), code=307)

		json = response.json()
		session["user"] = json["usuario"]

	return redirect(url_for("panel"), code=307)

@application.route("/reservas/sair", methods = ['GET', 'POST'])
def logout():
	session.clear()
	return redirect(url_for("index"), code=307)

@application.route("/reservas/painel", methods = ['GET', 'POST'])
@auth
def panel():
	user = User(**session["user"])
	return render_template("panel", user=user)

@application.errorhandler(500)
def error_500(e = None):
	return render_template('500'), 500

@application.errorhandler(404)
def error_404(e = None):
	return render_template('404'), 404
