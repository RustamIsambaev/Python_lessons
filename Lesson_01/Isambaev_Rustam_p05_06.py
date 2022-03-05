# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
import Isambaev_Rustam_my_module as My_module
my_revenue = round(My_module.my_float_number_input('введите выручку', '', True), 2)
my_costs = round(My_module.my_float_number_input('введите издержки', '', True), 2)
my_profit = round(my_revenue - my_costs, 2)
if my_profit > 0:
    my_personal_qty = My_module.my_integer_number_input('укажите численность персонала', 'значение не может '
                                                                                         'быть отрицательным '
                                                                                         'числом!!!')
    print('Финансовый результат: Прибыль составляет:', my_profit)
    print(f'Рентабельность составляет: {round(my_profit / my_revenue * 100, 2)}%')
    print(f'Прибыль в расчете на одного сотрудника составляет: {round(my_profit / my_personal_qty, 2)}')
elif my_profit < 0:
    print('Финансовый результат: Убыток составляет:', my_profit)
else:
    print('Финансовый результат: - составляет:', my_profit)