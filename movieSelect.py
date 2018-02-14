import media

django = media.Movie("Django Unchained", "Dr. Schultz explains that he feels responsible for Django since Django is the first person he has ever freed, and feels morally obliged to help Django reunite with Broomhilda.", "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg", "https://www.youtube.com/watch?v=eUdM9vrCbow" )
print(django.title)
django.runTrailer()