import tweepy
import wikipedia
from config import *


# Defining searching Wikipedia
def search():
  x = wikipedia.summary(searchtext, sentences=3)
#Defining the main program
def main():
  # Authorization.
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)
  
  # Not replying to old messages
  new_messages = api.direct_messages(count=1)
  old_messages = api.sent_direct_messages(count=1)
  for message in old_messages:
      old = message.recipient_id
  for message in new_messages:
     new = message.sender_id_str
     searchtext = message.text
     search()
     print("Messaging....")
     api.send_direct_message(new, x)
     print("Message sent.")
try:
  while True:
    main()
except Exception as e:
  print("Error: "+e)
  
