import matplotlib.pyplot as plt
import numpy as np

company_products=["facewash","facecream"]
student_marks=[1500,2500]

products_perc=[]

for x in student_marks:
    res=(x*3000)*100
    products_perc.append(res)
print(products_perc)

def marks_line_chart():
    plt.plot(company_products,student_marks)
    plt.title("company products")
    plt.xlabel("company products")
    plt.ylabel("cost")
    plt.show()
def percentage_bar_chart():
    plt.bar(company_products,products_perc)
    plt.title("company Percentage")
    plt.xlabel("company Products")
    plt.ylabel("company Percentage")
    plt.show()

marks_line_chart()
percentage_bar_chart()