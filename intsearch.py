def find_max_number(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

number_list = [5, 9, 3, 1, 7]
print(find_max_number(number_list))
