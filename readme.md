# Required Steps for Deployment
### Setup Spotify API
1. Create a spotify developer account here: https://developer.spotify.com/dashboard/login
2. Click create an app, fill out required fields.
3. You should now see a Client ID and Client Secret--you will need these later.

### Setup Genius API
1. Go to https://genius.com/api-clients, and create an account when prompted
2. Now click New API Client, and fill in all of the required fields (skip URI for now)
3. You should now see a screen with a Client ID, Client Secret, and Client Access Token
4. Click generate access token--you will need this shortly

### Create a .env file in the project's directory, then add this code to it (with your IDs):
```bash
export SPOTIPY_CLIENT_ID='YOUR_SPOTIFY_CLIENT_ID'
export SPOTIPY_CLIENT_SECRET='YOUR_SPOTIFY_CLIENT_SECRET'
export GENIUS_AUTH='GENIUS_ACCESS_TOKEN'
```

### Ensure you have the following libraries installed:
1. sudo pip install requests
2. sudo pip install spotipy
3. sudo pip install python-dotenv

Now, you have all dependencies needed to run this application. Cd into your project directory then run it with the command:
```bash
python main.py
```

# Known Issues / What I'd do in the future
Issue: No audio previews are available for most of the top songs from Kanye West. If I had more time, I'd link to the spotify song instead of saying no preview available.

Future Plan: I would add a drop-down menu to select an artist on the main page. Selecting one would reload the page with a new song from that artist. I would do this by adding a drop down box in the html, and by creating an event listener for an selection in javascript. The javascript would then pass the choice to the backend by using a new Flask route /select/\<artist\> and refresh the page with a new song from that artist.

# Problems I Experienced
1. An issue that I foresaw was that some implementations of getting the auth token for the spotify using requests.post could possibly break if a user sits on the page for too long. Looking at the spotify documentation, the authentication token has a Time to Live (TTL) attribute, which would expire the auth token after typically 5 minutes. So, despite using the requests framework for most of my api calls, I chose to use the spotipy library, which has a built in get_auth_token function that will automatically request a new token if it expires, for my authentication. Documentation is available here: https://spotipy.readthedocs.io/en/2.16.1/#module-spotipy.oauth2
2. The Genius API has a convoluted way of generating an access token for an application user [read about it here](https://docs.genius.com/#/authentication-h1 "Genius API"). I initially tried to implement this, but I realized that I was never redirecting a user, so that authentication flow wouldn't work. I later found out that access tokens do not expire, so I could just add the access token to my .env instead of trying to generate one every time the page is loaded.
3. I initially had difficulty loading a background image onto the page. I used [mozilla's css guide](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) to realize that the URL is relative to the current position of the style.css file. So, to access a file in the same folder as style.css, I'd still have to start the url with ../
4. There was a bug where refreshing the page would result in a key error. I tracked it back to the spotipy authentication logic using print statements every time I called the spotify api. Because I defined the auth manager in the global namespace, refreshing the page would not get a new authentication token, and consequently fail the spotify api call. I fixed this by moving the authenticator to the top_songs namespace.