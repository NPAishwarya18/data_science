import pandas as pd
df=pd.read_csv(r'D:\data.csv')
#http://localhost:8888/edit/data.csv
print("First few rows")
print(df.head())

print("\Summary statistics")
print(df.describe())

filtered_data=df[df['Age']>30]
print("\n Filtered data(Age>30):")
print(filtered_data)

sorted_data=df.sort_values(by='Salary',ascending=False)
print("\n Sorted data(by salary):")
print(sorted_data)

df['Bonus']=df['Salary']*0.1
print("\n Data with new column(Bonus):")
print(df)

df.to_excel('output.xlsx',index=False)
print("\n Data written to output.xlsx")


