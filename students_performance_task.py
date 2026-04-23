import pandas as pd
studentsTable = pd.read_csv("student_performance.csv")



#1) find avg score and attendace of female students age wise

# result = studentsTable[studentsTable['gender'] == 'Female'].groupby('age').agg(
#     avgprevious_score=('previous_score','mean'),
#     avgattendance_rate = ('attendance_rate','mean')
# )
# print(result)


#2) find avg study hours of students scoring above 80 parental education wise

# result = studentsTable[studentsTable['final_score'] > 80].groupby('parent_education').agg(
#     avgstudy_hours_per_week=('study_hours_per_week','mean')
# )
# print(result)


#3) display female students only

# result = studentsTable[studentsTable['final_score']>90]
# print(result)

#4) find avg attendance and total students scoring below 70 gender wise

# result = studentsTable[studentsTable['previous_score']<70].groupby('gender').agg(
#     avgattendance_rate=('attendance_rate','mean'),
#     totalstudent_id =('student_id','count')
# )
# print(result)

#5) find avg score of students with attenda ce above 75 parent education wise

# result = studentsTable[studentsTable['attendance_rate']>75].groupby('parent_education').agg(
#     avgfinal_score=('final_score','mean')
# )
# print(result)

#6)find max score

# result = studentsTable['final_score'].max()
# print(result)

#7)find avg study hours

# result = studentsTable['study_hours_per_week'].mean()
# print(result)


#8) find avg score of students age below 18 gender wise

# result = studentsTable[studentsTable['age']<18].groupby('gender').agg(
#     avgprevious_score=('previous_score','mean')
# )
# print(result)

#9)find total students with internet access age wise

# result = studentsTable[studentsTable['internet_access'] == 'Yes'].groupby('age').agg(
#     totalstudent_id =('student_id','count') 
# )
# print(result) 

#10) find average score and study hours of students attendance above 70 age wise

result = studentsTable[studentsTable['attendance_rate']>70].groupby('age').agg(
    avgfinal_score = ('final_score','mean'),
    avgstudy_hours_per_week = ('study_hours_per_week','mean')
)
print(result)