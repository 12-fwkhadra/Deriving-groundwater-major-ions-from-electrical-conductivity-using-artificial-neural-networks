from chargeBalance_calculator import *
import pandas as pd
import sys
filepath = sys.argv[1]
df=pd.read_csv(filepath)

df['Mg']=0.0
df['Ca']=0.0
df['HCO3']=0.0

def Ca_Mg_calculator(EC, Na, K):
    if EC>=300 and EC<=3000:
        Mg=(EC-33.3645-(4.0179*Na)-(3.14175*K))/19.362915
        Ca=3*Mg
        return Ca, Mg
        
    Na_meq=Na/22.99
    K_meq=K/39.1
    
    if EC <300:
        Mg_meq = ((EC/100)-Na_meq-K_meq)/4
        Mg_mg=20.04*Mg_meq
        Ca_mg = 3*Mg_mg
        return Ca_mg, Mg_mg
    if EC >3000:
        r=EC/133.605
        rr=r**(1/0.9058)
        Mg_meq=(rr-Na_meq-K_meq)/4
        Mg_mg=20.04*Mg_meq
        Ca_mg=3*Mg_mg
        return Ca_mg, Mg_mg


#N03=1
def HCO3_calculator(EC, Cl, SO4):
    NO3=1
    if EC>=300 and EC<=3000:
        hco3= (EC-66.7654-(2.7689*Cl)-(1.4788*SO4)-(1.1456*NO3))/1.1142
        return hco3
    
    Cl_meq=Cl/35.453
    SO4_meq=(2*SO4)/96.06
    NO3_meq=NO3/62
    
    if EC<300:
        hco3_meq= (EC/100) - Cl_meq - SO4_meq - NO3_meq
        hco3_mg= 61.02*((EC/100)- Cl_meq - SO4_meq - NO3_meq)
        return hco3_mg
    
    if EC>3000:
        r=EC/133.605
        rr=r**(1/0.9058)
        hco3_meq=rr-SO4_meq - NO3_meq - Cl_meq
        hco3_mg=61.02*(rr-Cl_meq-SO4_meq-NO3_meq)
        return hco3_mg

for index, row in df.iterrows():
    EC=row['EC']
    SO4=row['SO4']
    Cl=row['Cl']
    Na=row['Na']
    K=row['K']
    
    Ca, Mg=Ca_Mg_calculator(EC, Na, K)
    bicarb=HCO3_calculator(EC, Cl, SO4)
    df.at[index, 'Ca'] = Ca
    df.at[index, 'Mg'] = Mg
    df.at[index, 'HCO3'] = bicarb

    C = cations_sum(Na,K,row['Ca'],row['Mg'])
    A = anions_sum(Cl,SO4,row['HCO3'],1)
    CB = charge_balance(C,A)
    accuracy = accuracy_check(C,A,CB)
    df.at[index,'Accuracy'] = accuracy


df.to_csv(filepath, index=False)
