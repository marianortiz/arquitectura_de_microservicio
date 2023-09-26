from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def get_session():
    MYSQL_HOST = config('SQL_HOST')
    MYSQL_USER = config('SQL_USER')
    MYSQL_PASSWORD = config('SQL_PASS')
    MYSQL_BD = config('SQL_DATABASE')

    connection_str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_BD}'

    try:
        engine = create_engine(connection_str)
        Session = sessionmaker(engine)
        session = Session()

    except Exception as ex:
        raise ex
    return session


def create_models():
    MYSQL_HOST = config('SQL_HOST')
    MYSQL_USER = config('SQL_USER')
    MYSQL_PASSWORD = config('SQL_PASS')
    MYSQL_BD = config('SQL_DATABASE')

    connection_str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_BD}'

    engine = create_engine(connection_str)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
