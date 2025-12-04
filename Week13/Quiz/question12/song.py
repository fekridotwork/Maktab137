class Song:
    def __init__(self, title, duration, genre, track_number):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.track_number = track_number

    def info(self):
        return (
            f"+ Track: {self.track_number}\n"
            f"+ Title: {self.title}\n"
            f"+ Genre: {self.genre}\n"
            f"+ Duration: {self.duration}s"
        )

