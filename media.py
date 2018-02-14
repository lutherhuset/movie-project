import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story, poster_img, youtube_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster = poster_img
        self.trailer = youtube_trailer

    def runTrailer(self):
        webbrowser.open(self.trailer)
