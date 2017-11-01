from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import readini
db_connect_string= readini.get_db_config()
engin=create_engine(db_connect_string)
SessionType=scoped_session(sessionmaker(bind=engin,expire_on_commit=False))

def get_session():
    return  SessionType

from contextlib import contextmanager
@contextmanager
def session_scope():
    session=get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        