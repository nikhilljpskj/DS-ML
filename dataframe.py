import pandas as pd
import numpy as np

data = {
    'First_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Arun'],
    'Last_Name': ['Smith', 'Jones', 'Johnson', 'Brown', 'Lee', 'Jacob'],
    'Age': [25, 30, 22, 35, 28, 25],
    'Salary': [50000, 60000, 45000, 70000, 55000, 45000],
    'Department': ['HR', 'IT', 'Marketing', 'Finance', 'Operations', 'Finance']
}

df = pd.DataFrame(data)

print("Top 5 rows:")
print(df.head())

columns_to_remove = ['Last_Name','Department']
df = df.drop(columns=columns_to_remove)

new_column_names = {'Age': 'Employee_Age', 'Salary': 'Employee_Salary'}
df = df.rename(columns=new_column_names)


print("\nDataFrame after removing columns and renaming:")
print(df)
