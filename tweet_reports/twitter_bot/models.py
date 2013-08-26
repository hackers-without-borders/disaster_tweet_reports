from django.db import models

# Create your models here.

#The "TwitterBot" i.e. TwitterBot that aggregates tweets from followers
class TwitterBot(models.Model):
	twitter_handle = models.CharField(max_length=30)
	oauth_token  = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)
	#need to keep list of followers so bot knows who to follow back
	def __unicode__(self):
		return self.twitter_handle

#The parsed version of an incoming tweet
class Update(models.Model):
	tweet_id = models.IntegerField(blank=False, db_index=True)
	TwitterBot = models.ForeignKey(TwitterBot) #which Bot the Update is associated with
	tweet_text = models.CharField(max_length=1000)

	#handle the tweet came from
	tweet_origin = models.CharField(max_length=30) 
	tweet_geocode = models.CharField(max_length=200)
	#tweet_image = models.ImageField(upload_to=None)

	tweet_trimmed = models.CharField(max_length = 2000)
