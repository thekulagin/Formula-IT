numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_of_numbers = sum(numbers[:4]) + sum(numbers[5:])
amount_of_numbers = len(numbers)

numbers[4] = sum_of_numbers / amount_of_numbers

print("Измененный список:", numbers)
