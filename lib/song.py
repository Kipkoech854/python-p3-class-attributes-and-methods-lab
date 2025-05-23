class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist  
        self._genre = genre    
        
        
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @property
    def name(self):
        return self._name

    @property
    def artist(self):
        return self._artist

    @property
    def genre(self):
        return self._genre

    
    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count