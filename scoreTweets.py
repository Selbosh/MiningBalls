import json

'''Very very basic sentiment scorer that takes tweets and scores them according to an external corpus.
Then returns time of tweet, hashtag(s) and score in a data structure.'''

filename = 'exampledata.txt'
f = open(filename, 'r')
for line in f:
	tweet = json.loads(line)

# def main():
	# print 'Stuff.'

# if __name__ == '__main__':
	# main()