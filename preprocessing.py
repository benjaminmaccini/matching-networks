# Collects and vectorizes songs from Spotify
import requests
import sys
import argparse
import numpy as np
from pprint import pprint

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
def get_song(uri):
	return r

def collect(songs):
	json_list = []
	return json_list

def vectorize(json_list):
	song_features = np.zeros(12,1)
	return song_features

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--list', dest='collection', action='append', default=[], help='A list of Spotify uris')
	parser.add_argument('--uri', dest='uri', default='not_a_uri')

	return parser.parse_args()


if __name__ == '__main__':
	args = parse_args()
	if(args.collection != []):
		json_list = collect(args.collection)
		song_features = vectorize(json_list)
		pprint(song_features)
	if(args.uri != 'not_a_uri'):
		pprint(get_song(args.uri))
