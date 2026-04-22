import pandas as pd
#table = pd.read_csv("Indian_Traffic_Violations.csv")
#print(table)
#print(table.columns)
#print(len(table))

#print(table[["Fine_Amount","Vehicle_Model_Year"]])
#new=(table[["Fine_Amount","Vehicle_Model_Year"]])
#print(new)

#print(table['Violation_Type'])

#result = table[table['Violation_Type'] == 'No Seatbelt']
#print(result)

#result = table [table['Vehicle_Model_Year']>= 2018]
#print(result)

#Q) find violation from location Maharashtra
#Q) find violation by driver age below 30


#result_location = table[table['Location']=='Maharashta']
#print(result_Location)


studentTable = pd.read_csv('students.csv')
#print(studentTable)
#print(studentTable['name'])
#print(studentTable[['name','mark']])

#result = studentTable[ studentTable['mark']<=575]
#print(result)

#syntax: table () & ()

#result = studentTable[(studentTable['mark']<=570) & (studentTable['age']>=20)]
#print(result)

#result = studentTable[(studentTable['mark']<=570) | (studentTable['age']>=20)]
#print(result)

#Q) find student with mark above 560 and below 575

#result = studentTable[(studentTable['mark']>=560) & (studentTable['mark']<=575)]
#print(result)

#result = studentTable[ studentTable['mark'] . between(560,575)]
#print(result)

#Q) find students who's age btwn 21 and 22, mark btwn 560 and 580

result = studentTable[(studentTable['age'].between(21,22)) & (studentTable['mark']. between(560,580))]
print(result)