def main():
    height, width, mines = map(int, input().split())
    field = [[0 for _ in range(height)] for _ in range(width)]

    for _ in range(mines):
        y, x = map(int, input().split())
        field[x - 1][y - 1] = '*'

    for y in range(height):
        for x in range(width):
            if field[x][y] == '*':
                print('*', end = " ")
            else:
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < width and 0 <= y + j < height and field[x + i][y + j] == '*':
                            count += 1
                print(count, end = " ")
        print()

main()
