# This program takes a paragraph as an user input, uses regular expression to identify
# each sentence in the paragraph, then returns the number of sentences in the paragraph
# it also matches sentences beginning with numbers

import re

def split_sentences(paragraph):
    # Use the look-ahead patter matching feature to identify sentences.
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences =  re.findall(pat, paragraph, re.DOTALL | re.MULTILINE)
    return sentences

def display_sentences(sentences):
    # Display the number of sentences in the paragraph.
    print('Number of sentences:', len(sentences))
    for sentence in sentences:
        print(sentence)


def main():
    # Prompt the user for a paragraph.
    paragraph = input('Please enter a paragraph: ')
    sentences = split_sentences(paragraph)
    display_sentences(sentences)

if __name__ == '__main__':
    main()
