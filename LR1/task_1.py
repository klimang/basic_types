numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


average_of_numbers = sum(filter(None, numbers)) / len(numbers)

numbers[numbers.index(None)] = average_of_numbers
print("Измененный список:", numbers)
