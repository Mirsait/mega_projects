"""
"""
import sys
import re

def get_eng_to_piglatin(text):
    """ translate english to pig latin """
    words = text.replace('\W', ' ').split()
    pig_words = ''
    for word in words:
        # гласные
        res = re.findall(r'\b[aeiouhAEIOUH]\w+', word)
        if res:
            word = re.sub(r'\b([aeiouhAEIOUH]\w+)', r'\1ya', word)
        else:
            word = re.sub(r'\b([^aeiouhAEIOUHqQ ]+)(\w+)', r'\2\1ay', word)
            word = re.sub(r'\b(qu)(\w+)', r'\2\1ay', word)
        pig_words += word+' '
    return pig_words


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = get_eng_to_piglatin(sys.argv[1])
    else:
        text = 'Error: No text!'
    print(text)
