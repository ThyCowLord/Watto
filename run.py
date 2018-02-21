import tweepy, wikipedia, smtplib, random, os, sys, praw
from config import *

# Defining searching Wikipedia
def search():
  x = wikipedia.summary(searchtext, sentences=3)
def report():
  if opt-in == 0:
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(email, email-password)
    server.sendmail(email, email, searchtext)
 if reddit-opt-in == 0:
  r = praw.Reddit(user_agent = 'Watto', client_id = client_id, client_secret = client_secret, username = username, password)
  r.submit(subreddit, 'Watto Reports', text = message.text)
#Defining the main program
def main():
  # Authorization.
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)
  poob = random.randint(1, cat-attack-chance)
  noob = random.randint(1, cat-attack-chance)
  if noob == poob:
     os.system("python cat-attack.py")
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
     report()
     
try:
  while True:
    main()
except Exception as e:
  print("Error: "+e)
  
