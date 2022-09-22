import numpy as np
from prettytable import PrettyTable as pt

import research_part1
import function
import start_values


def check(x1,x2, e, r, t):
    return np.abs(function.f(x2[0], x2[1], r, t)-function.f(x1[0], x1[1], r, t))<=e


def best():
    rs=[1, 0.1, 0.01, 0.001, 0.0001]

    # В залежності від положення допустимої точки
    print("---------- В залежності від положення допустимої точки")
    xs=start_values.x_m
    variants=["Всередині допустимої області", "Поза допустимою областю"]
    counter_2=0
    counter_list_2=[]
    for x in xs:
        print("------- "+ variants[xs.index(x)])
        area_type=start_values.area_type
        f_min_list=[]
        x_min_list=[]
        counter_list=[]
        for r in rs:
            f_min, x_min, counter=research_part1.best(x, r, area_type)
            f_min_list.append(f_min)
            x_min_list.append(x_min)
            counter_list.append(counter)
            counter_2+=sum(counter_list)
            if check(x, x_min, 0.001, r, area_type)==True:
                break
            else:
                x=x_min

        Table= pt(["R", "Кількість ітерацій", "Аргументи функції", "Мінімум функції"])
        for i in range(len(counter_list)):
            Table.add_row([rs[i], counter_list[i], x_min_list[i], f_min_list[i]])
        print(Table)
        counter_list_2.append(counter_2)

    print("Найкращий вибір точки: {}".format(xs[counter_list_2.index(min(counter_list_2))]))

    # В залежності від виду допустимої області
    print("---------- В залежності від виду допустимої області")
    x=xs[counter_list_2.index(min(counter_list_2))]
    area_types=["convex", "not convex"]
    variants=["Опукла", "Неопукла"]

    for area_type in area_types:
        print("------- "+variants[area_types.index(area_type)])
        f_min_list=[]
        x_min_list=[]
        counter_list=[]
        for r in rs:
            f_min, x_min, counter=research_part1.best(x, r, area_type)
            f_min_list.append(f_min)
            x_min_list.append(x_min)
            counter_list.append(counter)
            counter_2+=sum(counter_list)
            if check(x, x_min, 0.001, r, area_type)==True:
                continue
            else:
                x=x_min


        Table= pt(["R", "Кількість ітерацій", "Аргументи функції", "Мінімум функції"])
        for i in range(len(counter_list)):
            Table.add_row([rs[i], counter_list[i], x_min_list[i], f_min_list[i]])
        print(Table)
        counter_list_2.append(counter_2) 
    print("Найкращий вибір допустимої області: {}".format(variants[counter_list_2.index(min(counter_list_2))]))

best()

 
