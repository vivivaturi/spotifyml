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
        client_credentials_manager = SpotifyClientCredentials(client_id=self.id, client_secret=self.secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        self.playlist = playlist
        self.dataframe = dataframe

        scope = 'user-library-read playlist-read-private'
        token = util.prompt_for_user_token(username, scope)

        if token:
            self.sp = spotipy.Spotify(auth=token)
        else:
            print("Can't get token for", username)


    def movePlaylist(self, source_user, source_playlist, target_user, target_playlist):
        """
        Gets the playlist that will be analyzed and moves it into another playlist
        for analysis. This method is much easier than the other getplaylistold method
        """
        sourcePlaylist = sp.user_playlist(source_user, playlist)
        trackList = sourcePlaylist["tracks"]
        songList = trackList["items"]
        while trackList['next']:
            for item in trackList["items"]:
                songList.append(item)

        ids = []
        for i in range(len(songs)):
            sp.user_playlist_add_tracks(target_user, target_playlist, [songList[i]["track"]["id"]])


    def getPlaylistSongId(self, user, playlist):
        trackList = playlist["tracks"]
        songList = tracks["items"]
        while trackList["next"]:
            trackList = sp.next(trackList)
            for item in trackList["items"]:
                songList.append(item)
        songId = []
        for i in range(len(songList)):
            songId.append(songList[i]["track"]["id"])

    def getAudioFeatures(self, songId):
        audioFeatures = []
        # Can only get upto 50 songs at once, so this is a workaround
        for i in range(0, len(songId), 50):
            features = sp.audio_features(good_ids[i:i+50])
            for track in features:
                audioFeatures.append(track)
                audioFeatures[-1]["target"] = 1


    def trainData(self, audioFeatures):
        trainData = pd.DataFrame(features)
        trainData.head()


    """
    Old playlist method. Slow and overly complicated.

    def getplaylistold(self, playlist):
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
    """
