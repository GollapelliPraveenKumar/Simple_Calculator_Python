import pandas as pd
import matplotlib.pyplot as plt


#Loading Dataset...
data = pd.read_csv("Employees.csv")
print(data.head())

#Basic Info.....
print(data.info())
print(round(data.describe()))
print(data.shape)
print(data["Department"].unique())

#ANALYSIS QUESTIONS
#1. Average Salary by Department.

avg_salary = data.groupby("Department")["Salary"].mean()
print(round(avg_salary),2)

avg_salary.plot(kind = "bar", title = "Average Salary by Department")
plt.ylabel("Average Salary")
plt.show()

#2. Gender Distribution

gender_count = data["Gender"].value_counts()
print(gender_count)

gender_count.plot(kind = "pie", autopct = "%1.1f%%", title = "Gender Distribution")
plt.show()

#3. Department Wise Employee Count

dept_count = data["Department"].value_counts()
print(dept_count)

dept_count.plot(kind = "bar", title = "Department wise Employee Count")
plt.ylabel("Employee Count")
plt.show()

#4. Average Experience by Department...

avg_exp = data.groupby("Department")["Experience"].mean()
print(round(avg_exp))

#5. Attrition Analysis....

attrition = data["Attrition"].value_counts()
print(attrition)

attrition.plot(kind = "pie", autopct = "%1.1f%%", title = "Attrition Rate")
plt.show()

#Attrition by Department...
attrition_dept = data[data["Attrition"] == "Yes"]["Department"].value_counts()
attrition_dept.plot(kind = "bar", title = "Attrition by Department", color = "orange")
plt.ylabel("Count")
plt.show()

#Correlation Between Experience And Salary...

plt.scatter(data["Experience"], data["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()