# Game_project


## Description
A simple number guessing game where the player selects a difficulty level and tries to guess the hidden number within a limited number of attempts.

## Game Levels
- **Easy:**  
  - Limits: [1 - 10]  
  - Number of trials: 3  

- **Intermediate:**  
  - Limits: [1 - 100]  
  - Number of trials: 7  

- **Hard:**  
  - Limits: [1 - 1000]  
  - Number of trials: 15  

## How to Play
1. Run the game.
2. Choose a game level:  
   - Enter `1` for Easy  
   - Enter `2` for Intermediate  
   - Enter `3` for Hard  
3. Guess the hidden number within the allowed attempts.
4. If your guess is wrong, you'll get a hint to guess higher or lower.
5. After the game ends, you can choose to play again or exit.

## Requirements
- Python 3.x
- `random` library (pre-installed with Python)

## Running the Game
To run the game, use the following command in your terminal:

```bash
python guessing_game.py
