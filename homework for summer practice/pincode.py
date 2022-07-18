def check_pin(pincode) -> str:
    [a, b , c] = pincode.split("-")
    return is_prime(int(a)) and is_palindrom(b) and is_power_of_two(int(c))


def is_prime(a) -> bool:
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def is_palindrom(b) -> bool:
    return b == b[::-1]
    

def is_power_of_two(c) -> bool:
    return (c & (c - 1) == 0) and c != 0


def main():
    pincode = input()
    print("Корректен" if check_pin(pincode) else "Некорректен")


main()