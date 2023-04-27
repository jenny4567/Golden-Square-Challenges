class TrackList():
    def __init__(self):
        self.tracks = {}
    def add(self, song, artist):
        if (type(song) != str) or (type(artist) != str):
            raise Exception("Input must be strings.")
        if song in self.tracks.keys():
            raise Exception("Song already added.")
        
        self.tracks[song] = artist
    def list_all(self):
        return self.tracks
    def track_count(self):
        return len(self.tracks.keys())