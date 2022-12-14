import random


def getHangmanWord(difficulty):
    filteredCountrisList = []
    countrisList = ['Benin', 'Ghana', 'Kenya', 'Niger', 'Sudan','Chile', 'Haiti','Libya','Palau','Syria', 'China','India','Malta','Qatar','Tonga',
'Egypt','Italy','Nauru','Samoa','Yemen','Gabon'	,'Japan','Nepal', 'Spain', 'Azerbaijan ' , 'Bangladesh', 'ElSalvador','Kazakhstan','Kyrgyzstan','Luxembourg','Madagascar','Mauritania','Montenegro',
'Mozambique', 'New Zealand', 'North Korea', 'Saint Lucia', 'Seychelles', 'South Korea', 'South Sudan', 'Tajikistan', 'Uzbekistan', 'Falkland Islands', 'French Polynesia'
,'Marshall Islands', 'Northern Ireland','Southern Ireland', 'South West Africa']

    if difficulty == 1:
        for x in countrisList:
            if len(x) == 5:
                filteredCountrisList.append(x)
    if difficulty == 2:
        for x in countrisList:
            if len(x) == 10:
                filteredCountrisList.append(x)
    if difficulty == 3:
        for x in countrisList:
            if len(x) == 15:
                filteredCountrisList.append(x)

    selectedWord = random.choice(filteredCountrisList)
    return selectedWord


def drawPlayfield(attempt=0):
    if attempt == 0:
        print('  +---+')
        print('      |')
        print('      |')
        print('      |')
        print('      ===')
    if attempt == 1:
        print('  +---+')
        print('  O   |')
        print('      |')
        print('      |')
        print('      ===')
    if attempt == 2:
        print('  +---+')
        print('  O   |')
        print('  |   |')
        print('      |')
        print('      ===')
    if attempt == 3:
        print('  +---+')
        print('  O   |')
        print(' /|   |')
        print('      |')
        print('      ===')
    if attempt == 4:
        print('  +---+')
        print('  O   |')
        print(' /|\  |')
        print('      |')
        print('      ===')
    if attempt == 5:
        print('  +---+')
        print('  O   |')
        print(' /|\  |')
        print(' /    |')
        print('      ===')
    if attempt == 6:
        print('  +---+')
        print('  O   |')
        print(' /|\  |')
        print(' / \  |')
        print('      ===')

    return None


def playerGuess(letter):
    return None


print(f'Choose your difficulty option. 1: 5 letter country name')
print(f'2: 10 letter word or 3: 15 letter country name')
userDifficulty = int(input('Enter your selection:'))

try:
    selectedWord = getHangmanWord(userDifficulty)
except IndexError:
    raise IndexError("There has been a stupid. Select a number between 1 and 3 as requested.") from None

selectedWord = getHangmanWord(userDifficulty)
print(selectedWord)  # TODO remove after testing is complete

playerGuesses = 6

secretWord = '?' * len(selectedWord)

guess = 0
badguesses = ""
goodguesses = ""
while guess < playerGuesses and '?' in secretWord:
    drawPlayfield(guess)
    print(secretWord)
    playerEntry = input(f'Choose a letter: (attempt #{guess}): ')

    if len(playerEntry) == 1:  # Punish the player for repeat guesses
        if playerEntry in goodguesses or playerEntry in badguesses:
            print('You already entered that letter! Penalty!')
            guess += 1
            continue
        if playerEntry.isalpha() == False:  # Punish the player for entering a number
            print('You were asked to enter a *letter*! Penalty!')
        # Count the number of times the character occurs in the word
        num_occurrences = selectedWord.count(playerEntry)
        if num_occurrences == 0:
            guess += 1
            badguesses += playerEntry

        # Replace the appropriate position(s) in secretWord with the actual letter.
        position = -1  # TODO: Rewrite this section of code and convert into a class or function
        for occurrence in range(num_occurrences):
            position = selectedWord.find(playerEntry, position + 1)  # Find the position of the next occurrence
            secretWord = secretWord[:position] + playerEntry + secretWord[position + 1:]  # Reveal the secret word
        goodguesses += playerEntry

if not '?' in secretWord:
    print('You Are A Winner!', end=' ')
else:
    drawPlayfield(guess)
    print('Game Over YEAH!', end=' ')

print(f'The word was {selectedWord}.')






