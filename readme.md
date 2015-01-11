## Plan so far
* ~~Find an upcoming match~~
* Start the Twitter streaming API one hour before
* End the stream one hour after
* Plot sentiment over time using R
* Look at past data as well
* Build a sentimental analysis machine
	- Start with a basic one
	- Then add one capable of learning

## Potential issues 
* If two matches are playing at the same time, what to do? Join all the search terms into one Stream request and somehow extricate the tweets later? Or just pick one match to follow (_say, using an RNG_) and ignore the other(s) on this occasion?
* Is the script to be started manually each day, or run automatically?
	- Sites like [Python Anywhere](https://www.pythonanywhere.com/) permit daily scheduling for free, but may or may not allow enough CPU time to keep the script running until the end of the stream(s).
	- Windows Task Scheduler can start the script each day. Just need to make sure output filenames are dynamic/unique to matches.

## To do
* ~~Manually create a dictionary of possible search terms for each team playing: (_e.g. Tottenham Hotspur FC might call for "Tottenham", "Spurs", "Tottenham Hotspur" and so on._) However this can be accepted as a limitation of the app for now; Twitter's search engine may be clever enough to work out which Tweets to return anyway...~~ Got a list of 'official' hashtags for each team in the 14-15 Premier League (see References).
* Improve the streamer so it writes useful information to a file, including tweet text, hashtags (maybe) and time of tweet. If possible exclude retweets
* ~~Find a way to schedule the streamer to start before kick off and the end after the final whistle. This may involve Windows Task Scheduler, or else a small helper script that periodically checks conditions and then triggers the main streamer (etc) when a match is taking place.~~
* Write an initial Python script to perform sentiment analysis using a corpus of positive and negative words. Be sure to remove stop words, hyperlinks etc.
	- Later improve with some form of machine learning to assign sentiment scores to terms not found in corpus
* Strip down the data to team (or hashtag), sentiment score and timestamp. Create density plot.
	- Maybe build into a Shiny app that allows adjustment of bandwidth of the density plot / width of bars in histograms. Host on http://selby.shinyapps.io

## References
* [RESTful football data](http://www.football-data.org/index "football-data.org")
* [Premier League team hashtags 2014-15](http://coolestguidesontheplanet.com/english-premiership-twitter-hashtags-2014-2015/)