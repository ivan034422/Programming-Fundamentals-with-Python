n = int(input())

positive_nums = []
negative_nums = []
odd_nums = []
even_nums = []

for i in range(n):
    current_numbers = int(input())
    if current_numbers >= 0:
        positive_nums.append(current_numbers)
    else:
        negative_nums.append(current_numbers)

    if current_numbers % 2 == 0:
        even_nums.append(current_numbers)
    else:
        odd_nums.append(current_numbers)

command = input()
if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)

