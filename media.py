import webbrowser

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_story, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def runTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
