def gemetria(word) -> str:
    return sum(map(lambda x: ord(x) - ord('A') + 1, word.upper()))


def main():
    words = []

    while word:= input():
        words.append(word)

    for word in sorted(words, key = lambda letter: (gemetria(letter), letter)):
        print(word)


main()