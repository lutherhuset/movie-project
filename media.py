import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.story = movie_story
        self.poster = poster_image_url
        self.trailer = trailer_youtube_url

    def runTrailer(self):
        webbrowser.open(self.trailer)
