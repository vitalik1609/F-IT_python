numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
count = len(numbers)
for i in range(len(numbers)):
    if not numbers[i]:
        l = sum(numbers[:i])+sum(numbers[i+1:])
        numbers[i] = l/count


print("Измененный список:", numbers)
