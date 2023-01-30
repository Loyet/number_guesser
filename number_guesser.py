import random

# Ask user to enter a number.
top_number = input("Type a number: ")

# Make sure entry is a valid number.
if top_number.isdigit():
    top_number = int(top_number)

    #If number is less than 0, tell the user so and exit the program.
    if top_number <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_number)

# Use loop to check the guess is valid and correct
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    #Make sure entry is a valid number.
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        # Add check to see if guess was too low or too high
        if user_guess > random_number:
            print("Your guess was above the number!")
        else:
            print("Your guess was below the number")

print(f"You got it in {guesses} guesses.")