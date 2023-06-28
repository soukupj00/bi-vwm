from sqlalchemy import Integer, String, Column, ARRAY
from sql_app.database import Base


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    song = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    lyrics = Column(String, nullable=False)


class LinkedList(Base):
    __tablename__ = 'linked_list'

    term = Column(String, primary_key=True)
    documents = Column(ARRAY(Integer), nullable=False)
