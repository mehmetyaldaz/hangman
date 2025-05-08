# Hangman Game (Console-based)

This is a Python console-based Hangman game that lets users guess a hidden word, one letter at a time, within a limited number of attempts. The game includes difficulty levels, colorful output using `colorama`, and ASCII art to represent the Hangman's progression.

## Features

- Random word selection from an external `words.txt` file
- Difficulty levels: Easy, Medium, Hard
- ASCII art of the hangman that updates with each incorrect guess
- Letter-by-letter guessing
- Option to guess the entire word
- Colorful game output using the `colorama` library

## How to Play

1. Run the game:
   ```bash
   python hangman.py
   ```
2. Choose a difficulty level (`easy`, `medium`, or `hard`).
3. Guess one letter per turn.
4. You can type `-` and then attempt to guess the entire word at once.
5. The game ends when:
   - You correctly guess all letters in the word (You win! 🎉)
   - You exceed the allowed number of incorrect guesses (Game over 💀)

## Files

- `hangman.py`: Main Python script with the game logic.
- `words.txt`: Text file containing a list of words (one or more per line).
- `README.md`: This documentation.

## Requirements

- Python 3.x
- `colorama` library for colored console output:
  ```bash
  pip install colorama
  ```
