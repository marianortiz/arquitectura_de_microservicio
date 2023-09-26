from flask import Blueprint, jsonify, request
from http import HTTPStatus
from .service import UserService as Service
from App.common.decorators import exception_manager

service = Service()

user_page = Blueprint('users', __name__)


@user_page.route('/', methods=['GET'])
@exception_manager
def get_users() -> list():
    result = service.fetch_all()
    if len(result) == 0:
        return jsonify('Users Not found'), HTTPStatus.NOT_FOUND
    return jsonify(result), HTTPStatus.OK


@user_page.route('/<string:username>')
@exception_manager
def get_user(username) -> dict():
    result = service.fetch_one(username)
    if result is None:
        return jsonify(f'User {username} not found'), HTTPStatus.NOT_FOUND
    return jsonify(result), HTTPStatus.OK


@user_page.route('/create_user', methods=['POST',])
@exception_manager
def add_user() -> dict():
    user = request.get_json()
    store_data = service.add_user(user)
    return jsonify(store_data), HTTPStatus.CREATED


@user_page.route('/delete/<string:username>', methods=['DELETE',])
@exception_manager
def delete_user(username):
    result = service.delete_user(username)
    return {'message': result}, HTTPStatus.OK
