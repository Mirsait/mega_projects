import sys


def is_polydrome(text):
    return (text == text[::-1])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = is_polydrome(sys.argv[1])
    else:
        text = 'Error: No text!'
    print(text)
