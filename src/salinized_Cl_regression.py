import pandas as pd
import sys
filepath = sys.argv[1]
df=pd.read_csv(filepath)

def Cl_predictor(x):
    y=0.32821783*x-125.93039341
    return y

df['Cl']=0.0
for index, row in df.iterrows():
    val=Cl_predictor(row['EC'])
    df.at[index, 'Cl'] = val

df.to_csv(filepath, index=False)