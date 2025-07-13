import pandas as pd
s1= pd.Series([1,2,3,4,5,6])
s2= pd.Series({'name':'priya','age':'22','city':'NYC'})

df1= pd.DataFrame({
    'name':['priya','isha','bhavya','rupa'],
    'age':[23,24,25,20],
    'city':['NYC','TX','GNT','BRLYN']
})
data = {
    'a': [1,2,3,4],
    'b': [4,5,6,7],
      
}
df2 = pd.DataFrame(data)
print(df2)