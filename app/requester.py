import urllib
import urllib2
import base64
import httplib
from pprint import pprint
import sys # used for the storage class
import pycurl # used for curling
import base64 # used for encoding string
import urllib # used for enconding
import cStringIO # used for curl buffer grabbing
import json # used for decoding json token
import time # used for stuff to do with the rate limiting
from time import sleep # used for rate limiting
from time import gmtime, strftime # used for gathering time
bearerToken=""
class Person:
	def __init__(self,name=None,url=None,followers=None):
		self.screenName=name
		self.imageUrl=url
		self.followersCount=followers
	def name(self):
		return self.screenName
	def image(self):
		return self.imageUrl
	def followers(self):
		return str(self.followersCount)
People=[]
def createRequest(url,bearerToken):
	host="https://api.twitter.com"
	headers = [ 
	str("GET "+url+" HTTP/1.1"), 
	str("Host: api.twitter.com"), 
	str("User-Agent: jonhurlock Twitter Application-only OAuth App Python v.1"),
	str("Authorization: Bearer "+bearerToken+"")
	]
	buf = cStringIO.StringIO()
	results = ''
	pycurl_connect = pycurl.Curl()
	pycurl_connect.setopt(pycurl_connect.URL, host+url) # used to tell which url to go to
	pycurl_connect.setopt(pycurl_connect.WRITEFUNCTION, buf.write) # used for generating output
	pycurl_connect.setopt(pycurl_connect.HTTPHEADER, headers) # sends the customer headers above
	#pycurl_connect.setopt(pycurl_connect.VERBOSE, True) # used for debugging, really helpful if you want to see what happens
	pycurl_connect.perform() # perform the curl
	results += buf.getvalue() # grab the data
	pycurl_connect.close() # stop the curl
	results=json.loads(results)
	return results
	
def get_bearer_token(consumer_key,consumer_secret):
	# enconde consumer key
	consumer_key = urllib.quote(consumer_key)
	# encode consumer secret
	consumer_secret = urllib.quote(consumer_secret)
	# create bearer token
	bearer_token = consumer_key+':'+consumer_secret
	# base64 encode the token
	base64_encoded_bearer_token = base64.b64encode(bearer_token)
	# set headers
	headers = [
	"POST /oauth2/token HTTP/1.1", 
	"Host: api.twitter.com", 
	"User-Agent: Multunus App",
	"Authorization: Basic "+base64_encoded_bearer_token+"",
	"Content-Type: application/x-www-form-urlencoded;charset=UTF-8", 
	"Content-Length: 29"]
	# do the curl
	token_url = "https://api.twitter.com/oauth2/token"
	buf = cStringIO.StringIO()
	access_token = ''
	pycurl_connect = pycurl.Curl()
	pycurl_connect.setopt(pycurl_connect.URL, token_url) # used to tell which url to go to
	pycurl_connect.setopt(pycurl_connect.WRITEFUNCTION, buf.write) # used for generating output
	pycurl_connect.setopt(pycurl_connect.HTTPHEADER, headers) # sends the customer headers above
	pycurl_connect.setopt(pycurl_connect.POSTFIELDS, 'grant_type=client_credentials') # sends the post data
	#pycurl_connect.setopt(pycurl_connect.VERBOSE, True) # used for debugging, really helpful if you want to see what happens
	pycurl_connect.perform() # perform the curl
	access_token = buf.getvalue() # grab the data
	pycurl_connect.close() # stop the curl
	x = json.loads(access_token)
	bearer = x['access_token']
	return bearer

def getImage(screenName):
	url="/1.1/users/lookup.json?screen_name="+urllib.quote(screenName)+"&include_entities=true"
	result=createRequest(url,bearerToken)
	return result[0]['profile_image_url']

def getTweets(screenName,numberOfTweets,bearerToken):
	global People
	del People[:]
	url="/1.1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name="+urllib.quote(screenName)+"&count="+str(numberOfTweets)
	Tweets=createRequest(url,bearerToken)
	followers=[]
	rtData=[]
	newData=[]
	max=0
	for i in range(0,len(Tweets)):
		if (Tweets[i]['retweet_count']!=0):
			url="/1.1/statuses/retweets/"+str(Tweets[i]["id"])+".json"
			reTwit=createRequest(url,bearerToken)
			#print json.dumps(Tweets[i])
			#exit(0)
			for j in range(0,len(reTwit)):
				followers.append(reTwit[j]['user']['followers_count'])
			rtData.append(reTwit)
			#print followers
	followers=list(set(followers))
	followers.sort(reverse=True)
	#print followers
	for i in range(0,10):
		for reTwit in rtData:
			for j in range(0,len(reTwit)):
				if(reTwit[j]['user']['followers_count']==followers[i]):
					#print reTwit[j]['user']['screen_name'] +" : "+ str(reTwit[j]['user']['followers_count'])
					flag=0
					for person in People:
						if person.name()==reTwit[j]['user']['screen_name']:
							flag=1
					if flag==0:
						People.append(Person(reTwit[j]['user']['screen_name'],reTwit[j]['user']['profile_image_url'],reTwit[j]['user']['followers_count']))
	return People
def getData(screenName):
	global bearerToken
	CONSUMER_KEY = 'kiDqkeAri3jLhh2FJ8y0uA'
	CONSUMER_SECRET = 'vPujizuOfr5AlE1Ozfzv7qfC0UJej221aDZrayCjJwk'
	bearerToken=get_bearer_token(CONSUMER_KEY,CONSUMER_SECRET)
	#screenName="dhh"
	#print twitId
	return getTweets(screenName,20,bearerToken)
	#for person in People:
	#	print person.name() + " : " + person.followers() + " : " +person.image()
#getData()
