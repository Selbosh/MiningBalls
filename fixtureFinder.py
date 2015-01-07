import json, stream, time
from urllib2 import urlopen



# Note that the Premier League 2014/15 season has id=354

recentFixturesData = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=p7')
recentFixtures = json.load(recentFixturesData)
print "The past 7 days' Premier League fixtures were:"
for fixture in recentFixtures:
    print '\t' + str(fixture['homeTeam']) + ' v ' + str(fixture['awayTeam'])
print

timeFormat = '%Y-%m-%dT%H:%M:%SZ'

upcomingFixturesData = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=n7')
upcomingFixtures = json.load(upcomingFixturesData)
print "Premier League football fixtures coming up in the next 7 days..."
for fixture in upcomingFixtures:
    kickOff = time.strptime(fixture['date'], timeFormat)
    kickOffTime = time.mktime(kickOff)
    finalWhistleTime = kickOffTime + 7200 # allow two hours
    finalWhistle = time.strftime(timeFormat, time.gmtime(finalWhistleTime))
    print '\t' + str(fixture['homeTeam']) + ' v ' + str(fixture['awayTeam']) + '\t @ ' + str(fixture['date']) + ', finishing ' + str(finalWhistle)
print

print "And now time for some hashtags..."
hashtagFile = open('team_hashtags.json')
hashtagDict = json.loads(hashtagFile.read())

premTeamsData = urlopen('http://football-data.org/soccerseasons/354/teams/')
premTeams = json.load(premTeamsData)
for fixture in upcomingFixtures:
    hT = fixture['homeTeam']
    print "\tHome team " + str(hT)
    for team in premTeams:
        if team['name']==hT: #Find the id of the home team
            print "\t has ID " + str(team['id']) + " and hashtag #" + str(hashtagDict[str(team['id'])])


#stream.search('#cfc', finalWhistleTime) # Will stream 10 tweets right now containing the keyword in arg
