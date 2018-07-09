import tweepy
auth = tweepy.OAuthHandler("Kihyf0vB5AvcnXE8dIcEXLI4j","fyf1g9adE1vWoD9dI3u6w3PoqLmI4bj4rWSXo04KCA7rcvU9im")
auth.set_access_token("996686256619868162-caVORTMLw08Wpfbc2wxuS6alSLWmJAn","pNGAPP6kD9oO2KglNwOXPgDv7sHFBT4nBqON2xPw8zhUH")
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print(dir(tweet))
    print(tweet.text.encode("utf-8"))
    
user = api.get_user("twitter")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print("friends.screen_name")