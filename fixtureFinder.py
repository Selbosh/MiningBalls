import json, pprint
from urllib2 import urlopen

"""
website = urlopen('http://www.football-data.org/soccerseasons/')
seasons = json.loads(website.read())
for season in seasons:
    print str(season['id']) + '\t' + str(season['caption']) #Name of each league
    # Note that the Premier League 2014/15 has id=354
"""

# The past week's Premier League Fixtures:
website = urlopen('http://football-data.org/soccerseasons/354/fixtures/?timeFrame=p7')
fixtures = json.loads(website.read())
print "The past 7 days' Premier League fixtures were:"
for match in fixtures:
    print '\t' + str(match['homeTeam']) + ' v ' + str(match['awayTeam'])
