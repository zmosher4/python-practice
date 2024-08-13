favorite_movies = []
count = 0

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else: 
        print(f"Movie '{movie}' not found.")

def display_movies():
    print("Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    
    print(f"There are '{len(favorite_movies)}' movies in the list.")

def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie '{movie}' found.")
    else: 
        print(f"Movie '{movie}' not found.")

def clear_movies():
    favorite_movies.clear()
    print("List has been cleared")

add_movie("burning")
add_movie("past lives")
add_movie("whiplash")

count_movies()

remove_movie("past lives")

count_movies()
