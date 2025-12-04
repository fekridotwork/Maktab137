from artist import Artist
from album import Album
from song import Song

if __name__ == "__main__":

    artist = Artist("Hans Zimmer", "Soundtrack")

    album1 = Album("Interstellar", 2014, artist.name)
    album2 = Album("Inception", 2010, artist.name)

    artist.add_album(album1)
    artist.add_album(album2)

    album1.add_song(Song("Cornfield Chase", 120, "Soundtrack", 1))
    album1.add_song(Song("Stay", 240, "Soundtrack", 2))

    album2.add_song(Song("Time", 260, "Soundtrack", 1))
    album2.add_song(Song("Dream is Collapsing", 150, "Soundtrack", 2))

    artist.show_all()

    print("\nSearch results for 'time':")
    results = artist.search_song("time")
    for album_title, song in results:
        print(f"- Found in {album_title}: \n{song.info()}")

    print("\nTotal duration Interstellar:", album1.total_duration(), "seconds")
