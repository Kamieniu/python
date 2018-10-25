import random
import inquirer


game_dict = {
    "programming": [
        "go lang",
        "python",
        "php",
        "scala"
    ],
    "food": [
        "chicken",
        "pizza",
        "water"
    ]
}


class WordClass:
    def __init__(self, category=None, word=None):
        self.category = category
        self.word = word


class HangmanGame:
    def __init__(self):
        self.words: list = []  # List of all avalibles words/categories
        self.wordsLength: int = 0  # Lenght of words
        self.randomNumber: int  # Random number from 0 to length of array
        self.randomWord: str

        self.filteredWords: list
        self.chosenValueMatchTable: list = []
        self.userInput: str  # User input from prompt

        print('Welcome in hangman game!')
        print('\n\n Let \'s play a game!')

        self.fillUpWords()
        self.choseCategory()

    def fillUpWords(self, array=game_dict):
        print(array.keys())

        for key in array.keys():
            values = array[key]

            for value in values:
                self.words.append(WordClass(key, value))

    def choseCategory(self):
        categories = game_dict.keys()
        questions = [
            inquirer.List('category',
                          message="What category you choose?",
                          choices=categories,
                          ),
        ]
        userChosenCategory = inquirer.prompt(questions)

        self.filterWordsWithCategory(userChosenCategory)

    def filterWordsWithCategory(self, categoryName):
        self.filteredWords = list(
            filter(lambda element: element.category == categoryName['category'], self.words))
        self.wordsLength = len(self.filteredWords)

        self.generateRandomNumber()

    def generateRandomNumber(self):
        self.randomNumber = int(random.uniform(0, self.wordsLength))

        self.choseRandomWord()

    def choseRandomWord(self):

        randomWord = self.words[self.randomNumber]

        self.chosenValueMatchTable = [''] * len(randomWord.word)

        self.randomWord = randomWord

        self.displayPrompt()

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def insertlettersToArray(self, index, letter):
        self.chosenValueMatchTable[index] = letter

    def displayPrompt(self):

        while ''.join(self.chosenValueMatchTable) != self.randomWord.word:
            print(
                f'Category {self.randomWord.category}, {self.chosenValueMatchTable}'
            )

            userInput = input('Give me a letter: ')

            if userInput.isalpha():
                self.userInput = userInput

                indexOfLetter = self.find(
                    self.randomWord.word, self.userInput)

                if indexOfLetter:
                    for index in indexOfLetter:

                        self.insertlettersToArray(index, self.userInput)

                else:
                    print('Wrong!')

            else:
                print('It\'s not a letter, dummy!')
                self.displayPrompt()
        print(f'Great, you won!')


hangmanGame = HangmanGame()
