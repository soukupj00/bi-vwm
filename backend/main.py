import time

from fastapi import FastAPI, Depends, HTTPException, Query
# an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from data_manipulation import invertList, fillDatabase
from data_manipulation import wordStemmer
from data_manipulation.queryParser import retrieveDocumentIds
from sql_app import models, crud
from sql_app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def appCreateStemmedData():
    wordStemmer.stemLyrics()


@app.on_event("startup")
def app_createLinkedList():
    invertList.createInvertedList()


@app.on_event("startup")
def app_fillDatabase():
    fillDatabase.fillDatabaseWithData()


@app.get("/songs")
async def read_songs(q: str = Query(None), skip: int = 0, db: Session = Depends(get_db)):
    print("Received query: " + q)
    startTime = time.time()
    songIds = retrieveDocumentIds(q)
    endTime = time.time()
    execTime = (endTime - startTime) * 1000
    print("Time taken: {:.2f} ms".format(execTime))
    songs = crud.getSongsForIds(db, songIds, skip)
    return songs


@app.get("/songs/{song_id}")
async def get_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.getSong(db, song_id=song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
