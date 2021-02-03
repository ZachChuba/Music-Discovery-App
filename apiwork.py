import os
import requests
import spotipy
import random
from dotenv import load_dotenv, find_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv(find_dotenv())
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
spotify_auth_manager = spotipy.SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET
)

def get_top_song(auth_manager):
    '''
    Dynamically retrieves data on top songs from a random artist
    
    :param auth_manager: Authentication manager for Spotify
    :return: Json of an artist's top pieces
    :rtype: json object
    '''
    # kanye, random, random
    artist_ids = ['5K4W6rqBFWDnAN6FQUkS6x', ]
    choice = random.randint(0, len(artist_ids) - 1)
    
    req_url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_ids[choice])
    req_params = {
        'market' : 'US'
    }
    req_header = {
        'Authorization' : 'Bearer {}'.format(auth_manager.get_access_token())
    }
    
    response = requests.get(
        url=req_url,
        params=req_params,
        headers=req_header
    )
    return response.json()