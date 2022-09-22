#Курсова робота на тему "Модифікований метод Ньютона"
#Студента групи КМ-93 Костенка Олександра

import numpy as np
import math

import helping_func

def f(x1, x2, r=0, t=""):
    if r==0:
        # counter+=1
        return math.pow((10*(x1-x2)**2+(x1-1)**2), (1/4))
    else:
        if t=="convex": 
            # counter+=1
            return math.pow((10*(x1-x2)**2+(x1-1)**2), (1/4))-r*np.log(9-(x1+3)**2-x2**2)
        else:
            # counter+=1
            return math.pow((10*(x1-x2)**2+(x1-1)**2), (1/4))-r*(np.log(9-(x1+3)**2-x2**2)+np.log((x1+3)**2+x2**2-1))



# def p(x1, x2, r, t):
#     sum=0
#     for i in range(len(g(x1, x2, t))):
#         sum+=np.log(g(x1, x2, t)[i])
#     return -r*sum

# def g(x1, x2, t):
#     if t=="convex":   
#         print(x1)
#         print(x2)     
#         return [9-(x1+3)**2-x2**2]
#     else:
#         return [9-(x1+3)**2-x2**2, (x1+3)**2+x2**2-1]

def calc_f(x, _lambda, s, r, t):
    _lambda=_lambda/helping_func.distance(s)
    return f(x[0]+_lambda*s[0], x[1]+_lambda*s[1], r=0, t="")
    