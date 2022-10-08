import numpy as np

from function import f

# Вибір схеми обчислення похідних
def der_scheme(scheme, h, x1, x2, power, r, t):
    if scheme=="ліва різниця":
        return left_dif(h, x1, x2, power, r, t)
    elif scheme=="права різниця":
        return right_dif(h, x1, x2, power, r, t)
    else:
        return central_dif(h, x1, x2, power, r, t)

# Ліва різниця
def left_dif(h, x1, x2, power, r, t):
    # Перша похідна
    if power==1:
        return np.array([(f(x1,x2,r, t)-f(x1-h, x2, r, t))/h, (f(x1,x2,r, t)-f(x1, x2-h, r, t))/h])
        
    # Друга похідна
    else:
        l1=[(left_dif(h, x1, x2, 1, r, t)[0]-left_dif(h, x1-h, x2, 1, r, t)[0])/h, (left_dif(h, x1, x2, 1, r, t)[1]-left_dif(h, x1-h, x2, 1, r, t)[1])/h]
        l2=[(left_dif(h, x1, x2, 1, r, t)[0]-left_dif(h, x1, x2-h, 1, r, t)[0])/h, (left_dif(h, x1, x2, 1, r, t)[1]-left_dif(h, x1, x2-h, 1, r, t)[1])/h]
        return np.array([l1, l2])

# Права різниця
def right_dif(h, x1, x2, power, r, t):
    if power==1:
        return np.array([(f(x1+h,x2,r, t)-f(x1, x2, r, t))/h, (f(x1,x2+h,r, t)-f(x1, x2, r, t))/h])
    else:
        r1=[(right_dif(h, x1+h, x2, 1, r, t)[0]-right_dif(h, x1, x2, 1, r, t)[0])/h, (right_dif(h, x1, x2+h, 1, r, t)[1]-right_dif(h, x1, x2, 1, r, t)[1])/h]
        r2=[(right_dif(h, x1, x2+h, 1, r, t)[0]-right_dif(h, x1, x2, 1, r, t)[0])/h, (right_dif(h, x1, x2+h, 1, r, t)[1]-right_dif(h, x1, x2, 1, r, t)[1])/h]
        return np.array([r1, r2])

# Центральна різниця
def central_dif(h, x1, x2, power, r, t):
    if power==1:
        return np.array([(f(x1+h,x2,r, t)-f(x1-h, x2, r, t))/h, (f(x1,x2+h,r, t)-f(x1, x2-h, r, t))/(2*h)])
    else:
        c1=[(central_dif(h, x1+h, x2, 1, r, t)[0]-central_dif(h, x1-h, x2, 1, r, t)[0])/(2*h), (central_dif(h, x1, x2+h, 1, r, t)[1]-central_dif(h, x1, x2-h, 1, r, t)[1])/(2*h)]
        c2=[(central_dif(h, x1, x2+h, 1, r, t)[0]-central_dif(h, x1, x2-h, 1, r, t)[0])/(2*h), (central_dif(h, x1, x2+h, 1, r, t)[1]-central_dif(h, x1, x2-h, 1, r, t)[1])/(2*h)]
        return np.array([c1, c2])

    

