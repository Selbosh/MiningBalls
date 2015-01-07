import tweepy, time

class StdOutListener(tweepy.StreamListener):
    '''Collects and prints tweets from the streaming API.
    Ends after a fixed duration or maximum number of tweets,
    whichever one is the sooner.'''
    
    tweetCounter = 0
    
    def on_status(self, status):
        print('Tweet text:\t' + status.text)
        #for hashtag in status.entities['hashtags']:
        #    print(hashtag['text'])
        self.tweetCounter += 1
        print(self.tweetCounter)
        if self.tweetCounter < self.maxTweets:
            if time.time() < self.finishTime:
                return True
            else:
                print 'Time\'s up!'
        else:
            print 'Maximum tweets = ' + str(self.tweetCounter)
        return False

    def on_error(self, status_code):
        print('Error with code: ' + str(status_code))
        time.sleep(5)
        return True # Wait 5 seconds, then continue

    def on_timeout(self):
        print('Timeout...')
        time.sleep(5)
        return True # Wait 5 seconds, then continue


def authorise():
    consumer_key = "nFzKM3rCAnYJiGr5LweBgqjWi"
    consumer_secret = "15iZgSU8vxVUn8ZgG4LVeJCNwFlaCvSUIbQZLjigX7VFM0X7xU"
    access_token = "2548779734-IME2W1SESF4IbR4kyL9HQOwDlVMF9mZ09AKU2XQ"
    access_token_secret = "AeicxZGuZRIq8utpMIWsKJ59HP4jWSovPl3L9v7fADg50"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def getTweetsByHashtag(hashtag, stopAtCount, stopAtTime):
    try:
        StdOutListener.maxTweets = stopAtCount
        StdOutListener.finishTime = stopAtTime
        auth = authorise()
        streamingAPI = tweepy.streaming.Stream(auth, StdOutListener(), timeout=60)
        streamingAPI.filter(track=[hashtag], languages=['en'])
    except KeyboardInterrupt, e: #Ctrl+C
        print 'Stream interrupted by user (KeyboardInterrupt)'


if __name__ == '__main__':
    print 'Running script...'
    finalWhistle = time.time()+60 # One minute from now
    getTweetsByHashtag('cfc', 10, finalWhistle)
