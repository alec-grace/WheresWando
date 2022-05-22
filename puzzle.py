# Alec Grace
# Start: 5/15/2022
# Description: class to generate puzzle and maintain variables
import random
from text_images import images


class Puzzle:
    def __init__(self, chars: dict, width: int, height: int, goal: str):
        self.chars = chars
        self.width = width
        self.height = height
        self.goal = goal
        self.difficulty = 0

    # TODO: insert goal characters
    #   - start with regular link
    #   - figure out hyperlink
    def generate_text(self):
        with open('result.txt', 'w') as outfile:
            for h in range(self.height):
                for w in range(self.width):
                    key = random.randint(0, len(self.chars.keys()) - 1)
                    outfile.write(self.chars[key])
                outfile.write('\n')

    # TODO: Flesh out menu options
    #   - determine difficulty meaning
    #   - determine options for goal text
    def change_settings(self):
        menu = '----- MENU ------\n' \
               '1. Height\n' \
               '2. Width\n' \
               '3. Difficulty\n' \
               '4. Goal text\n' \
               '0. Exit\n' \
               '\nEnter setting to change: '

        good_input = False
        choice = 0
        while not good_input:
            try:
                choice = int(input(menu))
                good_input = True
            except TypeError:
                print('~~Invalid input~~')

        self.__setting_manip(choice)

    def __setting_manip(self, choice):
        good_input = False
        if choice == 1:
            while not good_input:
                try:
                    self.height = int(input('Enter new value: '))
                    good_input = True
                except TypeError:
                    print('~~Invalid input~~')
        elif choice == 2:
            while not good_input:
                try:
                    self.width = int(input('Enter new value: '))
                    good_input = True
                except TypeError:
                    print('~~Invalid input~~')
        elif choice == 3:
            while not good_input:
                try:
                    self.difficulty = int(input('Enter new value: '))
                    good_input = True
                except TypeError:
                    print('~~Invalid input~~')
        elif choice == 4:
            while not good_input:
                try:
                    image_choice = int(input('Enter image number: '))
                    with open('out_image.txt', 'w', encoding='utf-8') as outfile:
                        outfile.write(images[image_choice])
                    good_input = True
                except TypeError or ValueError:
                    print('~~Invalid input~~')
