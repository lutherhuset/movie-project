import webbrowser

"""This file defines the Video and Movie classes.
For Video we just use the init to obtain a movie title and
for the Movie class, init and runTrailer methods
are used to store movie info and run trailers when called

Note:
    Video is not called directly in movieSelect.py.
    Movie is called which then uses the Video class to
    inherit the movie title.
"""

# added in this Video class to utilize
# inheritance even though it isn't really necessary.


class Video():
    """
        Args:
            self.title

        Attributes:
            movie_title

        Methods:
            Video init: store title information
    """
    def __init__(self, movie_title):
        self.title = movie_title

#  Movie is the class we use to store the movie data for our website
# also has a method for playing movie trailers called runTrailer


class Movie(Video):
    """
        Args:
            self.story
            self.poster
            self.trailer

        Attributes:
            movie_story
            poster_image_url
            trailer_youtube_url

        Methods:
            Movie init: store other movie info
            Movie runTrailer: runs trailer using the trailer URL
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # optional functionality for movie ratings--not currently used

    def __init__(self, movie_title, movie_story, poster, trailer):
            Video.__init__(self, movie_title)
            # movie is a child class of video and gets the title from video
            self.story = movie_story
            self.poster = poster_image_url
            self.trailer = trailer_youtube_url

    # used to run the movie trailer when called using webbrowser.open
    def runTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
