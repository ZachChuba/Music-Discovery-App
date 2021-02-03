#Required Steps for Deployment
1. Create a spotify developer account here: https://developer.spotify.com/dashboard/login
2. Click create an app, fill out required fields
3. Create a .env file in the project's directory, then add this code to it (with your IDs):
`export SPOTIPY_CLIENT_ID='YOUR_SPOTIFY_CLIENT_ID'
export SPOTIPY_CLIENT_SECRET='YOUR_SPOTIFY_CLIENT_SECRET'`

##Ensure you have the following libraries installed:
1. sudo pip install requests
2. sudo pip install spotipy
3. sudo pip install python-dotenv

#Known Issues
#Problems I Experienced
1. An issue that I foresaw was that some implementations of getting the auth token for the spotify using requests.post could possibly break if a user sits on the page for too long. Looking at the spotify documentation, the authentication token has a Time to Live (TTL) attribute, which would expire the auth token after typically 5 minutes. So, despite using the requests framework for most of my api calls, I chose to use the spotipy library, which has a built in get_auth_token function that will automatically request a new token if it expires, for my authentication. Documentation is available here: https://spotipy.readthedocs.io/en/2.16.1/#module-spotipy.oauth2