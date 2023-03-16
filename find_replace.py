import pandas as pd
df = pd.read_csv('dataset_sample.csv', index_col=0)
print(df)
tf = df.copy()


# using exclusiion
print(df.query("Tactic == 'B'")['Tactic'])




print(tf)



