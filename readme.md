## Plan so far
* Find an upcoming match
* Start the Twitter streaming API one hour before
* End the stream one hour after
* Plot sentiment over time using R
* Look at past data as well

## Potential issues 
* If _two_ matches are occurring at once, what to do? Join all the search terms into one Stream request and somehow extricate the tweets later? Or just pick one match to follow (_say, using an RNG_) and ignore the other(s) on this occasion?

## To do
* Manually create a dictionary of possible search terms for each team playing: _e.g. Tottenham Hotspur FC might call for "Tottenham", "Spurs", "Tottenham Hotspur" and so on._ However this can be accepted as a limitation of the app for now; Twitter's search engine may be clever enough to work out which Tweets to return anyway...

## Sources
* [RESTful football data](http://www.football-data.org/index "football-data.org")
* [Premier League team hashtags 2014-15](http://coolestguidesontheplanet.com/english-premiership-twitter-hashtags-2014-2015/)