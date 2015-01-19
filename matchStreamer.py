import tweepy, time, json
import sys, codecs

# Fix for printing to Windows console
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

class StdOutListener(tweepy.StreamListener):
    '''Collects tweets from the streaming API and writes to a file.
    Ends after a fixed duration or maximum number of tweets ---
    whichever is sooner.'''
    
    tweetCounter = 0
    
    def on_status(self, status):
        f = open(self.filename, 'a')
        output = json.dumps(status._json)
        f.write(output.encode('utf-8')+'\n')
        f.close()
        self.tweetCounter += 1
        print self.tweetCounter, status.user.screen_name
        if self.tweetCounter < self.maxTweets:
            if time.time() < self.finishTime:
                return True
            else:
                print 'Time\'s up!'
        else:
            print 'Hit maximum tweet count =', str(self.tweetCounter)
        return False

    def on_error(self, status_code):
        print >> sys.stderr, 'Error with code:', str(status_code)
        time.sleep(5)
        return True # Wait 5 seconds, then continue

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        time.sleep(90)
        return True # Wait 5 seconds, then continue


def authorise():
    consumer_key = "nFzKM3rCAnYJiGr5LweBgqjWi"
    consumer_secret = "15iZgSU8vxVUn8ZgG4LVeJCNwFlaCvSUIbQZLjigX7VFM0X7xU"
    access_token = "2548779734-IME2W1SESF4IbR4kyL9HQOwDlVMF9mZ09AKU2XQ"
    access_token_secret = "AeicxZGuZRIq8utpMIWsKJ59HP4jWSovPl3L9v7fADg50"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def getTweetsByHashtag(filename, hashtags, stopAtCount, stopAtTime):
    try:
        StdOutListener.filename = 'tweets/' + str(filename)+ ".txt"
        StdOutListener.maxTweets = stopAtCount
        StdOutListener.finishTime = stopAtTime
        auth = authorise()
        sAPI = tweepy.streaming.Stream(auth, StdOutListener(), timeout=60)
        sAPI.filter(track=hashtags, languages=['en'])
    except tweepy.TweepError, e:
            print e.message
            if e.message == 'Not authorized.':
                    pass
            elif e.message == [{u'message': u'Rate limit exceeded', u'code': 88}]:
                    print "Start : %s" % time.ctime()
                    time.sleep(930)
                    print "End : %s" % time.ctime()
            else:
                    pass
    except Exception, e:
        print e
    except KeyboardInterrupt, e: #Ctrl+C
        print 'Stream interrupted by user (KeyboardInterrupt)'
    

if __name__ == '__main__':
    print 'Running script...'
    test1Min = time.time()+60
    getTweetsByHashtag('exampledata', ['football'], 100, test1Min)
