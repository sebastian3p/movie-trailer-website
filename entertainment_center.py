import fresh_tomatoes
#That module has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.hat module has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.
import media

# define instances of each movie with title, storyline, poster image and trailer
pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
#print(pulp_fiction.storyline)
big_hero = media.Movie("Big Hero 6",
                        "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                        "http://ia.media-imdb.com/images/M/MV5BMjI4MTIzODU2NV5BMl5BanBnXkFtZTgwMjE0NDAwMjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=rD5OA6sQ97M")
#big_hero.show_trailer()
matrix = media.Movie("The Matrix",
                    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                    "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
#matrix.show_trailer()
wolf = media.Movie("The Wolf of Wall Street",
                    "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
                    "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=iszwuX1AK6A")
#wolf.show_trailer()
avengers = media.Movie("The Avengers",
                    "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                    "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

big_trouble = media.Movie("Big Trouble in Little China",
                    "An All-American trucker gets dragged into a centuries-old mystical battle in Chinatown.",
                    "http://ia.media-imdb.com/images/M/MV5BMTk5MjI4MzIxMl5BMl5BanBnXkFtZTYwODU1MDQ5._V1_SY317_CR8,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=592EiTD2Hgo")

#create array movies to display on webpage
movies = [pulp_fiction, big_hero, matrix, wolf, avengers, big_trouble]
fresh_tomatoes.open_movies_page(movies)
