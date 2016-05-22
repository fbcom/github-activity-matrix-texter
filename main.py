#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse

from gamt import TextMatrix

def parse_args():
    parser = argparse.ArgumentParser(description='Github Activity Matrix Texter.')
    parser.add_argument('--text', metavar='word', type=str, nargs='+', required=True, help='textmessage to render')
    parser.add_argument('--path', metavar='dir', type=str, default='.', help='path to your git repository')
    parser.add_argument('--threshold', metavar='n', type=int, default=1, required=False, help='minimum number of commits per day')
    parser.add_argument('--font', default='5x3', choices=['5x3', '5x4', '5x5'], help='font selection')
    parser.add_argument('--customfont', metavar='customfont', type=str, default=None, required=False, help='font name i.e. "abc" if the font file is "abc_font.txt"')
    parser.add_argument('--fontpath', metavar='fontpath', type=str, default='.', required=False, help='path to font files')
    parser.add_argument('--preview', action='store_true', help='leave git repository untouched')
    #parser.add_argument('--align', default='left', choices=['left', 'right'], help='alignment of the rendered text')

    config = vars(parser.parse_args())
    config['text'] = ' '.join(config['text'])

    if config['customfont']:
        config['font'] = config['customfont']
    return config

def load_commits(path):
    return [None] * 200 #@todo implement

def main():

    # Parse command line arguments
    config = parse_args()

    # Load commit history
    commits = load_commits(config['path'])

    # Initialize text matrix
    text_matrix_generator = TextMatrix.TextMatrix()

    if not text_matrix_generator.set_font(config['font'], config['fontpath']):
        print "Fontname '%s' not found in %s" % (config['font'], config['fontpath'])
        sys.exit(1)

    text_matrix_generator.set_text(config['text'])
    matrix = text_matrix_generator.generate_print_matrix()

    print "\n".join(matrix) #@TODO remove

    # check if there are enough commits in the history of
    # the git repo in order to render the text matrix

    pixelcount = text_matrix_generator.count_set_pixel()
    max_threshold = len(commits) / pixelcount
    if len(commits) < pixelcount * config['threshold']:
        print "There are not enough commits in your git log to render the text in the given font."
        if config['threshold'] > 1 and max_threshold > 0:
            print "Your threshold is set too high for your current text and font selection. Try setting it to a maximum of %d." %( max_threshold)
            sys.exit(1)
        print "Try a shorter text or a different font."
        sys.exit(1)

if __name__ == '__main__':
    main()

