import twitter_api as api
import os
from bot.models import TwitterBot, Update

def get_mentions(twitter_id):
	KEYFILE_PATH = os.path.join("../", "keys.txt")
	execfile(KEYFILE_PATH)
	twitter = TwitterAPI(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_secret)
	
	try:
		Update.objects.filter(TwitterBot__twitter_handle=twitter_id)
		

