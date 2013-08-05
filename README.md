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
   
   
   getTweets(screenName,NumberofTweets,bearerToken): 
   
      Retrieves Tweets which have been retweeted . The follower count of the users who have retweeted it is taken and 
      sorted. The sorted follower list is saved in the follower list. This follower list is then matched with all the users 
      who have retweeted and it is matched to find the users who match our criteria.
      This list is then saved in the People list.


   getData():
   
      This is the main function of the requester.py file.It returns the details of the people who satisfy the puzzle.
   
   
