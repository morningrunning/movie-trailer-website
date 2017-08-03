import fresh_tomatoes
import media


# MOVIES

# Instanciating movies information
movie_title = "Vanilla Sky"
movie_storyline = "Charged with murder, a young man recounts his story to a \
                   court appointed psychologist."
movie_image_url = "https://upload.wikimedia.org/wikipedia/en/9/9b/Vanilla_sky_post.jpg"  # noqa
movie_youtube_url = "https://www.youtube.com/watch?v=k09OX40NLUw"
date_on_theater = "12/14/2001"
duration = "136"
vanilla_sky = media.Movie(
            movie_title, duration, movie_storyline,
            movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "The Departed"
movie_storyline = "An undercover cop and a mole in the police attempt to \
                   identify each other while \
                   infiltrating an Irish gang in South Boston."
movie_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_.jpg"  # noqa
movie_youtube_url = "https://www.youtube.com/watch?v=iojhqm0JTW4"
date_on_theater = "10/06/2006"
duration = "151"
the_departed = media.Movie(
               movie_title, duration, movie_storyline,
               movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "The Words"
movie_storyline = "A writer at the peak of his literary success discovers the \
                   steep price he must pay for  \
                   stealing another man's work."
movie_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2NjgyMjI3OV5BMl5BanBnXkFtZTcwMDkxMjIyOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
movie_youtube_url = "https://www.youtube.com/watch?v=pMKB1LqwSHI"
date_on_theater = "09/07/2012"
duration = "102"
the_words = media.Movie(
                 movie_title, duration, movie_storyline,
                 movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "Casino Royale"
movie_storyline = "Armed with a license to kill, Secret Agent James Bond sets \
                   out on hisfirst mission as 007"
movie_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMDI5ZWJhOWItYTlhOC00YWNhLTlkNzctNDU5YTI1M2E1MWZhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_CR0,0,672,1000_AL_.jpg"  # noqa
movie_youtube_url = "https://www.youtube.com/watch?v=0quEnseH0zo"
date_on_theater = "11/17/2006"
duration = "144"
casino_royale = media.Movie(
                  movie_title, duration, movie_storyline,
                  movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "The Next Three Days"
movie_storyline = "A married couple's life is turned upside down when the \
                   wife is accused of a murder."
movie_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAzMjk4NjI4M15BMl5BanBnXkFtZTcwNjQ4OTEwNA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
movie_youtube_url = "https://www.youtube.com/watch?v=NBY0l7A2uLA"
date_on_theater = "11/19/2010"
duration = "133"
the_next_three_days = media.Movie(
                        movie_title, duration, movie_storyline,
                        movie_image_url, movie_youtube_url, date_on_theater)


# TV SHOWS

# Instanciating tv show information

title = "Wings"
storyline = "Brothers Brian and Joe Hackett attempt to run an airline on the \
             New England island of Nantucket while surrounded by \
             their various wacky friends and employees."
image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTEwMDQ3MzIxNjNeQTJeQWpwZ15BbWU3MDc1OTcyMzI@._V1_.jpg"  # noqa
youtube_url = "https://www.youtube.com/watch?v=ZdWMNe_B3ak"
duration = "30"
num_seasons = "7"
wings = media.TvShow(
               title, duration, storyline,
               image_url, youtube_url, num_seasons)

title = "The King of Queens"
storyline = "Delivery man Doug Heffernan has a good life: He's got a \
             pretty wife (Carrie), a big TV and friends to watch it with."
image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ3MDgyNTE4OV5BMl5BanBnXkFtZTcwMjU2ODA1MQ@@._V1_.jpg"  # noqa
youtube_url = "https://www.youtube.com/watch?v=i1pX0GhgjDs"
duration = "22"
num_seasons = "9"
king_of_queens = media.TvShow(
                  title, duration, storyline,
                  image_url, youtube_url, num_seasons)

title = "Dexter"
storyline = "By day, mild-mannered Dexter is a blood-splatter analyst for \
             the Miami police. But at night, he is a serial killer \
             who only targets other murderers."
image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_.jpg"  # noqa
youtube_url = "https://www.youtube.com/watch?v=YQeUmSD1c3g"
duration = "53"
num_seasons = "8"
dexter = media.TvShow(
         title, duration, storyline,
         image_url, youtube_url, num_seasons)

# movie varibale names stored in an array
movies_tvshow = [vanilla_sky, the_departed, the_words,
                 casino_royale, the_next_three_days,
                 wings, king_of_queens, dexter]
# running this function below will generate the fresh_tomatoes html file
fresh_tomatoes.open_movies_page(movies_tvshow)
