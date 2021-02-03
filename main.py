from flask import Flask, render_template
import apiwork
import os

app = Flask(__name__)
@app.route('/')

def app_runtime():
    # TODO
    fav_tv = ["Better Call Saul", "Breaking Bad", "Parks & Rec", "The Office", "Band of Brothers"]
    return render_template(
        "index.html",
        len = len(fav_tv),
        shows = fav_tv
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)