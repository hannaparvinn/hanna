import pandas as pd
table  = pd.read_csv('employee.csv')
#print(table)

# print(table['salary'].sum())
# print(table['salary'].mean())
# print(table['name'].min)
# print(table['salary'].min())
# print(table['salary'].max())
# print(table['empid'].count())


# result = table.agg(
    # totalsalary = ('salary','sum'),
    # avgSalary = ('salary','mean'),
    # firstEmployee = ('name','min'),
    # lastEmployee = ('name','max'),
# )
# print(result)

# result = table.groupby('dept').agg(
    # countofEmps = ('empid','count'),
    # Totalsalary = ('salary','mean'),
    # avgSalary = ('salary','mean'),
    # minAge = ('age','min')
# )
# print(result)

#Q) find employee avg experience, avg age in location wise

result = table.groupby('location').agg(
    avgExperience = ('exp','mean'),
    avgage = ('age','mean')
)
print(result)