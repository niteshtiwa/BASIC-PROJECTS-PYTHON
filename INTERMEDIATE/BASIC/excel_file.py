import pandas as pd
# df = pd.read_excel('data.xlsx')
# print(df)
data ={
  'phone':['507110435']
}
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index = False)
