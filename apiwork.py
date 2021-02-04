import os
import requests
import spotipy
import random
import song
from dotenv import load_dotenv, find_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv(find_dotenv())
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
spotify_auth_manager = spotipy.SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET
)

def _get_top_songs():
    '''
    Fetches top songs from artists from spotify
    
    :global spotify_auth_manager: Authentication manager for Spotify
    :return: Json of an artist's top pieces
    :rtype: json object
    '''
    global spotify_auth_manager
    # kanye, rick roll, random
    artist_ids = ['5K4W6rqBFWDnAN6FQUkS6x', '0gxyHStUsqpMadRV0Di1Qt', ]
    choice = random.randint(0, len(artist_ids) - 1)
    
    req_url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_ids[choice])
    req_params = {
        'market' : 'US'
    }
    req_header = {
        'Authorization' : 'Bearer {}'.format(spotify_auth_manager.get_access_token())
    }
    
    response = requests.get(
        url=req_url,
        params=req_params,
        headers=req_header
    )
    return response.json()


def top_songs():
    """
    Gets the top songs from one of 3 artists
    
    :return: list of :class: Song for an artist
    :rtype: List -> song.Song
    """
    json_data = _get_top_songs()
    readable_top_songs = []
    
    for i in range (len(json_data['tracks'])):
        name = json_data['tracks'][i]['artists'][0]['name']         # artist name
        title = json_data['tracks'][i]['name']                      # track name
        preview = json_data['tracks'][i]['preview_url']             # preview url 
        image = json_data['tracks'][i]['album']['images'][0]['url'] # image
        
        the_song = song.Song(title, name, image, preview)
        readable_top_songs.append(the_song)
    
    return readable_top_songs