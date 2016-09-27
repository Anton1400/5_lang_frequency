#-*- coding: utf-8 -*-
import sys
from collections import Counter
import re

def load_data(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def get_most_frequent_words(text, count):
    regular = re.compile("([^:.\-()+/«12–34567890»@#$%\];~№%*\s[=“?!&\,<>\^|…—]+)")
    words = regular.findall(text)
    frequent_words = Counter(words)
    return frequent_words.most_common(count)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска')
        sys.exit(1)
    for word, frequent in get_most_frequent_words(load_data(sys.argv[1]), 10):
        print(word, frequent)
