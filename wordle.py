import math
import pandas
import csv


def all_possible_words():

    with open("possiblewords(1), "r") as file:
        words = []
        for word in file:
            word = word.isupper().strip()
            if len(word) == 5 and word.isalpha():
                words.append(word)

        print(words)
