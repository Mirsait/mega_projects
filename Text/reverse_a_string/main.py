"""
Reverse a String – Enter a string and the program will reverse it and
print it out.
 """
import sys

def reverse_string (text):
    chars = list(text)
    chars.reverse()
    return ''.join(chars)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = reverse_string(sys.argv[1])
    else:
        text = 'Error: No string!'
    print(text)
