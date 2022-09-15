# API credentials

# Client Id and Secret from Spotify API
CLIENT_ID = 'b3efc4982a5a4c7197f979d08087128d'
CLIENT_SECRET = '3cd6cc8bdf114d9a97be07ad12024683'

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# URL for authorisation
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Track features
track_features_list = ['name', 'popularity']

artist_features_list = ['genres', 'popularity']

audio_features_list = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
                  'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

# ML model
model = 'my_model'

model_all = 'my_model_all'

# Scaler
scaler = 'scaler'

scaler_all = 'scaler_all'

# Decoding dictionary
genre_decode_dict = {1 : 'ambient',
                 2 : 'psytrance',
                 3 : 'dnb',
                 4 : 'hardstyle',
                 5 : 'trance',
                 6 : 'techno',
                 7 : 'techhouse',
                 8 : 'trap',
                 9 : 'synthwave'}

genre_decode_dict_all = {1 : 'blues',
                 2 : 'classical',
                 3 : 'country',
                 4 : 'disco',
                 5 : 'electronic',
                 6 : 'hiphop',
                 7 : 'metal',
                 8 : 'jazz',
                 9 : 'pop',
                 10: 'reggae',
                 11: 'rock',
                 12: 'latin'}
