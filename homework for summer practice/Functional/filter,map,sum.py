def check(box):
   return list(filter(lambda x: x % 9 == 0, box))


def main():
    box = range(10, 100)
    summing =  sum(map(lambda x: x ** 2, check(box)))
    print(summing)

main()
