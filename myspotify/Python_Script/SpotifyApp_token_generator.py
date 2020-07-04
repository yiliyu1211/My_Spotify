#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:28:12 2020

@author: teddy
"""


import spotipy.util as util

username = 'your user name' 
# your username (find in Spotify account)

client_id ='your client id' 
client_secret = 'your client secret' 
# client id and client secret (find in Spotify app account)

redirect_uri = 'http://localhost:7777/callback'
# redirect by local host

scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)

print(token)
