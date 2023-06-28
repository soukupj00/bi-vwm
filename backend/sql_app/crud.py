from sqlalchemy.orm import Session

from sql_app import models


def getSong(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def getSongs(db: Session, skip: int = 0):
    return db.query(models.Song).offset(skip).all()


def getSongsForIds(db: Session, ids: list[int], skip: int = 0):
    return db.query(models.Song).filter(models.Song.id.in_(ids)).offset(skip).all()


def getSongIds(db: Session):
    return [r for (r,) in db.query(models.Song.id).all()]


def getDocumentsInLinkedList(db: Session, term: str):
    result = db.query(models.LinkedList.documents).filter(models.LinkedList.term == term).first()
    return result[0] if result else []


def getDocsForTerm(db: Session, term: str):
    songs = db.query(models.Song).filter(models.Song.lyrics.contains(term)).all()
    result = []
    for song in songs:
        result.append(song.id)
    if result:
        return result
    else:
        return None
