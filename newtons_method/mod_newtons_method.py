#Модифікований метод Ньютона

from re import S
import numpy as np
import math 

import helping_func
import derivative

der_scheme=derivative.der_scheme

def mod_newton_method(x, _lambda, s):
    x_new=[]
    _lambda=_lambda/helping_func.distance(s)
    x_new.append(x[0]+_lambda*s[0])
    x_new.append(x[1]+_lambda*s[1])
    return x_new

def dir(scheme, h, x1, x2, r, t):
    s=np.array(np.reshape(-1*np.matmul(np.linalg.matrix_power(der_scheme(scheme, h, x1, x2, 2, r, t), (-1)), np.reshape(der_scheme(scheme, h, x1, x2, 1, r, t), (2, 1))), (1, 2)))[0]
    return s