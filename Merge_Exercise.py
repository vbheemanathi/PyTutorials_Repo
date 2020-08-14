import pandas as pd

data1 = pd.read_csv(r'/Users/vars5086/Documents/Data_1.csv')

df1 = pd.DataFrame(data1)


data2 = pd.read_csv(r'/Users/vars5086/Documents/Data_2.csv')
df2 = pd.DataFrame(data2)

df3 = pd.concat([df1, df2], ignore_index = True)

print(df3)