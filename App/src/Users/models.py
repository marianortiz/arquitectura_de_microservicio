from sqlalchemy import Column, String, Integer
from App.drivers.sqlalchemy_config import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, unique=True, autoincrement=True)
    username = Column(String(50), nullable=False,
                      unique=True, primary_key=True)
    user_password = Column(String(100), nullable=False)
    user_email = Column(String(70), nullable=False)
    user_first_name = Column(String(50), nullable=False)
    user_last_name = Column(String(50), nullable=False)

    def __init__(self, username, user_password, user_email, user_first_name, user_last_name):
        self.username = username
        self.user_password = user_password
        self.user_email = user_email
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name

    def to_Json(self):
        return {
            'username': self.username,
            'email': self.user_email,
            'first_name': self.user_first_name,
            'last_name': self.user_last_name
        }
