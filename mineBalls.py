import json, sched, time
from datetime import datetime
from urllib2 import urlopen

'''The general idea is to run the script on match day before kick-off.
It should find the time of today's matches (if any) and schedule stream(s) accordingly.'''

def kickOff(match):
	timeFormat = '%Y-%m-%dT%H:%M:%SZ'
	return datetime.strptime(match['date'], timeFormat)

def matchesOfTheDay():
	'''Returns a list of matches (each a dictionary) yet to kick off today.'''
	upcomingFixturesData = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=n7') #Next 7 days
	upcomingFixtures = json.load(upcomingFixturesData)
	gamesToday = []
	for fixture in upcomingFixtures:
		if kickOff(fixture).date() == datetime.today().date():
			gamesToday.append(fixture)
	#if gamesToday == []:
		#print "There are no upcoming Premier League football matches today."
	return gamesToday

def hashtags(ID):
	matchID = str(ID)
	fixtureData = urlopen('http://football-data.org/soccerseasons/354/fixtures/?id='+matchID)
	
	homeTeam =
	with open('team_hashtags.json') as hashtagFile:
		hashtagDict = json.loads(hashtagFile.read())
	return hashtagDict[matchID]
	
def streamer():
	'''Just a shell for now. As all matches are the same length(ish) the streaming duration (120 min?) can be hardcoded into the streamer.'''
	print 'Streaming...', time.time()
	
def streamScheduler(matchList):
	'''Creates a queue of processes at today's kick-off times, input as a list of match IDs'''
	s = sched.scheduler(time.time, time.sleep)
	for fixture in matchList:
		scheduleTime = time.mktime(kickOff(fixture).timetuple())
		preMatch = 60*15 #minutes before kick-off
		s.enterabs(scheduleTime-preMatch, 1, streamer, ()) #arguments may include team names/IDs or hashtags or keywords
		print 'Stream scheduled for', kickOff(fixture)
	try:
		s.run()
	except KeyboardInterrupt:
		print 'Stream scheduler cancelled by user (KeyboardInterrupt)'

if __name__ == '__main__':
	#print matchesOfTheDay()
	print hashtags(563)
	streamScheduler(matchesOfTheDay())