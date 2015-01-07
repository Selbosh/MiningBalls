import tweepy, codecs, time, os

# Keys and tokens
consumer_key = "nFzKM3rCAnYJiGr5LweBgqjWi"
consumer_secret = "15iZgSU8vxVUn8ZgG4LVeJCNwFlaCvSUIbQZLjigX7VFM0X7xU"
access_token = "2548779734-IME2W1SESF4IbR4kyL9HQOwDlVMF9mZ09AKU2XQ"
access_token_secret = "AeicxZGuZRIq8utpMIWsKJ59HP4jWSovPl3L9v7fADg50"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print 'Authenticated using account ' + api.me().name

class listener(tweepy.streaming.StreamListener):
    def __init__(self, api=None):
        super(listener, self).__init__()
        self.num_tweets=0
    def on_status(self, status):
        try:
            feed = status.text.encode('utf-8')
            text = feed.replace('\n',' ')
            self.num_tweets+=1
            print str(self.num_tweets) + '. ' + text
            saveThis = text
        except BaseException, e:
            print 'failed on data', str(e)
            time.sleep(5)
        #if self.num_tweets<10:
        if time.time() < finalWhistleTime: # Keep streaming until the match has finished 
            saveFile = open('savedTweets.txt','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
        else:
            print "Match over. Shutting down."
            os._exit(0) #Possibly a bit sledgehammery? May need to restructure this.
    def on_error(self, status):
        print status

def search(keyword, until):
    print 'Mining tweets containing "' + keyword + '"...'
    twitterStream = tweepy.Stream(auth, listener())
    twitterStream.filter(track=[keyword], languages=['en'])

#searchFor = "#cfc" # pick a keyword, or a list (if so, remove the [] below)
#print 'Mining tweets containting "' + searchFor + '"...'
#twitterStream = tweepy.Stream(auth, listener())
#twitterStream.filter(track=[searchFor], languages=['en'])
