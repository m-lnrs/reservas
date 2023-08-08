from functools import wraps

from flask import session, render_template

def auth(function):

	@wraps(function)
	def wrapper(*args, **kargs):
		if "user" not in session or not session["user"]:
			return render_template('401')

		return function(*args, **kargs)

	return wrapper