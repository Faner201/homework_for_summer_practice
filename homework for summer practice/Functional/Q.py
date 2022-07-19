def main():
    countries_count = int(input())

    all_cites = {}

    for _ in range(countries_count):
        country, *cities = input().split()
        for city in cities:
            all_cites[city] = country

    cities_count = int(input())
    for _ in range(cities_count):
        cit = input()
        print(all_cites[cit])


main()