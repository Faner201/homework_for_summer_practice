def main():

    number = int(input())

    matrix = [0, 0]

    for _ in range(number - 1):
        matrix = [matrix, matrix]

    print(matrix)

main()