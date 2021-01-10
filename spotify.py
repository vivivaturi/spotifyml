"""
Module for model that predicts which song I will like using ML
"""
import json
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

class spotibot:
    """
    Class that interfaces with the spotify API.

    This class will analayze a playlist to determine what songs will be liked
    using information gathered from the Spotify API. This will eventually interface
    with a discord bot.
    """

    def __init__(self, id, secret, playlist = None, dataframe = None):
        """
        Initializes ID
        """
        self.id = id
        self.secret = secret
        client_credentials_manager = SpotifyClientCredentials(self.id, self.secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        self.playlist = playlist
        self.dataframe = dataframe

    def getplaylist(self, playlist):
        """
        Gets playlist and converts to Dataframe
        """
        results = sp.playlist(playlist)

        songs = [] #list of songs

        for item in results['tracks']['items']:
            track = item['track']['id']
            songs.append(track)

        sp_list = {'id':[], 'album':[], 'name':[],'artist':[], 'popularity':[]}

        for song_id in songs:
            # Find the metadata from the song
            metadata = sp.track(song_id)

            # Add the metadata to the dict
            sp_list['id'].append(song_id) # ID
            sp_list['album'] += metadata['album']['name'] # Album
            sp_list['name'] += metadata['name'] # Name
            s = ', '
            artist = s.join([singer['name'] for signer in metadata['artists']])
            sp_list['artists'] += [artist] # Artist
            sp_list['popularity'].append(metadata['popularity'])

        self.dataframe = pd.Dataframe.from_dict(sp_list)
