from IPython.display import clear_output as co
import random


class Word:
    categories = {
        'fruits': ['banana', 'pear', 'apple', 'mango', 'cantaloupe', 'watermelon'],
        'office': ['chair', 'desk', 'stylo', 'monitor', 'laptop']
    }

    def __init__(self):
        category = input(
            f"Choose from a word category: {[i.title() for i in Word.categories.keys()]}").lower()
        if category in Word.categories.keys():
            word_choice = random.choice(Word.categories[category])
        self.text = word_choice
        self.to_guess = ['_' for i in self.text]

    def display(self):
        return " ".join(self.to_guess)


class LetterGame:
    chances = 7
    guessed_letters = set()

    @classmethod
    def run(self):
        word = Word()
        done = False

        while not done:
            if self.chances == 0:
                print(f'Game Over! The correct word was {word.text}')
                break
            if word.to_guess == list(word.text):
                print(f'You have guessed the word "{word.text}" correctly.')
                break

            co()
            # print(word.__dict__)
            confirm = input(
                "Type 'quit' to exit the program. Press any key to continue. ").lower()
            if confirm == 'quit':
                break
            print(word.display())
            print(f"You have {self.chances} chances remaining. ")

            guess = input('Guess a letter: ').lower()

            if guess in self.guessed_letters:
                input("You've already chosen that letter. Try again. ")
            else:
                self.guessed_letters.add(guess)

                if guess in word.text:
                    for idx, letter in enumerate(word.text):
                        if guess == letter:
                            word.to_guess[idx] = letter
                else:
                    self.chances -= 1
                    input('That letter was not found in the word. ')


LetterGame.run()
