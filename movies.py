movie_collection = [
    ('burning', 'lee chan dong', 2019),
    ('past lives', 'celine song', 2023),
    ('her', 'spike jonze', 2013)
]

def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f'Movie {title} by {director} added to collection.')

def display_movies():
    print("Movie collection")
    for title, director, year in movie_collection:
        print(f'Title: {title}, Director: {director}, Year: {year}')

def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

add_movie('lost in translation', 'sofia copolla', 1998)
display_movies()

movies_by_copolla = search_by_director('sofia copolla')

print("Movies by sofia copolla:")
for title, director, year in movies_by_copolla:
    print(f'Title: {title}, year: {year}')