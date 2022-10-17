# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def main():
    n_number = int(input('Введите число n:  '))
    sequence = []
    value = 4
    for key in range(1, n_number + 1):
        sequence.append(value)
        value +=3
    print(list(enumerate(sequence, start = 1)))
main()