import matplotlib.pyplot as plt
import numpy as np

student_names=["Atiyyatullah","Sana","Lindani","Aparna"]
student_marks=[50,40,25,45]

marks_perc=[]

for x in student_marks:
    res=(x*50)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    plt.plot(student_names,student_marks)
    plt.title("Student Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
def percentage_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title("Students Percentage")
    plt.xlabel("Student Names")
    plt.ylabel("Students Percentage")
    plt.show()

marks_line_chart()
percentage_bar_chart()