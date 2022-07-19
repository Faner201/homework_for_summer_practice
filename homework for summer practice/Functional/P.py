from sys import stdin


def main():

    dictionary = {}

    for line in stdin:
        if line.rstrip() == "":
            break
        
        for word in line.split():
            if dictionary.get(word) == None:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    
    pairs = [(dictionary[key], key) for key in dictionary]

    for pair in sorted(pairs):
        c, word = pair
        print(word)


main()