import json, sys
from string import punctuation

'''Very very basic sentiment scorer that takes tweets and scores them according to an external corpus.
Then returns time of tweet, hashtag(s) and score in a data structure.'''

def loadCorpus(file):
    '''Opens a tab-separated file with 2 columns and returns a dictionary'''
    with open(file, 'r') as f:
        corpus = {line.split('\t')[0]: float(line.split('\t')[1]) for line in f}    
    return corpus

def sentiment(text, corpus):
    '''Sums sentiment score of words in a string that are found in a corpus'''
    print text
    score = 0.0
    words = text.split(' ')
    for word in words:
        if word in corpus:
            print '###'+word, corpus[word]
            score += corpus[word]
    return score

def loadTweets(file):
    '''Loads JSON-formatted tweets (one tweet per line) into a list'''
    with open(file, 'r') as f:
        tweetList = [json.loads(line) for line in f]
    print >> sys.stdout, len(tweetList), 'tweets loaded'
    return tweetList

def readTweet(tweet):
    '''Return text, possibly with hashtags and symbols removed'''
    textRaw = tweet['text'].lower().strip()
    #remove URLs here plz
    textClean = "".join(c for c in textRaw if c not in punctuation)
    return textClean

def main():
    sentDict = loadCorpus('AFINN-111.txt')
    tweets = loadTweets('exampledata.txt')
    for tweet in tweets[10:50]:
        tweetText = readTweet(tweet)
        print 'CLEANED', '*'*30
        print sentiment(tweetText, sentDict)
        print 'UNCLEAN', '*'*30
        print sentiment(tweet['text'], sentDict)
        print '='*50

if __name__ == '__main__':
        main()
