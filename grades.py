import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#Select File Path of Midterm Grades in CSV
grades = pd.read_csv(r'C:\Users\canvasexport.csv')

#sets all blanks to a value of 0
#ensure that the column in the Canvas Output says 'current score'
grades['current score'] = grades['current score'].fillna(0)
conditions = [
    (grades['current score'] >= 90),
    (grades['current score'] >= 80), 
    (grades['current score'] >= 70),
    (grades['current score'] >= 60), 
    (grades['current score'] <= 60),]

values = ['A', 'B', 'C', 'D', 'F']
#Check to make sure the title of the current score column is the same
grades['grade'] = np.select(conditions, values)

#ensure the column with course names says 'course'
unique_values = grades["course"].unique()

#grades.loc[(grades['current score'] < 70) & (grades['course'].isin(unique_values))]
#this is the file path for the new file being created
grades.to_csv("C:\Users\newfile.csv", index=False)

unique_values = grades["course"].unique()

failing = grades.loc[(grades['current score'] < 70) & (grades['course'].isin(unique_values))]

failing.to_csv("C:\Users\newfile.csv", index=False)

grade_counts = grades.groupby(['course', 'grade']).size()
grade_counts = grade_counts.sort_index(level=0)

# Convert the Series to a DataFrame using the `reset_index` method
grade_counts_df = grade_counts.reset_index()

# Use the `rename` method to change the name of the last column to "count"
grade_counts_df = grade_counts_df.rename(columns={0: "count"})

# Use the `style` attribute and the `background_gradient` method to add a color gradient to the values of the DataFrame
grade_counts_df.style.background_gradient()
#create another csv for failing by course
grade_counts_df.to_csv("C:\Users\new failing by course.csv", index=False)
print(grade_counts_df)

grades['failing'] = grades['current score'] < 70

# Group the DataFrame by the "student name" column and count the number of failing classes for each student
failing_counts = grades.groupby('student name')['failing'].sum()

# Count the number of students with each number of failing classes
fail_counts = failing_counts.value_counts()
print(fail_counts)

failing_df = failing_counts.reset_index()

# Filter the DataFrame for students who are failing 2 or more courses
failing_1_or_more = failing_df[failing_df['failing'] >= 1]

# Print the names of the students who are failing 1 or more courses
print(failing_1_or_more['student name'])

failing_df = failing_counts.reset_index()

# Filter the DataFrame for students who are failing 2 or more courses
failing_2_or_more = failing_df[failing_df['failing'] >= 2]

failing_2_or_more.to_csv(r'C:\Users\failing 2 or more.csv')

# Print the names of the students who are failing 2 or more courses
print(failing_2_or_more['student name'])
