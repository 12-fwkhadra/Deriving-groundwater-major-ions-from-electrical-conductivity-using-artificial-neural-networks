def cations_sum(Na,K,Ca,Mg):
    sum = (Na/22.99)+(K/39.01)+(Ca/20.04)+(Mg/12.15)
    return sum

def anions_sum(Cl,SO4,HCO3,NO3):
    sum = (Cl/35.45)+(SO4/48.03)+(HCO3/61.02)+(NO3/62)
    return sum

def charge_balance(C,A):
    CB = ((C - A) / (C + A)) * 100
    return CB

def accuracy_check(C,A,CB):
    #check the paper "Chemical composition accuracy check" subsection for clarifications
    sum = C+A
    abs_CB = abs(CB)
    if sum>8:
        if abs_CB<4:
            return 'good'
        elif abs_CB>=4 and abs_CB<=8:
            return 'moderate'
        elif abs_CB>8:
            return 'bad'
    elif sum>=2 and sum<=8:
        if abs_CB < 6:
            return 'good'
        elif abs_CB >= 6 and abs_CB <= 12:
            return 'moderate'
        elif abs_CB > 12:
            return 'bad'
    elif sum<2:
        if abs_CB < 10:
            return 'good'
        elif abs_CB >= 10 and abs_CB <= 20:
            return 'moderate'
        elif abs_CB > 20:
            return 'bad'