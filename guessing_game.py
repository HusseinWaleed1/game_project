

# Solution

## Show the game levels
"""

def show_levels():
  print(''' Game Levels :
  (1) Easy:
      * Limits : [1 - 10]
      * No. of trials : 3
  (2) Intermediate*:
      * Limits : [1 - 100]
      * No. of trials : 7
  (3) Hard :
      * Limits : [1 - 1000]
      * No. of trials : 15 ''')

"""## Ask the user for the game level"""

def game_level_choice():
  while True:
      game_level = input('Enter the game level :\n (1) Easy \t (2) Intermediate \t (3) Hard \t')
      if game_level in ['1','2','3']:
          game_level = int(game_level)
          break
      else:
          print('Invalid Choice! Please choose 1, 2, or 3')
          continue
  return game_level

"""## Set the game settings according to the game level:

"""

def set_game_settings(game_level):
  if game_level == 1:
    limits = range(1,11)
    n_trials = 3
  elif game_level == 2:
    limits = range(1,101)
    n_trials = 7
  else:
    limits = range(1,1001)
    n_trials = 15
  return limits, n_trials

"""## Start Playing"""

import random

def start_play(limits, n_trials):
  hidden = random.choice(limits)
  user_trials = 0

  while user_trials < n_trials:
    guess = int(input('Guess the number :   '))
    user_trials +=1

    if guess == hidden:
      print(f'You got it successfully in {user_trials} trials')
      break
    else:
      if user_trials == n_trials:
        print(f"Unfortunately, You tried {user_trials} trials. No more Trials!")
        print(f'The hidden number is  {hidden}')
      elif guess < hidden:
        print('No, Increase!')
      else:
        print('No, Decrease!')
    continue

"""# Play Again ?"""

def play_again():
    while True:
      play_again = input("Play again ? [0] No, [1] Yes:   ")
      if play_again in ['1','0']:
          break
      else:
          print('Invalid Choice! Please choose 0 or 1   ')
    return int(play_again)

#

"""## Let's Play"""

def play():
  show_levels()
  while True:
    game_level = game_level_choice()
    limits, n_trials = set_game_settings(game_level)
    start_play(limits, n_trials)
    if not play_again():
        break

play()
play_again()

