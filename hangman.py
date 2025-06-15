import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

print("H A N G M A N")

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel
whale wolf wombat zebra'''.split()

number = random.randint(0, len(words)-1)
secretWord = words[number]
#print(secretWord)
gameOver = False
correctLetters = ''
missedLetters = ''
def showResult(word, letters):
    number = len(missedLetters)
    print(HANGMAN_PICS[number])
    blanks = '_' * len(word)
    for i in range(0, len(word)):
        if word [i] in letters:
            blanks = blanks[:i] + word [i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


def enterLetter(allLetters):
    while True:
        letter = input('enter letter: ')
        letter = letter.lower()
        if len(letter) != 1:
            print('!enter a single letter!')
        elif letter in allLetters:
            print('!the letter has already entered!')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('!this is not a letter!')
        else:
            return letter

def solvedWord(correctLetters, secretWord):
    for i in range(0, len(secretWord)):
        if secretWord[i] not in correctLetters:
            return False
    return True

#na razie nie koniec gry
while not gameOver:
    #pokazać rezultat
    showResult(secretWord, correctLetters)
    #napisać litere
    letter = enterLetter(correctLetters + missedLetters)
    #jeśli litera zgadnięta
    if letter in secretWord:
        #dodać ją
        correctLetters = correctLetters + letter
        #jeśli całe słowo zgadnięte
        if solvedWord(correctLetters, secretWord):
            gameOver = True
            #pogratulować
            showResult(secretWord, correctLetters)
            print('You won!')
            #koniec gry
    #inaczej
    else:
        missedLetters = missedLetters + letter
        #jeśli szanse skonczyły się
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            #powiadomić o przegranej
            showResult(secretWord , correctLetters)
            print('You lost')
            print(secretWord)
            #koniec gry
            gameOver = True
    if gameOver:
        answer = ""
        while answer != "yes" and answer != "no":
            answer = input("Do you want to play again?(yes/no): ")
            if answer == "no":
                break
            elif answer == "yes":
                print('''














''')
                number = random.randint(0, len(words)-1)
                secretWord = words[number]
                #print(secretWord)

                gameOver = False
                correctLetters = ''
                missedLetters = ''
            
