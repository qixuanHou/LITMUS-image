import got3 as got
import datetime
import sys,getopt,datetime,codecs, requests
from dateutil.relativedelta import *

keywordList = ["landslide", "rockslide", "mudslide", "rockfall"]
startDate = datetime.date(2018, 1, 1)
endDate = datetime.date(2019, 1, 1)


def printTweet(tweets, outputFileName):
	outputFile = codecs.open(outputFileName, "w+", "utf-8")
	outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink;img')

	for t in tweets:
		outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s;%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink, t.img)))
		if (t.img):
			img_data = requests.get(t.img).content
			with open('imgs/%s.jpg'%t.id, 'wb') as handler:
				handler.write(img_data)
	outputFile.flush()


for key in keywordList:
	while startDate < endDate:
		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(key).setSince(startDate.strftime('%Y-%m-%d')).setUntil((startDate + relativedelta(months=+1)).strftime('%Y-%m-%d'))
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)
		printTweet(tweets, "%s_%s.txt"%(key,startDate.strftime('%Y-%m')))
		startDate = startDate + relativedelta(months=+1)

