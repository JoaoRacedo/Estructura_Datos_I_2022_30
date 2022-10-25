class Node_album:
    def __init__(self, value, next_node_album = None, prev_node_album = None):
        self.album_name = value[0]
        self.album_uri = value[1]
        self.next_album = next_node_album
        self.prev_album = prev_node_album
        self.head_node_track = value[2] # First attempt

    def __str__(self):
        return str(self.album_name)

class Node_album:
    def __init__(self, album_name, album_uri, album_tracks , next_node_album = None, \
        prev_node_album = None):
        self.album_name = album_name
        self.album_uri = album_uri
        self.next_album = next_node_album
        self.prev_album = prev_node_album
        self.head_node_track = LinkedList_track(album_tracks)

    def __str__(self):
        return str(self.album_name)

class LinkedList_album:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes_album(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_album
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_album
            
    @property
    def values(self):
        return [node for node in self]
    
    # if just albums is needed
    # value is list with name and uri of album
    # if all data is neededd
    # value is dict with "album_uri" and "track_list" sub keys and album name as key
    
    def add_node_album(self, album_name, album_uri, album_tracks):
        #if self.head is None:
        #    self.tail = self.head = Node_album(value)
        #else:
        #    self.tail.next_album = Node_album(value)
        #    self.tail = self.tail.next_album
        #return self.tail
        if self.head is None:
            self.tail = self.head = Node_album(album_name, album_uri, album_tracks)
        else:
            self.tail.next_album = Node_album(album_name, album_uri, album_tracks)
            self.tail = self.tail.next_album
        return self.tail

    def add_multiple_nodes_album(self, values):
        #    for value in values:
        #        self.add_node_album(value)
        for value_album in values:
            self.add_node_album(album_name = value_album, \
            album_uri = values[value_album]["album_uri"], \
            album_tracks = values[value_album]["track_list"])


class Node_track:
    def __init__(self, track_name, track_uri, track_is_explicit, next_node_track = None, prev_node_track = None):
        self.track_uri = track_uri
        self.track_is_explicit = track_is_explicit
        self.track_name = track_name
        self.next_track = next_node_track
        self.prev_track = prev_node_track

    def __str__(self):
        return str(self.track_name)

class LinkedList_track:
    def __init__(self, values = None):
        self.head_track = None
        self.tail_track = None
        if values is not None:
            self.add_multiple_nodes_track(values)
    
    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def add_node_track(self, track_name, track_uri, track_is_explicit):
        if self.head_track is None:
            self.tail_track = self.head_track = Node_track(track_name, track_uri, track_is_explicit)
        else:
            self.tail_track.next_track = Node_track(track_name, track_uri, track_is_explicit)
            self.tail_track = self.tail_track.next_track
        return self.tail_track

    # values is dict with "album_uri" and "track_list" sub keys and album name as key
    def add_multiple_nodes_track(self, values):
        for value_track in values:
            self.add_node_track(track_name = value_track["name"], \
                track_uri = value_track["uri"], \
                track_is_explicit = value_track["explicit"])
    
    def __len__(self):
        count = 0
        node = self.head_track
        while node:
            count += 1
            node = node.next_track
        return count
    
    def __iter__(self):
        current = self.head_track
        while current:
            yield current
            current = current.next_track
            

