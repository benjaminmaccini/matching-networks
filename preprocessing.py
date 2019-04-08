# Collects and vectorizes songs from Spotify
import requests
from requests.auth import HTTPBasicAuth
import sys, os
import argparse
import numpy as np
from pprint import pprint

import pandas as pd

import pickle

import pdb

'''
  	python3 preprocessing.py --list songs.txt artists.txt
	
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

	timbre *** TODO see audio_analysis
'''
class Song:
	'''
		Song Data Layer
	'''

	def __init__(self):
		self.CLIENT_ID = os.environ['CLIENT_ID']
		self.CLIENT_SECRET = os.environ['CLIENT_SECRET']
		self.ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
		self.TOKEN_HEADER = {}

	def spotify_auth(self):
		payload = {'grant_type':'client_credentials'}
		r = requests.post('https://accounts.spotify.com/api/token', data=payload,
										 auth=HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET))
		print("Token {}".format(r))
		os.environ['ACCESS_TOKEN'] = r.json()['access_token']
		self.ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
		self.TOKEN_HEADER = {'Authorization': 'Bearer ' + self.ACCESS_TOKEN}
		print("Successfully retrieved token:")
		print(self.TOKEN_HEADER)

	def get_artist_genre(self, artist_id):
		r = requests.get("https://api.spotify.com/v1/artists/{}".format(artist_id), headers=self.TOKEN_HEADER)
		print("{} for artist_id {}".format(r,artist_id))
		data = r.json()['genres'] # List of Strings
		name = r.json()['name']
		return data, name

	def get_song(self, song_id):
		r = requests.get("https://api.spotify.com/v1/audio-features/{}".format(song_id), headers=self.TOKEN_HEADER)
		print("{} for song_id {}".format(r,song_id))
		data = r.json()
		return data

	def collect(self, song_ids, artist_ids):
		supp = []
		for song_id, artist_id in zip(song_ids, artist_ids):
			song_id = self.get_id(song_id)
			artist_id = self.get_id(artist_id)
			data = self.get_song(song_id)
			labels, metalabel = self.get_artist_genre(artist_id)
			temp = {metalabel:(labels,data)}
			supp.append(temp)
		return supp

	def audio_analysis(self, song_id):
		# This is a TODO because it requires a lot of extra work to vectorize
		r = requests.get("https://api.spotify.com/v1/audio-analysis/{}".format(song_id), headers=self.TOKEN_HEADER)
		print("{} for song_id {}".format(r,song_id))
		data = r.json()
		return data

	def vectorize(self, supp):
		song_features = np.zeros(12,1)
		song_features = pd.get_dummies(song_features)
		return song_features

	def get_id(self, uri):
		return uri.strip().split(':')[-1]

	def e2e(self):
		# Take in a text file and then create support set
		pass

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--list', dest='collection', default=[], nargs='+', help='A list of Spotify uris or song ids')
	parser.add_argument('--uri', dest='uri', default='foo')
	parser.add_argument('--auth_test', dest='auth', action='store_true')
	parser.set_defaults(auth=False, create_map=False)

	return parser.parse_args()


if __name__ == '__main__':
	s = Song()
	args = parse_args()
	try:
		s.spotify_auth()
	except Exception as e:
		pprint(e)
		sys.exit()
	if(not args.auth):
		if(args.collection != []):
			song_list = []
			with open(args.collection[0], 'r') as in_file:
				for line in in_file:
					song_list.append(line.strip())
			artist_list = []
			with open(args.collection[1], 'r') as in_file:
				for line in in_file:
					artist_list.append(line.strip())
			supp = s.collect(song_list, artist_list)
			# song_features = s.vectorize(supp)
			pprint(song_features)
		elif(args.uri != 'foo'):
			song_id = s.get_id(args.uri)
			pprint(s.get_song(song_id))
			# s.audio_analysis(song_id)
		else:
			print("Check args")