number = map(int, input().split())

print(min(filter(lambda x: x > 0, number)))