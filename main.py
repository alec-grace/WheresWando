# Alec Grace
# Start: 5/13/2022
# Description: driver program for the "Where's Wando" game
import random
import sys


def goal_row(goal, chars):
    pass

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

# TODO:  Make "Puzzle" class to control variables
# Takes input from console to set size variable, default is 100000

def main():
    # Manipulate font size/color/style

    # Default settings
    height = 100
    width = 200
    goal = 'XXXXXXXXXX'
    # TODO: difficulty = 100 // potentially make this a factor in size, just give difficulty option
    #   - second option difficulty determines similarity between background and goal characters
    #       - train unsupervised ML to determine similarity ranking
    #           - Train on ASCII then test on Unicode
    #       - sort characters in binary tree
    #       - closer proximity = closer similarity
    #       - to generate goal line
    #           - generate avg Unicode score
    #           - difficulty is degree of difference from avg

    # Prompt user for character file
    character_file = input('Enter character file or (0) for default: ')
    char_list = parse_char_file(character_file)

    # Prompt user to change default settings
    # height
    # width
    # difficulty
    # goal
    # text
    # image
    # list of easy images
    # Generate 'Waldo image' - text art

    # Select target
    row_target = random.randint(0, height)
    col_target = random.randint(0, width)
    # full_goal = goal_row(goal, char_list)

    # Generate background text
    with open('result.txt', 'w') as outfile:
        for h in range(height):
            t_row = False
            if h == row_target:
                t_row = True
                outfile.write(goal)
            else:
                for w in range(width):
                    key = random.randint(0, len(char_list.keys()) - 1)
                    outfile.write(char_list[key])
            outfile.write('\n')


if __name__ == '__main__':
    main()
