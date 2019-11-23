import os

#welcome message and how to play hangman

print("""
It's time to play hangman.

How to play:

One player thinks of a word and inputs it into the hangman.txt file; 
the other tries to guess what it is one letter at a time. 
The computer will tell you how many characters are in the word. 
If the guessing player suggests a letter that occurs in the word, 
the computer will display the letter.
If the letter does not occur in the word,
The computer will not add it to the word. 
Once the hangman is complete you have lost.

    """)

#Hangman
hangmanPics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   0   |
       |
       |
      ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']

# clear terminal

# import word from hagman.txt file
def readWords():
    word_options = []
    with open("hangman.txt", "r") as doc:
        for line in doc:
            list.append(word_options, line)
    return(word_options[0])

# Display Board
def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()

    print('Missing letters:', end=' ')

    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    
    print()

# GetGuess
def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        os.system('cls')
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

# Play Again?
def playAgain():
    #This function returns True if the player wants to play again
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

secretWord = readWords()
missedLetters = ''
correctLetters = ''
gameIsDone = False

# While Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is " + secretWord + " You have won!")
            gameIsDone = True
    else: 
        missedLetters = missedLetters + guess

        #Check if the player has guessed too many times 
        if len(missedLetters) == len(hangmanPics) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses! \nAfter " + str(len(missedLetters))  + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was " + secretWord + ".")
            gameIsDone = True

    # want to play again?
    if gameIsDone:
        if playAgain():
            secretWord = readWords()
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            blanks = '_' * len(secretWord)
        else: 
            break
# end while
                        