from app.classes import LinkedList_album
from app.spotify_stuff import Spotify_Stuff
import pytest

@pytest.fixture
def Spotify_conection():
    spotify = Spotify_Stuff()
    url_data = "https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02?si=UxdHBE31RvOq-7FtFXVEyg"
    album_list = spotify.get_artist_album_data_by_URL(url_data)
    json_data = spotify.get_tracks_from_URI_album(album_list)
    return json_data

def test_first_album(Spotify_conection):
    albums_linked_list = LinkedList_album(Spotify_conection)
    assert albums_linked_list.head.album_name == "Midnights (3am Edition)"

def test_len_albums(Spotify_conection):
    albums_linked_list = LinkedList_album(Spotify_conection)
    assert len(albums_linked_list) == 6

def test_len_tracks(Spotify_conection):
    albums_linked_list = LinkedList_album(Spotify_conection)
    assert len(albums_linked_list.head.head_node_track) == 10
