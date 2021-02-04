import song
import apiwork
import os
import random
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def app_runtime():
    # get list of songs and randomly select one
    songs = apiwork.top_songs()
    selected = songs[random.randint(0, len(songs) - 1)]
    song_attrs = selected.getAttrs()
    length = len(song_attrs) - 1 if song_attrs[3] is None else len(song_attrs)
    
    return render_template(
        "index.html",
        len = length,
        song_data = song_attrs
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)