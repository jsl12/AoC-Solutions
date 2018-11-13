def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    phrases = [line.rstrip() for line in lines]
    return phrases


def all_unique(phrase):
    words = phrase.split(' ')
    unique_count = len(set(words))
    return unique_count == len(words)


def count_letters(word):
    res = {}
    for char in word:
        res[char] = word.count(char)
    return res

def check_validity(phrase):
    res = True
    words = phrase.split(' ')
    counts = []
    for word in words:
        lc = count_letters(word)
        for count in counts:
            if lc == count:
                res = False
        counts.append(lc)
    return res


p = read_input('day4_input.txt')
valids1 = [phrase for phrase in p if all_unique(phrase)]
print(len(valids1))

valids2 = [phrase for phrase in p if check_validity(phrase)]
print(len(valids2))