from .models import User as Model
from App.drivers.sqlalchemy_config import get_session
from App.common.exceptions import UserNotFoundException


class UserRepository():
    entity = Model

    def fetch_all(self):
        session = get_session()
        users = []
        try:
            entities = session.query(self.entity).all()
            if entities is not None:
                for item in entities:
                    users.append(item.to_Json())
                return users
            else:
                return users
        except Exception as ex:
            raise ex('Ocurrio un error al Buscar usuarios')

    def fetch_one(self, username):
        session = get_session()
        try:
            user = session.query(self.entity).filter_by(
                username=username).first()
            if user is not None:
                return user.to_Json()
            else:
                return None
        except Exception as ex:
            raise ex('Ocurrio un error al Buscar usuarios')

    def store(self, user):
        try:
            session = get_session()
            session.add(user)
            session.commit()
            return user.to_Json()
        except Exception as ex:
            session.rollback()
            raise ex('Ocurrio un error al persistir el usuario')

    def delete(self, username):
        session = get_session()
        user = session.query(self.entity).filter_by(
            username=username).first()
        if not user:
            raise UserNotFoundException(
                'User NOT FOUND. {} with username {} not found'.format(self.entity.__name__, username))
        user = session.delete(user)
        session.commit()
        return '{} eliminado con Exito'.format(username)
