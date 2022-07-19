# digit = 0
# clearo = ''

# for digit in input():
#     if int(digit) % 2 == 0 :
#         clearo += digit
# print(len(clearo))

print(len([digit for digit in input() if int(digit) % 2 == 0]))
