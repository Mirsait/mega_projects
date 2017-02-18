'''
Count Vowels
The program counts the number of
 vowels in the text and reports a sum of each vowel found.
'''
import sys
import re

def get_count_vowels(text):
    return [[char, list(text[:].lower()).count(char)] for char in ('aeiou')]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = get_count_vowels(sys.argv[1])
        for value in text:
            print(value)
