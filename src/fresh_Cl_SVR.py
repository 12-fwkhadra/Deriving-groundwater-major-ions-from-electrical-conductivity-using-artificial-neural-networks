
import pandas as pd
import numpy as np
import pickle
import sys
filepath = sys.argv[1]
df=pd.read_csv(filepath)

with open('svr_model.pkl', 'rb') as file:
    svr_model = pickle.load(file)

X=df['EC']
X=X.values
X=np.reshape(X,(-1,1))

predictions=svr_model.predict(X)

df['Cl']=predictions

df.to_csv(filepath, index=False)

