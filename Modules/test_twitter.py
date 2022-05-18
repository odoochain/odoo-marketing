import tweepy
from requests_oauthlib import OAuth1Session
import requests
import base64



# Authenticate to Twitter
auth = tweepy.OAuthHandler("1PjCbI9T3Ne060REhBvQUdYmJ", "Hts07ntx9ucLxPsXdvLx3hGUeMBuejizJiQhSoBFQXG2eqxnns")
auth.set_access_token("1526392550952554498-oQ4la4UQeo8ywDYDZliuj9JIbv3QTQ", "0K0r8or5Dz0AkbYJYdTunhqhMKKfAUWZJwFOJRZ359Oqi")

# Create API object
api = tweepy.API(auth)

# Create a tweet

tweet_text= ""
image="/home/yvan/src/odoo-marketing/Modules/fw_odoo_twitter_post/static/description/icon.png"
media = api.media_upload(image)
print(media)
api.update_status(status=tweet_text, media_ids=[media.media_id])

"""
CK = "1PjCbI9T3Ne060REhBvQUdYmJ"
CS = "Hts07ntx9ucLxPsXdvLx3hGUeMBuejizJiQhSoBFQXG2eqxnns"
AT = "1526392550952554498-oQ4la4UQeo8ywDYDZliuj9JIbv3QTQ"
AS = "0K0r8or5Dz0AkbYJYdTunhqhMKKfAUWZJwFOJRZ359Oqi"

url_text= "https://api.twitter.com/1.1/statuses/update.json"
#url_media= "https://api.twitter.com/1.1/media/upload.json"

params= {"status": "Hello, test!"}
files= {
        "media": open("/home/yvan/src/odoo-marketing/Modules/fw_odoo_twitter_post/static/description/icon.png", "rb")
        }

twitter = OAuth1Session(CK,CS,AT,AS)
#req = twitter.post(url_text, params=params)
req = twitter.post(url_text, files=files)

if req.status_code == 200:
    print("ok")
else:
    print("Error: %d" % req.status_code)
  """
