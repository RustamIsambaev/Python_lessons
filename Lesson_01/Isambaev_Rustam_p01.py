# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в
# переменные, затем выведите на экран.
import Isambaev_Rustam_my_module as My_module

empty_string = ''
my_content = 'Здравствуй'
name = input('введите Ваше имя')
print(my_content, name, '!')
a = 3
b = 4
print('Прямоугольный треугольник имеет следующие стороны:\nкатет a =', a, '\nкатет b =', b)
c = My_module.my_integer_number_input('Чему равна длина гипотенузы c этого треугольника?', 'длина должна быть '
                                                                                           'положительным '
                                                                                           'числом!!!')
if c == (a ** 2 + b ** 2) ** (1 / 2):
    print('Ответ верный! гипотенуза c =', c)
else:
    print('Ответ неверный')