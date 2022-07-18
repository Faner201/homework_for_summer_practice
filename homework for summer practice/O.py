def main():
    files_count = int(input())

    files = {}

    for _ in range(files_count):
        actions = input().split()
        files[actions[0]] = {
            "write" : "W" in actions,
            "read" : "R" in actions,
            "execute" : "X" in actions
        }

    request_count = int(input())
    for _ in range(request_count):
        request, name  = input().split()
        print("OK" if files[name][request] else "Access denied")

    
main()