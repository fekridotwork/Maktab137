from song import Song

class Album:
    def __init__(self, title, year, artist):
        self.title = title
        self.year = year
        self.artist = artist
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def remove_song(self, track_number):
        for song in self.songs:
            if song.track_number == track_number:
                self.songs.remove(song)
                break

    def total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration
        return total

    def show_songs(self):
        print(f"\nSongs in album '{self.title}':\n")
        for song in sorted(self.songs, key=lambda s: s.track_number):
            print(song.info())
            print("-" * 30)

    def __str__(self):
        return f"{self.title} ({self.year})"
