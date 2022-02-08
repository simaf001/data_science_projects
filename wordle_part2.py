import random



def all_possible_words(f="possiblewords.txt"):

    file = open(f, "r")
    words = []
    for word in file:
        word = word.lower().strip()
        if len(word) == 5 and word.isalpha():
            words.append(word)
    words = random.sample(words, len(words))
    return words

def find_word(words):

    nonletters = "aiyo"
    correct_letters = ["","","","",""]
    letters_contained = "drl"
    final_words = []
    for i in words:

        z = [char for char in i]

        for k in [char for char in letters_contained]:
            if k not in z:
                break
        else:

            for j in z:
                if j in nonletters:
                    break

            else:
                for j in range(len(correct_letters)):
                    if not correct_letters[j] == "":
                        if not z[j] == correct_letters[j]:
                            break
                else:
                    final_words.append(i)


    return final_words[0]


if __name__=="__main__":
    print(find_word(all_possible_words()))
