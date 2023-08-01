class Song:

    count = 0
    genres = []
    genre_count = {}
    artist_count = {}
    artists = []

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        Song.add_to_artists(artist)


    
    @classmethod
    def add_song_to_count(cls,increment = 1):
        cls.count += increment
    
    @classmethod
    def add_to_genres(cls,genre):
        if genre in Song.genres:
            return
        else:
            return cls.genres.append(genre)
        
    @classmethod
    def add_to_genre_count(cls,genre):
        if cls.genre_count.get(genre) == None:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1


    @classmethod
    def add_to_artist_count(cls,artist):
        if cls.artist_count.get(artist) == None:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
        
    @classmethod
    def add_to_artists(cls,artist):
        if artist in Song.artists:
            return
        else:
            cls.artists.append(artist)

    
        


       
    
