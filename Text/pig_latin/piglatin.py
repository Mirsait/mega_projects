"""
"""

def get_eng_to_piglatin(text):
    """ translate english to pig latin """


    return piglatin

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = get_eng_to_piglatin(sys.argv[1])
    else:
        text = 'Error: No text!'
    print(text)
