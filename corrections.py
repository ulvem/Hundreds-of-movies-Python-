
from data import movies
import json

# Function to update movie plot
def update_movie_plot(movie_id, plot):
    for movie in movies:
        if movie['id'] == movie_id:
            movie['plot'] = plot
            return True
    return False

# Update plots for specified movies
updates = [
    (1, "A recently deceased couple become ghosts and enlist the help of a mischievous bio-exorcist named Beetlejuice to remove the new inhabitants of their former home."),
    (22, "A skilled thief with the rare ability to 'extract' people's dreams enters the subconscious of a CEO to plant an idea, but the mission is complicated by the target's own mental defenses and the thief's personal demons."),
    (52, "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."),
    (53, "Two girlfriends on a summer holiday in Spain become enamored with the same painter, unaware that his ex-wife, with whom he has a tempestuous relationship, is about to re-enter the picture.")
]

for movie_id, plot in updates:
    if update_movie_plot(movie_id, plot):
        print(f"Updated plot for movie with id: {movie_id}")
    else:
        print(f"Movie with id: {movie_id} not found")

# Print updated movie information for verification
for movie in movies:
    if movie['id'] in [1, 22, 52, 53]:
        print(f"\nUpdated information for '{movie['title']}' (ID: {movie['id']}):")
        print(f"Plot: {movie['plot']}")

# Save the updated movies data back to the file
with open('data.py', 'w') as f:
    f.write("movies = ")
    json.dump(movies, f, indent=4)
    f.write("\n")

print("\nUpdated movie data has been saved to data.py")

# Function to update movie release year
def update_movie_year(movie_id, correct_year):
    for movie in movies:
        if movie['id'] == movie_id:
            print(f"Updating '{movie['title']}' - Old year: {movie['year']}, New year: {correct_year}")
            movie['year'] = correct_year
            return True
    return False

# Update release years for specified movies
updates = [
    (18, 2000),  # The Beach
    (27, 1999),  # American Beauty
    (54, 2008),  # Slumdog Millionaire
    (81, 2008),  # WALL-E
]

for movie_id, correct_year in updates:
    if update_movie_year(movie_id, correct_year):
        print(f"Updated release year for movie with id: {movie_id}")
    else:
        print(f"Movie with id: {movie_id} not found")

# Print updated movie information for verification
print("\nUpdated movie information:")
for movie in movies:
    if movie['id'] in [18, 27, 54, 81]:
        print(f"'{movie['title']}' (ID: {movie['id']}) - Release Year: {movie['year']}")

# Save the updated movies data back to the file
with open('data.py', 'w') as f:
    f.write("movies = ")
    json.dump(movies, f, indent=4)
    f.write("\n")

print("\nUpdated movie data has been saved to data.py")

# Adding Missing Directors and Saving Data

def update_movie_actor(movie_id, actor_index, actor_name):
    for movie in movies:
        if movie['id'] == movie_id:
            if 0 <= actor_index < len(movie['actors']):
                print(f"Updating '{movie['title']}' - Old actor: {movie['actors'][actor_index]}, New actor: {actor_name}")
                movie['actors'][actor_index] = actor_name
                return True
            elif actor_index == len(movie['actors']):
                print(f"Appending to '{movie['title']}' - New actor: {actor_name}")
                movie['actors'].append(actor_name)
                return True
    return False

# Update actor names for specified movies
updates = [
    (3, 0, "Tim Robbins"),  # The Shawshank Redemption, first actor
    (13, -1, "Josh Brolin"),  # No Country for Old Men, last actor
    (35, 0, "Leonardo DiCaprio"),  # Shutter Island, first actor
    (66, 1, "Thomas Kretschmann")  # The Pianist, second actor
]

for movie_id, actor_index, actor_name in updates:
    if update_movie_actor(movie_id, actor_index, actor_name):
        print(f"Updated actor for movie with id: {movie_id}")
    else:
        print(f"Failed to update actor for movie with id: {movie_id}")

