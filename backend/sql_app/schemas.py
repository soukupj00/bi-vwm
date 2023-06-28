from pydantic import BaseModel


class SongBase(BaseModel):
    id: int
    artist = str
    album = str
    song = str
    year = int
    lyrics = str


class SongCreate(SongBase):
    pass


class LinkedListBase(BaseModel):
    term: str
    documents = list
