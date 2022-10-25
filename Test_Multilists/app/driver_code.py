#from app.classes import LinkedList
from app.classes import LinkedList_album
from app.spotify_stuff import Spotify_Stuff

spotify = Spotify_Stuff()
url_data = "https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02?si=UxdHBE31RvOq-7FtFXVEyg"
album_list = spotify.get_artist_album_data_by_URL(url_data)
json_data = spotify.get_tracks_from_URI_album(album_list)
#print(json.dumps(json_data, indent=2))

### First attemp, we can improve!!
#lista_temp = []
#for data in json_data:
#    lista_album = []
#    lista_album.append(data)
#    lista_album.append(json_data[data]["album_uri"])
#    lista_album.append(json_data[data]["track_list"])
#    lista_temp.append(lista_album)
#albums_linked_list = LinkedList_album(lista_temp)
#print(albums_linked_list)


# Second attemp, better!!
albums_linked_list = LinkedList_album(json_data)
print(albums_linked_list)
print("first album:")
print(albums_linked_list.head)
print("how many tracks in this album:")
print(len(albums_linked_list.head.head_node_track))
print(albums_linked_list.head.head_node_track)