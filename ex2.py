

#""" Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве. 
#Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """

a_x = int(input("Введите первый координат х: "))
a_y = int(input("Введите первый координат y: "))
b_x = int(input("Введите второй координат х: "))
b_y = int(input("Введите второй координат y: "))

distance = lambda a, b, c, d: ((a - c) ** 2 + (b - d)**2)**(0.5)
res = distance(a_x, a_y, b_x, b_y)

print('Длина отрезка: ', format(res, '.3f'))

