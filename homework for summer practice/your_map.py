def simple_map(operation, values):
    entrace = []
    for i in range(len(values)):
        entrace.append(operation(values[i]))
    return entrace
    
def main():
    values = [1, 3, 1, 5, 7]
    operation = lambda x: x + 5
    print(*simple_map(operation, values))

main()