from .respository import UserRepository as Repository
from .models import User
from App.common.exceptions import ValuesNullException, UserAlreadyExistException


class UserService():

    def __init__(self):
        repository = Repository()
        self.repository = repository

    def fetch_all(self) -> list():
        return self.repository.fetch_all()

    def fetch_one(self, username: str):
        try:
            result = self.repository.fetch_one(username)
            return result
        except Exception as ex:
            return ex

    def add_user(self, user):
        for clave, valor in user.items():
            if valor is None or valor == '':
                message = f'La clave "{clave}" tiene un valor vacío o una cadena vacía'
                raise ValuesNullException(message)
        if self.repository.fetch_one(user['username']) is None:
            entity = User(
                username=user['username'],
                user_password=user['user_password'],
                user_email=user['user_email'],
                user_first_name=user['user_first_name'],
                user_last_name=user['user_last_name'])
        else:
            raise UserAlreadyExistException('El usuario ya existe')

        return self.repository.store(entity)

    def delete_user(self, username):
        return self.repository.delete(username)
