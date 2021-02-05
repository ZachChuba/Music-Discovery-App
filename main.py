import song
import apiwork
import os
import random
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def app_runtime():
    # get list of songs and randomly select one
    selected_song = apiwork.get_song()
    lyrics = apiwork.get_song_lyrics(selected_song)
    song_attrs = selected_song.getAttrs()
    
    return render_template(
        "index.html",
        song_data = song_attrs,
        lyrics_url = lyrics
    )
    
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)