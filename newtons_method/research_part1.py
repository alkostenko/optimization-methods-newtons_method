import start_values
import function
import derivative
import mod_newtons_method
import sven
import golden
import dsk_powell
import criterion
import table

# x_list=[start_values.x0]
# h=start_values.h
# scheme=start_values.scheme
# search_type=start_values.search_type
# search_accuracy=start_values.search_accuracy
# svenn_parametr=start_values.svenn_parametr
# criterion_type=start_values.criterion_type

# f_min=[]

def research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r=0, t=0):
    _lambda=0
    iteration=0
    counter=0
    for _ in  range(1000):
        # print("Ітерація {}".format(iteration))
        x=x_list[iteration]
        x1=x[0]
        x2=x[1]
        s=mod_newtons_method.dir(scheme, h, x1, x2, r, t)
        interval, counter=sven.sven(x, _lambda, svenn_parametr, s, counter, r, t)
        if search_type=="golden":
            _lambda, counter=golden.golden(x,interval[0], interval[1], search_accuracy, s, counter, r, t)
        else:
            _lambda, counter=dsk_powell.dsk_powell(x,interval[0], interval[1], search_accuracy, s, counter, r, t)
        x_list.append(mod_newtons_method.mod_newton_method(x, _lambda, s))
        counter+=1
        # print("x1 = {}\nx2 = {}\nf(x1, x2) = {}".format(x_list[iteration+1][0], x_list[iteration+1][1], function.f(x_list[iteration+1][0], x_list[iteration+1][1], r,t)))
        if criterion.criterion(criterion_type, x_list, 0.001, h, scheme, r,t)!=True and iteration<999:
            iteration+=1
            continue
        else:
            # print("Мінімальне значення функції з точністю {} дорівнює {}".format(0.001, function.f(x_list[iteration+1][0], x_list[iteration+1][1], r,t)))
            f_min.append(function.f(x_list[iteration+1][0], x_list[iteration+1][1], r,t))
            break
        
    
    return f_min, counter, x_list


def best(x0=start_values.x0, r=0, t=0):
    counter_2=0
    h=start_values.h
    scheme=start_values.scheme
    search_type=start_values.search_type
    search_accuracy=start_values.search_accuracy
    svenn_parametr=start_values.svenn_parametr
    criterion_type=start_values.criterion_type

    # В залежності від кроку h при обчисленні похідних
    print("----- В залежності від кроку h при обчисленні похідних")
    f_min=[]
    hs=[1, 0.1, 0.01, 0.001, 0.0001]
    counter_list=[]
    for h in hs:
        # print("Крок h при обчисленні похідних {}".format(h))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)

    best_h=hs[f_min.index(min(f_min))]
    table.table(hs, counter_list, f_min, "Величина кроку h")
    print("Найкраще значення кроку h при обчисленні похідних: {}".format(best_h))

    h=best_h
    counter_2+=sum(counter_list)

    # В залежності від схеми обчислення похідних
    print("----- В залежності від схеми обчислення похідних")
    f_min=[]
    counter_list=[]
    schemes=["ліва різниця", "права різниця", "центральна різниця"]
    for scheme in schemes:
        # print("Cхема обчислення похідних {}".format(scheme))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)

    best_scheme=schemes[f_min.index(min(f_min))]
    table.table(schemes, counter_list, f_min, "Схема обчислення похідних")
    print("Найкраща схема обчислення похідних: {}".format(best_scheme))

    scheme=best_scheme
    counter_2+=sum(counter_list)

    # В залежності від методу одновимірного пошуку
    print("----- В залежності від методу одновимірного пошуку")
    f_min=[]
    counter_list=[]
    search_types=["golden", "dsk-powell"]
    for search_type in search_types:
        # print("Метод одновимірного пошуку {}".format(search_type))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)
    
    best_search_type=search_types[f_min.index(min(f_min))]
    table.table(search_types, counter_list, f_min, "Метод одновимірного пошуку")
    print("Найкращий метод одновимірного пошуку: {}".format(best_search_type))

    search_type=best_search_type
    counter_2+=sum(counter_list)

    # В залежності від точності методу одновимірного пошуку
    print("----- В залежності від точності методу одновимірного пошуку")
    f_min=[]
    counter_list=[]
    search_accuracy_list=[0.01, 0.001, 0.0001]
    for search_accuracy in search_accuracy_list:
        # print("Точність методу одновимірного пошуку {}".format(search_accuracy))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)

    best_search_accuracy=search_accuracy_list[f_min.index(min(f_min))]
    table.table(search_accuracy_list, counter_list, f_min, "Точність методу одновимірного пошуку")
    print("Найкраща точність методу одновимірного пошуку: {}".format(best_search_accuracy))

    search_accuracy=best_search_accuracy
    counter_2+=sum(counter_list)

    # В залежності від значення параметру Свенна 
    print("----- В залежності від значення параметру Свенна ")
    f_min=[]
    counter_list=[]
    deltas=[0.1, 0.01, 0.001, 0.0001]
    for svenn_parametr in deltas:
        # print("Значення параметру Свенна {}".format(svenn_parametr))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)
    best_svenn_parametr=deltas[f_min.index(min(f_min))]
    table.table(deltas, counter_list, f_min, "Значення параметру Свенна")
    print("Найкраще значення параметру Свенна: {}".format(best_search_accuracy))

    delta=best_svenn_parametr
    counter_2+=sum(counter_list)

    # В залежності від вигляду критерію закінчення
    print("----- В залежності від вигляду критерію закінчення ")
    f_min=[]
    counter_list=[]
    criterion_types=[1]
    for criterion_type in criterion_types:
        # print("Вигляд критерію закінчення {}".format(criterion_type))
        x_list=[x0]
        f_min, counter, x_list=research(f_min, x_list, scheme, h, svenn_parametr, search_accuracy, criterion_type, search_type, r, t)
        counter_list.append(counter)

    best_criterion_type=criterion_types[f_min.index(min(f_min))]
    table.table(criterion_types, counter_list, f_min, "Вигляд критерію закінчення")
    print("Найкращий вигляд критерію закінчення: {}".format(best_criterion_type))

    criterion_type=best_criterion_type
    counter_2+=sum(counter_list)

    # best_values=[best_h, best_scheme, best_search_type, best_search_accuracy,  best_svenn_parametr, 1]
   
    print("Найменше значення функції при виборі найкращих умов: {}".format(min(f_min)))

    return min(f_min), x_list[f_min.index(min(f_min))], counter_2


best()











    
            
        
        

        


