from flask import Blueprint, jsonify
from App.drivers.sqlalchemy_config import create_models
from App.common.decorators import exception_manager
from http import HTTPStatus


database_page = Blueprint('database', __name__)


@database_page.route('/create_all')
@exception_manager
def drop_all_database():
    create = create_models()
    return jsonify('Create Database Done! '), HTTPStatus.OK
