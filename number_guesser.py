import random

# Ask user to enter a number.
top_number = input("Type a number: ")

#Make sure entry is a valid number.
if top_number.isdigit():
    top_number = int(top_number)

    #If number is less than 0, tell the user so and exit the program.
    if top_number <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(-1, 11)
