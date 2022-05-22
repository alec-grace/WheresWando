# Alec Grace
# Start: 5/13/2022
# Description: driver program for the "Where's Wando" game
from puzzle import Puzzle
import random
import sys


def check_valid_file(filename):
    try:
        open(filename, 'r')
        return True
    except FileNotFoundError or FileExistsError:
        print('Wow')
        return False


def parse_char_file(filename):
    the_dict = {}
    if not check_valid_file(filename):
        filename = 'default_list.txt'
    with open(filename, 'r') as infile:
        chars = infile.readline()
        infile.close()
    char_list = chars.split(',')
    for key in range(len(char_list)):
        the_dict[key] = char_list[key]

    return the_dict


# Takes input from console to set size variable, default is 100000

def main():
    # Manipulate font size/color/style

    # Default settings
    height = 100
    width = 200
    goal = 'XXXXXXXXXX'
    # TODO: difficulty = 100 // potentially make this a factor in size, just give difficulty option
    #   - second option difficulty determines similarity between background and goal characters
    #       - train unsupervised ML - NN to determine similarity ranking
    #           - Train on ASCII then test on Unicode
    #       - sort characters in binary tree
    #       - closer proximity = closer similarity
    #       - to generate goal line
    #           - generate avg Unicode score
    #           - difficulty is degree of difference from avg

    # TODO:
    # Prompt user for character file
    character_file = input('Enter character file or (0) for default: ')
    char_list = parse_char_file(character_file)

    search_text = Puzzle(char_list, width, height, goal)
    search_text.generate_text()

    # Prompt user to change default settings
    # height
    # width
    # difficulty
    # goal
    # text
    # image
    # list of easy images
    # Generate 'Waldo image' - text art
    search_text.change_settings()
    search_text.generate_text()


if __name__ == '__main__':
    main()
