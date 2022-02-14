from random import choice
from string import ascii_lowercase


class Hangman:
    tuple_of_words = ('python', 'java', 'kotlin', 'javascript')
    life = 8

    def __init__(self):
        self.word = str()
        self.chosen_word = choice(self.tuple_of_words)
        self.field = list('-' * len(self.chosen_word))
        self.answers = set()

    @staticmethod
    def greetings():
        return 'H A N G M A N'

    def letter_check(self, letter):
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter not in ascii_lowercase:
            print('Please enter a lowercase English letter')
        elif letter in self.answers:
            print("You've already guessed this letter")
        elif letter in self.chosen_word and letter not in self.answers:
            for i in range(len(self.chosen_word)):
                if self.chosen_word[i] == letter:
                    self.field[i] = letter
        else:
            self.life -= 1
            print("That letter doesn't appear in the word")

        self.answers.add(letter)

    def result(self):
        if '-' not in self.field:
            return f'You guessed the word {self.chosen_word}!\nYou survived!'
        elif self.life == 0:
            return 'You lost!'

    def main(self):
        print(self.greetings())

        while True:
            menu = input('Type "play" to play the game, "exit" to quit: ')

            if menu == 'play':
                while True:
                    print(f"\n{''.join(self.field)}")
                    letter = input('Input a letter: ')
                    self.letter_check(letter)

                    if self.result() is not None:
                        print(self.result())
                        print()
                        break
            elif menu == 'exit':
                break
            else:
                continue


def main():
    h = Hangman()
    h.main()


if __name__ == '__main__':
    main()
