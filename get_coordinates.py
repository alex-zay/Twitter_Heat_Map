import tweepy
import json

auth = tweepy.OAuthHandler('XXXXXXX', 'XXXXXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXX-XXXXXXXXXX', 'XXXXXXXXXXXXXXXXXX')
api = tweepy.API(auth)


def search_by_location(latitude, longitude, radius, number_of_tweets):

    lat = str(latitude)
    lon = str(longitude)
    # radius distance should be given in kilometers
    dis = str(radius)
    num = int(number_of_tweets)

    tweets = tweepy.Cursor(api.search, geocode=lat+','+lon+','+dis+"km").items(num)
    file = open('data.json', 'w')
    # empty list to contain coordinates
    l = []
    for tweet in tweets:
        # make tweets json format
        data = json.dumps(tweet._json)
        parseable_data = json.loads(data)
        try:
            # add collected coordinates to list
            l.append(parseable_data['geo']['coordinates'])
        except:
            pass
    # converts list to json
    list_to_json = json.loads(str(l))
    # formats json so it's readable
    json_list = json.dumps(list_to_json, indent=4)
    # writes formatted json to file
    file.write(json_list)
    file.close()

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
