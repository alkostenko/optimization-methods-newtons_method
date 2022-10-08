from function import calc_f

def golden(x, a, b, e, s, counter, r, t):
    l=10*e
    while l>e:
        counter+=1
        l=b-a
        alpha1=a+0.382*l
        alpha2=a+0.618*l
        if calc_f(x, alpha1, s, r, t)<calc_f(x, alpha2, s, r, t):
            b=alpha2
            continue
        elif calc_f(x, alpha1, s, r, t)>calc_f(x, alpha2, s, r, t):
            a=alpha1
            continue
        else:
            a=alpha1
            b=alpha2
    return (a+b)/2, counter