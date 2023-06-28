import json
import re
from os.path import exists

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

BooleanOperators = {'AND', 'OR', 'NOT', 'and', 'or', 'not'}


def createInvertedList():
    #if exists('./data/songs.json'):
    #    print("Inverted list already exists.")
    #    return

    # Declare stemmer
    stemmer = PorterStemmer()

    # Declare stopwords
    stopWords = set(stopwords.words('english'))

    # Load data in JSON
    inputData = json.load(open('./data/songs.json'))

    terms = []

    # Get keywords and stem the files
    for song in inputData:
        stemmed = []
        for lyric in song['lyrics'].split():
            lyric = re.sub('[^A-Za-z]+', '', lyric)
            if lyric not in stopWords and stemmer.stem(lyric) not in terms and stemmer.stem(
                    lyric) not in BooleanOperators and len(lyric) > 2:
                terms.append(stemmer.stem(lyric))
            stemmed.append(stemmer.stem(lyric))
        song['lyrics'] = stemmed

    # print(terms)
    print("Term count: " + str(len(terms)))
    print("Song count: " + str(len(inputData)))

    # Inverted list with terms
    keywordArray = []

    # Go through all found terms and find songs, that have given terms in lyrics
    for term in terms:
        tmpData = {'term': term}
        songArray = []
        for song in inputData:
            if term in song['lyrics']:
                songArray.append(song['id'])
        tmpData['documents'] = songArray
        keywordArray.append(tmpData)

    with open('./data/invertedList.json', 'w') as outputFile:
        json.dump(keywordArray, outputFile)

    print("Created inverted list.")
