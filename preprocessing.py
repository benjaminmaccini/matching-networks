# Collects and vectorizes songs from Spotify
import requests
from requests.auth import HTTPBasicAuth
import sys, os
import argparse
import numpy as np
from pprint import pprint

import pdb

'''
  Features (12):
  	id
	acousticness
	danceability
	energy
	instrumentalness
	key
	liveness
	loudness
	mode
	speechiness
	tempo
	time_signature
	valence
'''

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

ACCESS_TOKEN = ''
TOKEN_HEADER = {}

def spotify_auth():
	payload = {'grant_type':'client_credentials'}
	r = requests.post('https://accounts.spotify.com/api/token', data=payload,
									 auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
	print("Token {}".format(r))
	ACCESS_TOKEN = r.json()['access_token']
	TOKEN_HEADER = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}
	print("Successfully retrieved token:")
	pprint(r.json())
	print('\n~\n~\n~')

def create_map():
	# Utiliy script to compile all the genres and map them to prime numbers
	# This is an open TODO... is this even the correct method to use???
	pass

def get_artist_genre(song_id):
	r = requests.get("https://api.spotify.com/v1/artists/{}".format(song_id), headers=TOKEN_HEADER)
	data = r.json()['genres'] # List of Strings
	name = r.json()['name']
	return data, name

def get_song(song_id):
	r = requests.get("https://api.spotify.com/v1/audio-features/{}".format(song_id), headers=TOKEN_HEADER)
	print("{} for song_id {}".format(r,song_id))
	data = r.json()
	return data

def collect(song_ids):
	json_list = []
	return json_list

def vectorize(json_list):
	song_features = np.zeros(12,1)
	return song_features

def get_id_from_uri(uri):
	return uri.strip().split(':')[-1]

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--list', dest='collection', action='append', default=[], help='A list of Spotify uris or song ids')
	parser.add_argument('--id', dest='id', default='foo')
	parser.add_argument('--auth_test', dest='auth', action='store_true')
	parser.add_argument('--create_map', dest='create_map', action='store_true')
	parser.set_defaults(auth=False, create_map=False)

	return parser.parse_args()


if __name__ == '__main__':
	args = parse_args()
	try:
		spotify_auth()
	except Exception as e:
		pprint(e)
		sys.exit()

	if(args.create_map):
		artist_ids = [0,1,2,3,4]
		create_map()
	elif(args.collection != []):
		json_list = collect(args.collection)
		song_features = vectorize(json_list)
		pprint(song_features)
	elif(args.id != 'foo'):
		pprint(get_song(args.id))