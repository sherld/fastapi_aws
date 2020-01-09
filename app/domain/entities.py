import contextlib
from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime
from app.database import Base, Session


@contextlib.contextmanager
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()


class Todo(Base):
    __tablename__ = 'todos'
    id = Column('id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    done = Column(Boolean)
    pub_date = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

    @classmethod
    def read_todos(cls):
        with get_db() as db:
            return db.query(cls).all()

    @classmethod
    def create_todo(cls, title, text):
        return cls(title, text)

    def create(self):
        with get_db() as db:
            db.add(self)
            db.commit()
            db.refresh(self)
