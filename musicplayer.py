import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio):
        self.audio_files.append(audio)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class User:
    def __init__(self, name):
        self.name = name

# Create sample users
users = [User("User1"), User("User2"), User("User3")]

# Create sample audio files
audio1 = Audio("Song1", "http://example.com/song1.mp3")
audio2 = Audio("Song2", "http://example.com/song2.mp3")
audio3 = Audio("Song3", "http://example.com/song3.mp3")

playlist1 = Playlist("Playlist1", "Pop")
playlist2 = Playlist("Playlist2", "Rock")
playlist3 = Playlist("Playlist3", "Jazz")

playlist1.add_audio(audio1)
playlist2.add_audio(audio2)
playlist3.add_audio(audio3)

for playlist in [playlist1, playlist2, playlist3]:
    for user in users:
        rating = random.randint(1, 5)
        playlist.add_rating(rating)
        for audio in playlist.audio_files:
            audio.add_rating(rating)

for playlist in [playlist1, playlist2, playlist3]:
    print(f"{playlist.name} Average Rating: {playlist.average_rating()}")

    for audio in playlist.audio_files:
        print(f"   {audio.name} Average Rating: {audio.average_rating()}")