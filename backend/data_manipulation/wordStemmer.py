import json
import re
from os.path import exists

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

BooleanOperators = ['AND', 'OR', 'NOT', 'and', 'or', 'not']


def stemLyrics():
    #if exists('./data/songs.json'):
    #    print("Stemmed data already exists.")
    #    return
    stemmer = PorterStemmer()

    inputData = json.load(open('./data/songs.json'))

    stopWords = set(stopwords.words('english'))

    outputData = []

    uniqueWords = []

    wordsCounter = {}

    for song in inputData:
        stemmed = []
        for lyric in song['lyrics'].split():
            lyric = re.sub('[^A-Za-z]+', '', lyric)

            if lyric not in stopWords and stemmer.stem(lyric) not in BooleanOperators and len(lyric) > 2:
                stemmed.append(stemmer.stem(lyric))

                if stemmer.stem(lyric) not in uniqueWords:
                    uniqueWords.append(stemmer.stem(lyric))

                if stemmer.stem(lyric) not in wordsCounter:
                    wordsCounter[stemmer.stem(lyric)] = 1
                else:
                    wordsCounter[stemmer.stem(lyric)] += 1

        song['lyrics'] = stemmed
        outputData.append(song)

    with open('./data/stemmedData.json', 'w') as outfile:
        json.dump(outputData, outfile)

    with open('./data/uniqueStemmedWords.txt', 'w') as outfile2:
        outfile2.write(str(uniqueWords))

    sortedCounter = dict(sorted(wordsCounter.items(), key=lambda item: item[1]))
    with open('./data/stemmedWordCount.txt', 'w') as outfile3:
        outfile3.write(str(sortedCounter))

    print("Created stemmed data.")
