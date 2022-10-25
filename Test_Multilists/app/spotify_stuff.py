import json
from typing import List
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify_Stuff:
    """
    A class to represent spotify API and interactions.
    
    ...

    Attributes
    ----------
    None

    Methods
    -------
    get_id(spotify_url : str =):
        Returns the spotify id given a spotify URL
    
    get_playlist_data_by_URL(play_list_URL : str =):
        Returns Spotify object with playlist data of tracks given a playlist URL
    
    get_artist_album_data_by_URL(artist_url : str =, album_type : str = "album",
        number_albums : int = 10):
        Returns list with albums data of artist given artirst URL, type of album
        (possibles choices are: "album", "single", "appears_on", "compilation") and number 
        of albums to get
    
    get_tracks_from_URI_album(albums_list : List) -> json:
        Returns json with tracks of each album that is in the album_list list
    """

    def __init__(self):
        """
        Constructs the spotify object given the credentials

        Parameters
        ----------
        None
        """
        client_credentials_manager = SpotifyClientCredentials(
            "SPOTIPY_CLIENT_ID", \
            "SPOTIPY_CLIENT_SECRET")
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_id(self, spotify_url : str = None):
        """
        Returns the spotify id given a spotify URL

        Parameters
        ----------
        spotify_url : str. If not provided an error is raise
            Spotify URL
        
        Returns
        -------
        Spotify ID of URL
        """
        if spotify_url is None:
            raise TypeError("URL needed")
        spotify_id = spotify_url.split("/")[-1].split("?")[0]
        return spotify_id
    
    def get_playlist_data_by_URL(self, play_list_URL : str = None):
        """
        Returns Spotify object with playlist data of tracks given a playlist URL

        Parameters
        ----------
            play_list_URL : str, optional. If not provided an example Spotify URL is passed
                Spotify playlist URL
        
        Returns
        -------
        Spotify object with playlist data of tracks
        """
        if play_list_URL is None:
            url_playlist = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1XumoU?si=7844dc2d2bc14ed0"
            id_playlist = self.get_id(url_playlist)
        else:
            id_playlist = self.get_id(play_list_URL)\

        results = self.spotify.playlist_tracks(id_playlist)
        return results
    
    def get_artist_album_data_by_URL(self, artist_url : str = None, album_type : str = "album", \
        number_albums : int = 10):
        """
        Returns list with albums data of artist given artirst URL

        Parameters
        ----------
        artist_url : str. If not provided an error is raise
            Spotify artist URL
        album_type : str = "album".
            Type of data to be retrieved
            Possibles choices are: "album", "single", "appears_on", "compilation"
        number_albums : int = 10. optional
            Number of albums

        Returns
        -------
        Returns list with albums name and URI
        """
        if artist_url is None:
            raise TypeError("artist album url needed")
        else:
            artist_id = self.get_id(artist_url)
        
        results = self.spotify.artist_albums(artist_id, album_type = album_type)
        albums = results['items']
        result_list = []
        for album in albums[:number_albums]:
            result_list.append([album["name"], album["uri"]])
        
        return result_list
    
    def get_tracks_from_URI_album(self, albums_list : List):
        """
        Returns json with tracks of each album that is in the album_list list

        Parameters
        ----------
        albums_list : List.
            list with album name and URI ID
        
        Returns
        -------
        Returns json with tracks of each album that is in the album_list list
        """
        albums_data = {}
        for album in albums_list:
            tracks = self.spotify.album_tracks(album[1])
            track_list = []
            for track in tracks["items"][:10]:
                single_track = {}
                single_track["uri"] = track["uri"]
                single_track["explicit"] = track["explicit"]
                single_track["name"] = track["name"]
                track_list.append(single_track)
            albums_data[album[0]] = {"album_uri" : album[1], "track_list" : track_list}
        return albums_data


    


