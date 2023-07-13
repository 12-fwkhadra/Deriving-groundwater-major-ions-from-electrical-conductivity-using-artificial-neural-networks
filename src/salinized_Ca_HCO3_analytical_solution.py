
import pandas as pd
import sys
filepath = sys.argv[1]
df=pd.read_csv(filepath)

df['Ca']=0.0
df['HCO3']=0.0

def Ca_calculator(EC, Na, Mg, K):
    if EC>=300 and EC<=3000:
        Ca=(EC-33.3645-(4.0179*Na)-(3.14175*K)-(9.008415*Mg))/3.4515
        return Ca
        
    Na_meq=Na/22.99
    Mg_meq=(2*Mg)/24.312
    K_meq=K/39.1
    
    if EC <300:
        Ca_meq = (EC/100)-Na_meq-K_meq-Mg_meq
        Ca_mg = 20.04*((EC/100)-Na_meq-K_meq-Mg_meq)
        return Ca_mg
    if EC >3000:
        r=EC/133.605
        rr=r**(1/0.9058)
        Ca_meq=rr-Na_meq-K_meq-Mg_meq
        Ca_mg=20.04*(rr-Na_meq-K_meq-Mg_meq)
        return Ca_mg


#N03=average of the values in the original dataset
def HCO3_calculator(EC, Cl, SO4):
    NO3=7.2
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
    Na=row['Na']
    Mg=row['Mg']
    K=row['K']
    SO4=row['SO4']
    Cl=row['Cl']
    
    Ca=Ca_calculator(EC,Na,Mg,K)
    bicarb=HCO3_calculator(EC, Cl, SO4)
    df.at[index, 'Ca'] = Ca
    df.at[index, 'HCO3'] = bicarb

df.to_csv(filepath, index=False)