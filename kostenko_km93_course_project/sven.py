import numpy as np
import math

from function import calc_f

def sven_check(x, _lambda, delta, s, r, t):
    if calc_f(x,_lambda+delta, s, r, t)>calc_f(x,_lambda-delta, s, r, t):
        return -1
    else:
        return 1

def sven(x, _lambda, delta, s, counter, r, t):
    coef=sven_check(x, _lambda, delta, s, r, t)
    _lambda_previous=0
    _lambda_current=_lambda
    _lambda_next=_lambda_current+coef*delta
    counter+=1
    i=1
    while calc_f(x, _lambda_next, s, r, t)<calc_f(x, _lambda_current, s, r, t):
        _lambda_previous=_lambda_current
        _lambda_current=_lambda_next
        _lambda_next=_lambda_current+coef*delta*2**i
        i+=1
        counter+=1

    if (_lambda_current+_lambda_next)/2>_lambda_previous:
        interval=[_lambda_previous, (_lambda_current+_lambda_next)/2]
    else:
        interval=[(_lambda_current+_lambda_next)/2, _lambda_previous]
    return interval, counter

    

