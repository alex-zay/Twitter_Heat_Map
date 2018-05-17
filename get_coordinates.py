import tweepy
import json

auth = tweepy.OAuthHandler('XXXXXXX', 'XXXXXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXX-XXXXXXXXXX', 'XXXXXXXXXXXXXXXXXX')
api = tweepy.API(auth)


def search_by_location(latitude, longitude, radius, number_of_tweets):

    lat = str(latitude)
    long = str(longitude)
    # radius distance should be given in kilometers
    dis = str(radius)
    num = int(number_of_tweets)

    tweets = tweepy.Cursor(api.search, geocode=lat+','+long+','+dis+"km").items(num)

    for tweet in tweets:
        data = json.dumps(tweet._json)
        parseable_data = json.loads(data)
        try:
            print(parseable_data['geo']['coordinates'])
        except:
            pass


def search_by_query(search_term, number_of_tweets):
    
    query = str(search_term)
    num = int(number_of_tweets)
    tweets = tweepy.Cursor(api.search, q=query).items(num)

    for tweet in tweets:
        data = json.dumps(tweet._json)
        parseable_data = json.loads(data)
        try:
            print(parseable_data['text'])
        except:
            pass

# latitude and longitude of the statue of liberty
search_by_location(40.6892, -74.0454, 1, 100)
