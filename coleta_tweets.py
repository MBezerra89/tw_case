#!/usr/bin/env python3

# Importando bibliotecas necessarias.
import tweepy as tw

# Autenticacao com a API, Por segurança as chaves ficarão salvas no servidor no arquivo key.txt.

with open('key.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth)

# Coletando hashtags #openbanking, #remediation, #devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing

openbanking = "#openbanking" + " -filter:retweets"
remediation = "#remediation" + " -filter:retweets"
devops = "#devops" + " -filter:retweets"
sre = "#sre" + " -filter:retweets"
microservices = "microservices" + " -filter:retweets"
observability = "#observability" + " -filter:retweets"
oauth = "#oauth" + " -filter:retweets"
metrics = "#metrics" + " -filter:retweets"
logmonitoring = "#logmonitoring" + " -filter:retweets"
opentracing = "#opentracing" + " -filter:retweets"

cursor = tw.Cursor (api.search,
        q=openbanking).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location,tweet.user.lang, sep=',', end=' ,#openbanking\n')

cursor = tw.Cursor (api.search,
        q=remediation).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang, sep=',', end=' ,#remediation\n')

cursor = tw.Cursor (api.search,
        q=devops).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang, sep=',', end=' ,#devops\n')
	 
cursor = tw.Cursor (api.search,
        q=sre).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang, sep=',', end=' ,#sre\n')
	 
cursor = tw.Cursor (api.search,
        q=microservices).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang, sep=',', end=' ,#microservices\n')	 

cursor = tw.Cursor (api.search,
        q=observability).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang,sep=',', end=' ,#observability\n')
	 
cursor = tw.Cursor (api.search,
        q=oauth).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang,sep=',', end=' ,#oauth\n')
	 
cursor = tw.Cursor (api.search,
        q=metrics).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang, sep=',', end=' ,#metrics\n')
	 
cursor = tw.Cursor (api.search,
        q=logmonitoring).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang,sep=',', end=' ,#logmonitoring\n')

cursor = tw.Cursor (api.search,
        q=opentracing).items(100)

for tweet in cursor:
     print(tweet.created_at,tweet.user.screen_name,tweet.user.followers_count,tweet.user.location, tweet.user.lang,sep=',', end=' ,#opentracing\n')