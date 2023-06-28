import json

from sql_app.database import SessionLocal
from sql_app.models import Song, LinkedList


def addSongs(db):
    with open('./data/songs.json') as f:
        songs = json.load(f)

    for song in songs:
        # print(song)
        song_obj = Song(**song)
        # Add song only if the ID is not already present in database
        if not db.get(Song, {"id": song['id']}):
            db.add(song_obj)
    db.commit()


def addLinkedList(db):
    with open('./data/invertedList.json') as f:
        invertedList = json.load(f)

    for term in invertedList:
        # print(term)
        termObj = LinkedList(**term)
        # Add instance only if the term is not already present in database
        if db.query(LinkedList).filter_by(term=termObj.term).first() is None:
            db.add(termObj)
    db.commit()


def fillDatabaseWithData():
    db = SessionLocal()
    addSongs(db)
    addLinkedList(db)
    linkedList = db.query(LinkedList).all()
    songs = db.query(Song).all()
    print("Number of terms in linked list DB: " + str(len(linkedList)))
    print("Number of songs DB: " + str(len(songs)))
    # for ls in linkedList:
    #     print(ls.term, ls.documents)
    # for song in songs:
    #     print(song.id, song.artist, song.album, song.song, song.year)
    print("Filling of database completed.")
    # t = crud.getSongsForIds(db, [1, 100, 200, 412])
    # for i in t:
    #     print(i.__dict__)
