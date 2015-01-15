import json, sys, time, csv
from string import punctuation

'''Very very basic sentiment scorer that takes tweets and scores them according to an external corpus.
Then returns time of tweet, hashtag(s) and score in a data structure.'''

def loadCorpus(file):
    '''Opens a tab-separated file with 2 columns and returns a dictionary'''
    with open(file, 'r') as f:
        corpus = {line.split('\t')[0]: float(line.split('\t')[1]) for line in f}    
    return corpus

def loadTweets(file):
    '''Loads JSON-formatted tweets (one tweet per line) into a list'''
    with open(file, 'r') as f:
        tweetList = [json.loads(line) for line in f]
    print >> sys.stdout, len(tweetList), 'tweets loaded'
    return tweetList

def sentiment(tweet, corpus):
    '''Sums sentiment score of words in a tweet that are found in a corpus'''
    score = 0.0
    textRaw = tweet['text'].lower().strip()
    #remove URLs here plz
    text = "".join(c for c in textRaw if c not in punctuation)
    words = text.split(' ')
    for word in words:
        if word in corpus:
            score += corpus[word]
    return score

def timePosted(tweet):
    #e.g. "Wed Aug 27 13:08:45 +0000 2008"
    created = time.mktime(time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    return created #since epoch; in R retrievable using as.POSIXct(time, origin="1970-01-01")

def hashtags(tweet):
    '''Have two columns in output: binary variables indicating if home or away team hashtag mentioned'''
    tags = [ht['text'] for ht in tweet['entities']['hashtags'] if ht['text'] in ['football']] #change to list of all hashtags
    if len(tags)>0:
        return tags[0]
    else: return None

def main():
    sentDict = loadCorpus('AFINN-111.txt')
    tweets = loadTweets('exampledata.txt')
    with open('outputdata.csv', 'wb') as csvfile:
        print >> sys.stdout, 'Writing data to file...'
        output = csv.writer(csvfile, delimiter=',')
        output.writerow(["sentiment","time","hashtags"])
        for tweet in tweets[:100]:
            output.writerow([sentiment(tweet, sentDict), timePosted(tweet), hashtags(tweet)])

if __name__ == '__main__':
        main()
