###############################################################################
###               Stock Repo
###
### Facilitates Stock Repo program
###
### @file   main.py
### @author Justin Loi
###############################################################################

import requests
import json

def get_messages(channelid):
    headers = {
        # Key stored elsewhere
        'authorization': 'test'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    json_object = json.loads(r.text)
    for value in json_object:
        print(value, '\n')

# Key stored elsewhere
get_messages(test)
