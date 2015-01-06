import json, pprint
from urllib2 import urlopen

"""
website = urlopen('http://www.football-data.org/soccerseasons/')
seasons = json.loads(website.read())
for season in seasons:
    print str(season['id']) + '\t' + str(season['caption']) #Name of each league
    # Note that the Premier League 2014/15 has id=354
    There is also a hashtag, 
"""

# The past week's Premier League Fixtures:
website = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=p7')
recentFixtures = json.loads(website.read())
print "The past 7 days' Premier League fixtures were:"
for fixture in recentFixtures:
    print '\t' + str(fixture['homeTeam']) + ' v ' + str(fixture['awayTeam'])
print

# The next week's Premier League Fixtures:
website = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=n7')
upcomingFixtures = json.loads(website.read())
print "Premier League football fixtures coming up in the next 7 days..."
for fixture in upcomingFixtures:
    print '\t' + str(fixture['homeTeam']) + ' v ' + str(fixture['awayTeam'])
print

print "And now time for some hashtags..."
hashtagFile = open('team_hashtags.json')
hashtagDict = json.loads(hashtagFile.read())

website = urlopen('http://football-data.org/soccerseasons/354/teams/')
premTeams = json.loads(website.read())
#Find the id of the home team
for fixture in upcomingFixtures:
    hT = fixture['homeTeam']
    print "Home team " + str(hT)
    for team in premTeams:
        if team['name']==hT:
            print "\t has ID " + str(team['id']) + " and hashtag #" + str(hashtagDict[str(team['id'])])
