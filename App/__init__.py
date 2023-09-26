""" Create Flask API. """

from flask import Flask
from .common.config import config
from App.src.Users.views import user_page
from App.src.databse.views import database_page


ACTIVE_ENDPOINTS = [('/users', user_page), ('/database', database_page)]


def page_not_found(error):
    return "<h2> Page Not Found :( </h2>", 404


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])

    """ Register BLUEPRINT """
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    """ Register Error Handler """
    app.register_error_handler(404, page_not_found)

    return app
