# Start of the quiz game
print("Welcome to my computer quiz!")

# Ask the player if they want to play
playing = input("Do you want to play? (yes/no): ")

# If the player doesn't enter "yes", the game ends
if playing.lower() != "yes":
    print("Goodbye!")
    quit()  # Exit the program

# Game starts if the player chooses to play
print("Okay! Let's play :)")
score = 0  # Variable to keep track of the score
total_questions = 3  # Total number of questions in the quiz

# First question about CPU
answer = input("What does CPU stand for? : ")
if answer.lower() == "central processing unit":  # Check if the answer is correct
    print("Correct!")
    score += 1  # Increment the score if the answer is correct
else:
    print("Incorrect.")

# Second question about GPU
answer = input("What does GPU stand for? : ")
if answer.lower() == "graphics processing unit":  # Correct answer: "graphics processing unit"
    print("Correct!")
    score += 1  # Increment the score for a correct answer
else:
    print("Incorrect.")

# Third question about RAM
answer = input("What does RAM stand for? : ")
if answer.lower() == "random access memory":  # Check if the answer is correct
    print("Correct!")
    score += 1  # Increment the score if the answer is correct
else:
    print("Incorrect.")

# Final output showing the player's score
print(f"You got {score}/{total_questions} questions correct.")
print(f"Your score is: {round((score / total_questions) * 100, 2)}%.")  # Show percentage score
