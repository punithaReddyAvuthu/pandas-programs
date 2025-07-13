import pandas as pd
def project_2_employee_data():
    print("/nPROJECT 2 : EMPLOYEE DATA ANALYZER")
    print("-" * 40)
employee_data = {
    'Employee ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 70000, 65000],
    'Experience (Years)': [2, 5, 3, 8, 6],
    'Performance Score': [80, 90, 70, 95, 85]
}

df = pd.DataFrame(employee_data)

print("Employee Data:\n", df)

print("\nAverage Salary:", df['Salary'].mean())

print("\nEmployees with more than 5 years of experience:")
print(df[df['Experience (Years)'] > 5])

print("\nEmployees with performance score >= 85:")
print(df[df['Performance Score'] >= 85])

max_salary = df['Salary'].max()
print("\nEmployee(s) with the highest salary:")
print(df[df['Salary'] == max_salary])
