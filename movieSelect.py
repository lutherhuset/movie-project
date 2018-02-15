import fresh_tomatoes
import media

""" Class filled with instances of movie that will be called into the html webpage via the movie array below """

django = media.Movie("Django Unchained", "Former slave whoops ass.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=B9tF3KgEdAI")

frozen = media.Movie("Frozen", "Cold weather and talking snowmen.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=Zb5IH57SorQ")

gotg2 = media.Movie("Guardians of the Galaxy 2", "Cool space fights and a dope baby tree.",
                    "http://i.annihil.us/u/prod/marvel/html_pages_assets/gotg2-premiere/images/master_gotg2-b3de7b1c93.jpg",
                    "https://www.youtube.com/watch?v=z_p3OEpeviM")

logan = media.Movie("Logan", "Cool earth fights and Hugh Jackman.",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=v_SyrpYk-Ik")

jumanji = media.Movie("Jumanji", "Animal stampedes, Robin Williams,and two unlucky orphans play a board game.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Jumanji_poster.jpg/220px-Jumanji_poster.jpg",
                      "https://www.youtube.com/watch?v=_lUiJsnGXh8")

blade = media.Movie("Blade", "Bad ass never aging samarui vampire.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Blade_movie.jpg/220px-Blade_movie.jpg",
                    "https://www.youtube.com/watch?v=cI5RYgvPHLU")

movies = [django, frozen, gotg2, logan, jumanji, blade]
fresh_tomatoes.open_movies_page(movies)

# This class is the creation of
# several movies that use the init created in media.py
