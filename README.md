The twitter Multunus Puzzle

Depends on python-flask
use python run.py to run the webapp.

Modules

requester.py --> The Main Man
   This is the module that connects to the Twitter API .
   This module is divided into a few functions which hae the name as what they do.
   
   get_bearer_token(consumer Key,consumer secret) :
      My application uses application only auth to connect to Twitter .
      This function retrieves the bearer token from Twitter to make further requests to the Twitter API.
   createRequest(url,bearerToken):
      This module is used to place requests to the Twitter API and retrieve the appropriate json data.
   getImage(screenName) :
      This module retrieves the profile image url for the particular Screen Name
   