# Print updated movie information for verification
print("\nUpdated movie information:")
for movie in movies:
    if movie['id'] in [3, 13, 35, 66]:
        print(f"'{movie['title']}' (ID: {movie['id']}) - Actors: {', '.join(movie['actors'])}")

# Save the updated movies data back to the file
with open('data.py', 'w') as f:
    f.write("movies = ")
    json.dump(movies, f, indent=4)
    f.write("\n")

print("\nUpdated movie data has been saved to data.py")

def add_director(movie_id, director_name):
    for movie in movies:
        if movie['id'] == movie_id:
            if 'director' not in movie:
                movie['director'] = director_name
                print(f"Added director for '{movie['title']}': {director_name}")
            else:
                print(f"'{movie['title']}' already has a director: {movie['director']}")
            return True
    return False

# Add directors for specified movies
updates = [
    (8, "Christopher Nolan"),  # Memento
    (31, "Guy Ritchie"),  # Lock, Stock and Two Smoking Barrels
    (38, "Woody Allen"),  # Midnight in Paris
    (64, "Bobcat Goldthwait"),  # God Bless America
    (82, "Martin Scorsese")  # The Wolf of Wall Street
]

for movie_id, director_name in updates:
    if add_director(movie_id, director_name):
        print(f"Updated director for movie with id: {movie_id}")
    else:
        print(f"Movie with id: {movie_id} not found")

# Print updated movie information for verification
print("\nUpdated movie information:")
for movie in movies:
    if movie['id'] in [8, 31, 38, 64, 82]:
        print(f"'{movie['title']}' (ID: {movie['id']}) - Director: {movie.get('director', 'Not added')}")

# Save the updated movies data back to the file
with open('data.py', 'w') as f:
    f.write("movies = ")
    json.dump(movies, f, indent=4)
    f.write("\n")

print("\nUpdated movie data has been saved to data.py")

# Define the corrections as a list of dictionaries
corrections = [
    {
        "id": 96,
        "genres": ["Action", "Comedy", "Crime", "Mystery", "Thriller"]
    },
    {
        "id": 146,
        "genres": ["Biography", "Comedy", "Drama"]
    }
]

# Function to apply corrections to the original movies list
def apply_corrections(movies, corrections):
    for correction in corrections:
        for movie in movies:
            if movie["id"] == correction["id"]:
                movie.update(correction)
                break

# Example usage
if __name__ == "__main__":
    # Example original movies list
    movies = [
        {"id": 96, "title": "Kiss Kiss Bang Bang"},
        {"id": 146, "title": "The Big Short"},
        # Other movies...
    ]

    # Apply corrections
    apply_corrections(movies, corrections)

    # Print updated movies list
    for movie in movies:
        print(movie)
        
# Define the corrections as a list of dictionaries
corrections = [
    {
        "id": 96,
        "genres": ["Action", "Comedy", "Crime", "Mystery", "Thriller"]
    },
    {
        "id": 146,
        "genres": ["Biography", "Comedy", "Drama"]
    },
    {
        "id": 90,
        "title": "V for Vendetta",
        "genres": ["Action", "Drama", "Sci-Fi", "Thriller"],
        "release_year": 2005,
        "director": "James McTeigue",
        "cast": ["Hugo Weaving", "Natalie Portman", "Rupert Graves", "Stephen Rea"]
    }
]

# Function to apply corrections to the original movies list
def apply_corrections(movies, corrections):
    for correction in corrections:
        for movie in movies:
            if movie["id"] == correction["id"]:
                movie.update(correction)
                break
        else:
            # If the movie is not found, add it to the list
            movies.append(correction)

    # Sort the movies list by id
    movies.sort(key=lambda x: x["id"])

# Example usage
if __name__ == "__main__":
    # Example original movies list
    movies = [
        {"id": 85, "title": "Oblivion"},
        {"id": 95, "title": "Gattaca"},
        {"id": 96, "title": "Kiss Kiss Bang Bang"},
        {"id": 146, "title": "The Big Short"},
        # Other movies...
    ]

    # Apply corrections
    apply_corrections(movies, corrections)

    # Print updated movies list
    for movie in movies:
        print(movie)

