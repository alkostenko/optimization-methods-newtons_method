from prettytable import PrettyTable as pt

def table(parametr, count, f, parametr_name):
    Table=pt([parametr_name, "Кількість ітерацій", "Мінімум функції"])
    for i in range(len(parametr)):
        Table.add_row([parametr[i], count[i], f[i]])
    print(Table)