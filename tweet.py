import tweepy
auth = tweepy.OAuthHandler("Kihyf0vB5AvcnXE8dIcEXLI4j","fyf1g9adE1vWoD9dI3u6w3PoqLmI4bj4rWSXo04KCA7rcvU9im")
auth = tweepy.OAuthHandler("Kihyf0vB5AvcnXE8dIcEXLI4j","fyf1g9adE1vWoD9dI3u6w3PoqLmI4bj4rWSXo04KCA7rcvU9im",None)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get request token.")
 
session.set("request_token", auth.request_token)