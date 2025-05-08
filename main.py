import random
from collections import Counter
from colorama import Fore, Back, Style
# List of ASCII art representing the hangman at various stages
hangmanAscii=[
'''
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
########
''',
'''
   ------
   |    |
   |    O
   |   /|\\
   |   
########
''',
'''
   ------
   |    |
   |    O
   |   
   |   
########
'''
,
'''
   ------
   |    |
   |    
   |   
   |   
########
'''
,
'''
   ------
   |    
   |    
   |   
   |   
########
''',
'''
   
   |    
   |    
   |   
   |   
########
''',
'''
   
     
      
     
   |       
########
''',
'''





########
''',
'''






'''

]
# Load words from words.txt into a list
words=[]
with open('words.txt', 'r') as file:
    for line in file:
        for word in line.split():
            words.append(word)

# Returns a random word from the list
def getRandomWord():
    return random.choice(words)

# Predefined hangman states for medium and hard difficulties
hangManStateMedium=[7,5,4,2,1,0]
hangManStateHard=[6,4,2,1,0]

# Default hangman states for easy difficulty
hangmanStateInts = [7,6,5,4,3,2,1,0]

# Game state variables
remainingAttempts = 0
guessedLetters = []
hangmanStateInt =0
hangmanState = hangmanAscii[8]
attemptsDifficulty = 1
currentWord = ""
currentWordTemp = ""
displayedCurrentWord =""
colors = [Fore.RED,Fore.BLACK,Fore.BLUE,Fore.MAGENTA,Fore.GREEN,Fore.CYAN,Fore.MAGENTA,Fore.LIGHTCYAN_EX,Fore.YELLOW,Fore.LIGHTMAGENTA_EX]


# Display the current game screen (attempts, guessed letters, hangman, and word)
def printScreen():
    print("Remaining Attempts:{remainingAttempts}".format(remainingAttempts=remainingAttempts))
    print("Guessed Letters:")
    print(guessedLetters)
    print(colors[random.randint(0, len(colors)-1)], hangmanState)
    print(displayedCurrentWord)

# Prompt the player to choose difficulty and adjust attempts/hangman states accordingly
def selectDifficulty():
    global remainingAttempts
    global hangmanStateInts
    global hangmanStateInt
    difficulty = input("easy, medium, hard: ")
    if difficulty == "easy":
        remainingAttempts = 8
    elif difficulty == "medium":
        remainingAttempts = 6
        hangmanStateInts = hangManStateMedium
    elif difficulty == "hard":
        remainingAttempts = 5
        hangmanStateInts = hangManStateHard
    else:
        print("Invalid input")
        selectDifficulty()

# Check if all letters in the word have been guessed
def has_won(word, guessed_letters):
    word_counter = Counter(word)
    guess_counter = Counter(guessed_letters)

    for letter, count in word_counter.items():
        if guess_counter[letter] < count:
            return False
    return True

# Handle a single letter guess by the player
def guess(letter):
    global remainingAttempts
    global guessedLetters
    global hangmanState
    global currentWord
    global displayedCurrentWord
    global hangmanStateInt
    global currentWordTemp
    guessedLetters.append(letter)
    if letter in currentWordTemp:
        index = currentWordTemp.find(letter)
        displayedCurrentWord = displayedCurrentWord[:index] + letter + displayedCurrentWord[index + 1:]
        currentWordTemp = currentWordTemp[:index] + "*" + currentWordTemp[index + 1:]
    else:
        hangmanState = hangmanAscii[hangmanStateInts[hangmanStateInt]]
        remainingAttempts -= 1
        hangmanStateInt += 1



# Main game loop
def startGame():
    selectDifficulty()
    global remainingAttempts
    global guessedLetters
    global hangmanState
    global currentWord
    global displayedCurrentWord
    global currentWordTemp
    currentWord = getRandomWord()
    currentWordTemp = currentWord
    displayedCurrentWord = "_" * len(currentWord)
    printScreen()
    while remainingAttempts > 0:
        guessed = input("you can guess 1 letter at a time to guess the whole word type \"-\" \n")
        if len(guessed) != 1:
            continue
        elif guessed == "-":
            guessed = input("guess the whole word: \n")
            if guessed == currentWord:
                print("you win!")
                break
        guess(guessed)
        if has_won(currentWord, guessedLetters):
            print("you win!")
            break
        printScreen()
        if remainingAttempts == 0:
            print("you lose :(")
            print(currentWord)
            break
startGame()























































