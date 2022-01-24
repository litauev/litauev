proceeds = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if proceeds > costs:
    print('Фирма работает с пыбылью')
    income = proceeds - costs
    print('Рентабельность фирмы {:%}'.format(income / proceeds))
    employees = int(input('Введите количество сотрудников фирмы: '))
    print(f'Доходность фирмы на сотрудника составляет {income / employees} у.е.')
else:
    print('Фирма работает в убыток')
