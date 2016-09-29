import sys
import re
from collections import Counter


TOP_WORDS = 100


def load_data(filepath):
    with open(filepath, 'r') as input_file:
        data = input_file.read()
    return data


def get_most_frequent_words(text):
    text = re.split('\W+', text.lower())
    return Counter(text).most_common()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Вы не указали путь к файлу, который нужно проанализировать')
        sys.exit(1)
    for word, frequency in get_most_frequent_words(load_data(sys.argv[1]))[:TOP_WORDS]:
        print(word, frequency)
