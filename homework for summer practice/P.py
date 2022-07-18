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
    
    for key in dictionary:
        pairs = [-dictionary[key], key]

    for pair in sorted(pairs):
        count, word = pair
        print(word)


main()