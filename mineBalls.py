import json, sched, time
from datetime import datetime
from urllib2 import urlopen
import matchStreamer

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
	if gamesToday == []:
		print "There are no upcoming Premier League football matches today."
	return gamesToday

def hashtags(matchID):
	fixtureData = urlopen('http://football-data.org/fixtures/' + str(matchID))
	fixture = json.load(fixtureData)
	homeTeam = fixture['homeTeam']
	awayTeam = fixture['awayTeam']
	with open('team_hashtags.json') as htFile:
		hashtagDict = json.loads(htFile.read())
	return [hashtagDict[homeTeam], hashtagDict[awayTeam]]
	
def streamer(matchID, endTime):
	print 'Streaming started at', datetime.today()
	#endTime = time.time()+10 #TEST
	matchStreamer.getTweetsByHashtag(matchID, hashtags(matchID), 10000, endTime)
	
def streamScheduler(matchList):
	'''For today's matches, schedules streamers to start 15 minutes before kick-off and run for 2 hours'''
	s = sched.scheduler(time.time, time.sleep)
	for fixture in matchList:
		kickOffTime = time.mktime(kickOff(fixture).timetuple())
		preKickOff = kickOffTime - 60*15
		endTime = time.mktime(kickOff(fixture).timetuple()) + 60*105
		s.enterabs(preKickOff, 1, streamer, (fixture['id'], endTime))
		print 'Stream scheduled for', fixture['homeTeam'], 'vs.', fixture['awayTeam']
		print 'Kick-off is at', kickOff(fixture), 'and streamer will start 15 mins before.'
	try:
		s.run()
	except KeyboardInterrupt:
		print 'Stream scheduler cancelled by user (KeyboardInterrupt)'

def main():
	streamScheduler(matchesOfTheDay())

if __name__ == '__main__':
	#print 'Hashtags:', hashtags(136836)
	#print 'Match ID:', matchesOfTheDay()[0]['id']
	main()