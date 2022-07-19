from collections import defaultdict


def main():

    dictionary = defaultdict(list)

    count = int(input())

    for _ in range(count):
        word, transcriptions = input().split(" - ")
        for transcription in transcriptions.split(", "):
            dictionary[transcription].append(word)

    keys = dictionary.keys()

    print(len(keys))
    for key in sorted(keys):
        print(key, end = " - ")
        print(", ".join(sorted(dictionary[key])))


main()