import numpy as np

from function import calc_f

def dsk_powell(x, alpha1, alpha3, e, s, counter, r, t):
    counter+=1
    alpha2=(alpha3+alpha1)/2
    delta_alpha=alpha3-alpha2
    alpha_star=alpha2+((delta_alpha*(-calc_f(x, alpha1, s, r, t)+calc_f(x, alpha3, s, r, t)))/(2*(calc_f(x, alpha1, s, r, t)-2*calc_f(x, alpha2, s, r, t)+calc_f(x, alpha3, s, r, t))))
    f=[calc_f(x, alpha1, s, r, t), calc_f(x, alpha2, s, r, t), calc_f(x, alpha3, s, r, t), calc_f(x, alpha_star, s, r, t)]
    if np.abs(calc_f(x, alpha2, s, r, t)-calc_f(x, alpha_star, s, r, t))<=e and np.abs(alpha2-alpha_star)<=e:
        return alpha_star, counter
    
    
    else:
        while np.abs(calc_f(x, alpha2, s, r, t)-calc_f(x, alpha_star, s, r, t))>e and np.abs(alpha2-alpha_star)>e:
            f=[calc_f(x, alpha1, s, r, t), calc_f(x, alpha2, s, r, t), calc_f(x, alpha3, s, r, t), calc_f(x, alpha_star, s, r, t)]
            
            if f.index(min(f))==1:
                if alpha2>alpha_star:
                    alpha1=alpha_star
                else:
                    alpha3=alpha_star
            if f.index(min(f))==3:
                if alpha2<alpha_star:
                    alpha1=alpha2
                else:
                    alpha3=alpha2
                alpha2=alpha_star
            else:
                return alpha_star, counter

            a1=(calc_f(x, alpha2, s, r, t)-calc_f(x, alpha1, s, r, t))/(alpha2-alpha1)
            a2=(1/(alpha3-alpha2))*((calc_f(x, alpha3, s, r, t)-calc_f(x, alpha1, s, r, t))/(alpha3-alpha1)-a1)

            alpha_star=(alpha1+alpha2)/2-0.5*a1/a2
            counter+=1
        return alpha_star, counter

        

