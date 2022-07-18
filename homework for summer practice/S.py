def main():

    dictionary = {}

    count = int(input())

    for _ in range(count):
        word, transcriptions = input().split("-")
        for transcription in transcriptions.split(", "):
            if dictionary.get(transcription) == None:
                dictionary[transcription] = [word]
            else:
                dictionary[transcription].append(word)

    keys = dictionary.keys()

    print(len(keys))
    for key in sorted(keys):
        print(key, end = "-")
        print(", ".join(sorted(dictionary[key])))


main()