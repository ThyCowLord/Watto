#!/usr/bin/python
import tweepy
import time
import sys
import requests
import os
import urllib.request
import xmltodict
from config import *


class Colour:
    Green, Red, White, Yellow = '\033[92m', '\033[91m', '\033[0m', '\033[93m'

print(Colour.Yellow + """
╦═╗╔═╗╔╗╔╔╦╗╔═╗╔╦╗  ╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═
╠╦╝╠═╣║║║ ║║║ ║║║║  ║  ╠═╣ ║   ╠═╣ ║  ║ ╠═╣║  ╠╩╗
╩╚═╩ ╩╝╚╝═╩╝╚═╝╩ ╩  ╚═╝╩ ╩ ╩   ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩
""")

mins = timer / 60
print(Colour.White + 'Attacking every {}'.format(int(mins)),
      'minutes\n\nPress Ctrl + C to exit\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

d = time.strftime('%a %H:%M:%S')


def cat():
    twt = api.search(q=search, count=count, lang='en', result_type='recent')
    for s in twt:
        try:
            urllib.request.urlretrieve(
                'http://thecatapi.com/api/images/get?format=xml&size=full&category=funny&type=gif&results_per_page=1', 'data/cat.xml')

            with open('data/cat.xml') as fd:
                doc = xmltodict.parse(fd.read())

            yey = doc['response']['data']['images']['image']['url']

            with open('data/cat.gif', 'wb') as f:
                f.write(requests.get(yey).content)

            sn = s.user.screen_name

            if not s.user.following:
                s.user.follow()
                print(Colour.Green + d, '- Following: @' + sn)
                time.sleep(2)
            else:
                print(Colour.Red + d, '- Already following: @' + sn)
                time.sleep(2)

            m = '@%s Random cat attack! x' % (sn)
            picci = ('data/cat.gif')
            api.update_with_media(picci, m, s.id)
            print(Colour.Green + d, '- Tweeting:', m)
            time.sleep(5)
        except KeyboardInterrupt:
            print(Colour.White + '\nExiting\n')
            sys.exit(1)
        except:
            print(Colour.Red + d, '- FAIL')
            time.sleep(10)


while True:
    cat()
    time.sleep(timer)

    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

