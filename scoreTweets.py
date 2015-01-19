import json, sys, time, csv
from string import punctuation
from urllib2 import urlopen
from mineBalls import hashtags as matchHashtags

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

def tweetHashtags(tweet, matchTags):
	tags = [ht['text'] for ht in tweet['entities']['hashtags'] if ht['text'] in matchTags]
	if len(tags)>1:
		return ['Both']
	else: return tags
	# homeTag = ''
	# awayTag = ''
	# for tt in tweet['entities']['hashtags']:
		# if matchTags[0] == tt['text']:
			# homeTag = matchTags[0]
		# if matchTags[1] == tt['text']:
			# awayTag = matchTags[1]
	# return [homeTag, awayTag]

def matchSentiment(matchID):
    sentDict = loadCorpus('AFINN-111.txt')
    tweets = loadTweets('tweets\\'+str(matchID)+'.txt')
    matchTags = matchHashtags(matchID)
    with open('tweets\\'+str(matchID)+'.csv', 'wb') as csvfile:
        print >> sys.stdout, 'Writing data to file...'
        output = csv.writer(csvfile, delimiter=',')
        output.writerow(["sentiment","time","hashtags"])
        for tweet in tweets:
            output.writerow([sentiment(tweet, sentDict), timePosted(tweet)] + tweetHashtags(tweet,matchTags))
    print >> sys.stdout, 'Completed'

if __name__ == '__main__':
	matchSentiment(136836)
	#print matchHashtags(136836)
