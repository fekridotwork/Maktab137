from album import Album

class Artist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.albums = []

    def add_album(self, album: Album):
        self.albums.append(album)

    def remove_album(self, title: str):
        for album in self.albums:
            if album.title == title:
                self.albums.remove(album)
                break

    def search_song(self, song_name):
        results = []
        for album in self.albums:
            for song in album.songs:
                if song.title.lower() == song_name.lower():
                    results.append((album.title, song))
        return results

    def show_all(self):
        print(f"\nArtist: {self.name}")

        for album in self.albums:
            print(f"\nAlbum: {album.title} ({album.year})")
            album.show_songs()
