import sys
import tweepy
import random
import time
from functions import *
from config import *


# Add some pretty colours for good measure
class Colour:
    Green, Red, Purple, White, Yellow = '\033[92m', '\033[91m', '\033[95m', '\033[0m', '\033[93m'

# Title (http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=WATTO)
print(Colour.Yellow + """
╦ ╦╔═╗╔╦╗╔╦╗╔═╗
║║║╠═╣ ║  ║ ║ ║
╚╩╝╩ ╩ ╩  ╩ ╚═╝
""")

print(Colour.White + 'Checking every {}'.format(int(sleep_timer)),
      'seconds\n\nPress Ctrl + C to exit\n')


def main():
    # Twatter authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Get new DM
    new_messages = api.direct_messages(count=1)

    # Get previous DM message text
    old_messages = api.sent_direct_messages(count=1)
    for message in old_messages:
        old = message.text

    # Get new DM sender id
    for message in new_messages:
        # print(message)
        new = message.sender_id_str
        sn = message.sender_screen_name
        searchtext = message.text
        wiki = search(searchtext)

        if not old == wiki:
            api.send_direct_message(new, text=wiki)
            print(Colour.Green + '\rMessage sent', end='')

            # Random cat attack
            if cat_attack:
                poob = random.randint(1, cat_attack_chance)
                noob = random.randint(1, cat_attack_chance)
                if noob == poob:
                    print(Colour.Green + '\rRandom cat attack', end='')
                    cat()
                    m = '@%s Random cat attack! x' % (sn)
                    picci = ('data/cat.gif')
                    api.update_with_media(picci, m, new)

        else:
            print(Colour.Purple + '\rNothing new', end='')

# Main loop
try:
    while True:
        main()
        time.sleep(sleep_timer)
except Exception as e:
    print(Colour.Red + str(e))

# Exit notice on ctrl+c
except KeyboardInterrupt:
    print(Colour.White + '\nExiting\n')
    sys.exit()
