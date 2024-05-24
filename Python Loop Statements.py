# Q1 Task1

import random

# Create a list of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Loop through the days of the week
for day in range(7):
  # Get the day name based on the index (0 = Monday, 6 = Sunday)
  day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
  
  # Randomly select a mood from the list
  mood = random.choice(moods)

  # Print the result
  print(f"On {day_name}, you were feeling {mood}.")


# Q2 Task1

import random

# Create a list of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired"]

# List of times of the day
times = ["morning", "afternoon", "evening"]

# Loop through the days of the week
for day in range(7):
  # Get the day name based on the index (0 = Monday, 6 = Sunday)
  day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
  
  # Loop through the times of the day
  for time in times:
    # Randomly select a mood from the list
    mood = random.choice(moods)

    # Print the result
    print(f"On {day_name} {time} you were feeling {mood}.")

    # Q3 Task 1

# Initialize a counter variable
counter = 0

# Loop with a condition that's always true
while True:
  # Print a message
  print("Iteration", counter)

  # Increment counter
  counter += 1

  # Exit the loop after 5 iterations
  if counter == 5:
    break

# Q3 Task 2

# Initialize a counter variable
counter = 0

# Loop with a condition that becomes false
while counter < 5:
  # Print a message
  print("Iteration", counter)

  # Increment counter
  counter += 1

# Q4 Task 1

import random

# Define a list of items
items = ["apple", "banana", "orange", "grape"]

# Randomly select an item
chosen_item = random.choice(items)

# Get user's guess
guess = input("Guess the item! It's a fruit: ")

# Check if the guess is correct
if guess.lower() == chosen_item:
  print("You guessed correctly! ")
else:
  print(f"Sorry, the chosen item was {chosen_item}.")

# Q5 

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: for loop DJ Set
for index, genre in enumerate(genres):
  # Get the track number by adding 1 to the index (starts from 0)
  track_number = index + 1
  print(f"Track {track_number}: Now playing {genre}!")

# Task 2: The Remix Artist with while
# Initialize a counter and variable to store the stop genre
current_index = 0
stop_genre = "Hip-hop"

while current_index < len(genres) and genres[current_index] != stop_genre:
  # Get the track number
  track_number = current_index + 1
  print(f"Track {track_number}: Now playing {genres[current_index]}!")
  current_index += 1  # Increment counter

# Task 3: Light Show Technician Loop
for index in range(len(genres)):
  genre = genres[index]
  # Skip classical genre
  if genre.lower() != "classical":
    track_number = index + 1
    print(f"Track {track_number}: Light show ready for {genre}!")

# Q6

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: The Selective DJ
# Get a slice of genres from index 1 (second track) to index 3 (fourth track) excluding the fourth element
sublist_genres = genres[1:3]

print("Selected genres:")
for genre in sublist_genres:
  print(genre)

# Task 2: The One-Liner Band with List Comprehensions
# Create a new list using list comprehension
genres_with_music = [genre + " Music" for genre in genres]

print("Genres with 'Music' appended:")
print(genres_with_music)

# Task 3: Numerical Beats with range
for number in range(10, 0, -1):  # Countdown from 10 to 1
  print(number)

print("The beat drops now!")


