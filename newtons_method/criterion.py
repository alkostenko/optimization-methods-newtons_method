from distutils import dist
import numpy as np
import numpy as np

from function import f
from helping_func import distance
import derivative

def criterion(c_type, x_list, e, h, scheme, r, t):
    x=x_list[-2]
    xk=x_list[-1]

    x_diff=[xk[0]-x[0], xk[1]-x[1]]

    if c_type==1:
        if distance(x_diff)/distance(x)<=e and np.abs(f(xk[0], xk[1], r, t)-f(x[0], x[1], r, t))<=e:
            return True
    else:
        if distance(derivative.der_scheme(scheme, h, x[0], x[1], 1, r, t))<=e:
            return True


