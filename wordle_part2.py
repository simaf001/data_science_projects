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

    nonletters = {'b','r','n'}
    correct_letters = ['','','','','']
    letters_contained = {'i','g'}
    new_words = []
    y_words = []
    z_words = []
    final_word = []
    for i in range(len(words)):
        intersection = set.intersection(nonletters, set(words[i]))
        if len(intersection) == 0:
            new_words.append(words[i])
        #for char in nonletters:
            #if char in words[i]:
            #    new_words.append(words[i])

    for i in new_words:

        for j in i:

            for char in correct_letters:
                if char == j:
                    y_words.append(i)



    for y_word in y_words:
        intersection = set.intersection(letters_contained, set(y_word))
        if len(intersection) == len(letters_contained):
        #for char in letters_contained:
            #if char in y_word:
            z_words.append(y_word)

        #if letters_contained in y_word:

        #    z_words.append(y_words[i])
    for i in z_words:
        if i not in final_word:
            final_word.append(i)

    return final_word[0]


if __name__=="__main__":
    print(find_word(all_possible_words()))
