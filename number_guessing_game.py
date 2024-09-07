import random

number_of_guesses = 0


top_range = input('Pick a number: ')
if top_range.isdigit:
    top_range = int(top_range)
    
    if top_range < 0:
        print('Please enter a number above 0!')
        quit()
else:
    print('Please enter a number next time!')
    quit()
    
    
random_number = random.randint(0, top_range)

while True:
    number_of_guesses +=1
    player_guess = input('Guess a number between 0 and the number you picked: ')
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print('Please enter a number...')
        continue
        
    if player_guess == random_number:
        print('Congratulations! You guessed the correct number!')
        break
    elif player_guess > random_number:
            print("the correct number is lower")
    else:
        print('The correct number is higher')
    

print(f'You got it in {number_of_guesses} amount of guesses')