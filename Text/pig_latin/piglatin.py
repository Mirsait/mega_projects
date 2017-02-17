"""
"""
import sys
import re

def get_eng_to_piglatin(text):
    """ translate english to pig latin """
    words = text.replace('\W', ' ').split()
    #vowels = ['a','e','i','o','u','h']
    #consonant = ['qu', ]
    vowels = '\b[aeiouhAEIOUH]\W+'
    pig_words = words
    for word in words:
        stri =''
        # гласные
        res = re.findall(r'\b[aeiouhAEIOUH]\w+', word)
        if res:
            stri = re.sub(r'\b([aeiouhAEIOUH]\w+)', r'\1ya', word)
        else:
            # согласных
            stri = re.sub(r'\b([^aeiouhAEIOUH ]+)(\w+)', r'\2\1ay', word)
        print(stri)

    return pig_words


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = get_eng_to_piglatin(sys.argv[1])
    else:
        text = 'Error: No text!'
    print(text)
