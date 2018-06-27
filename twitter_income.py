from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="VpRi7WMQEKPPEziMJAA1utuIy"
csecret="FzDDPgrnc3rBmBmtvxiGjRYZqvqCG7BxHspktDwZAGce1XAU33"
atoken="997587083140222981-8COuhezuDUTugiRLLI1riMojbqqP8tk"
asecret="0mGZrUFKpuCRbR7tysngqPUgyjgU2Fo5KMZ4GV9kT4Hut"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            print(tweet)
            sentiment_value = s.sentiment(tweet)
            print(tweet,sentiment_value)

            if confidence*100 >= 80:
                output = open("twitter_output.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
            
            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
