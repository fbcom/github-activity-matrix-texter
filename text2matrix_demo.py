#!/usr/bin/python


def parse_font_definition(font_definition):
    """
    Parses test and line based font definition

    How this works:

        10 find font height
        20 find first or next letter
        30 parse letter
        40 goto 20
    """
    font = {}
    # helper variables for parsing
    font_height = 0
    parsing_flag = False
    parsing_line = 0
    parsing_letter = ''
    parsing_letter_width = 0
    parsing_buffer = []
    for line in font_definition:
        line = line.rstrip()
        if not line and not parsing_flag:
            continue

        if not font_height:
            font_height = int(line.rstrip())
            font['height'] = font_height
            # defining spacing between letters
            space_width = 2
            font['letter_spacing'] = space_width

            # adding a letter for spaces
            font[' '] = [' ' * space_width] * font_height
            font[' _width'] = space_width
            # adding a letter for unknowns
            font['unknown'] = ['#' * space_width*2] * font_height
            font['unknown_width'] = space_width*2
        else:
            if line or parsing_flag:
                if not parsing_flag and len(line) == 1:
                    # start parsing a letter
                    parsing_letter = line
                    parsing_letter_width = 0
                    parsing_flag = True
                    parsing_line = 0
                    parsing_buffer = []

                elif parsing_flag and parsing_line < font_height:
                    # parsing a letter
                    parsing_line += 1
                    parsing_buffer.append(line)
                    parsing_letter_width = max(parsing_letter_width, len(line))

                if parsing_line >= font_height:
                    # end parsing a letter
                    parsing_flag = False
                    font[parsing_letter] = parsing_buffer
                    font["%s_width" % (parsing_letter)] = parsing_letter_width
    return font


def load_font(file_name):
    with open(file_name) as f:
        font_definition = f.readlines()
    return parse_font_definition(font_definition)


def generate_print_matrix(font, text):
    """
    generates a matrix containing the text using the provided font
    """
    print_matrix = [''] * font['height']
    letter_spacing = font['letter_spacing']
    for letter in text.upper():
        y = 0
        if letter not in font:
            letter = 'unknown'
        letter_print_matrix = font[letter]
        letter_width = font["%s_width" % (letter)]
        for row in letter_print_matrix:
            print_matrix[y] = print_matrix[y] + row
            print_matrix[y] += ' ' * (letter_width-len(row) + letter_spacing)
            y = y + 1

    return print_matrix


def display_print_matrix(print_matrix):
    for row in print_matrix:
        print row


# Demo
import os
import string
text = string.ascii_uppercase + string.digits + "-"
for file_name in os.listdir("."):
    if file_name.endswith("_font.txt"):
        if 'font' in locals():
            print
        font = load_font(file_name)
        print_matrix = generate_print_matrix(font, text)
        display_print_matrix(print_matrix)