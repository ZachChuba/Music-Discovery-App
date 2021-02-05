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

def call_spotify_api():
    '''
    Fetches top songs from artists from spotify
    
    :global spotify_auth_manager: Authentication manager for Spotify
    :return: Json of an artist's top pieces
    :rtype: json object
    '''
    global spotify_auth_manager
    
    # kanye, rick roll, random
    ARTIST_IDS = ['5K4W6rqBFWDnAN6FQUkS6x', '0gxyHStUsqpMadRV0Di1Qt', '7jVv8c5Fj3E9VhNjxT4snq']
    choice = random.randint(0, len(ARTIST_IDS) - 1)
    
    req_url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=ARTIST_IDS[choice])
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


def get_song():
    """
    Gets the top songs from one of 3 artists
    
    :return: list of :class: Song for an artist
    :rtype: List -> song.Song
    """
    json_data = call_spotify_api()
    readable_top_songs = []
    
    for i in range (len(json_data['tracks'])):
        name = json_data['tracks'][i]['artists'][0]['name']         # artist name
        title = json_data['tracks'][i]['name']                      # track name
        preview = json_data['tracks'][i]['preview_url']             # preview url 
        image = json_data['tracks'][i]['album']['images'][0]['url'] # image
        
        the_song = song.Song(title, name, image, preview)
        readable_top_songs.append(the_song)
    
    selected = readable_top_songs[random.randint(0, len(readable_top_songs) - 1)]
    return selected
    

def call_genius_api(artist_name, song_title):
    '''
    :param artist_name: string name of artist
    :param song_title: string song title
    :return: json containing the lyrics url
    :rtype: json
    '''
    
    REQ_URL = 'https://api.genius.com/search'
    search_query = '{} {}'.format(artist_name, song_title)
    req_params = {
        'q' : search_query
    }
    req_header = {
        'Authorization' : 'Bearer {}'.format(os.getenv('GENIUS_AUTH'))
    }
    
    response = requests.get(
        url=REQ_URL,
        params=req_params,
        headers=req_header
    )
    return response.json()
    
    
def get_song_lyrics(song):
    '''
    :param song: a song.Song
    :return: a link to the lyrics for a song
    :rtype: string
    '''
    
    title = song.getTitle()
    name = song.getName()
    
    lyrics_json = call_genius_api(name, title)
    
    return lyrics_json['response']['hits'][0]['result']['url']
