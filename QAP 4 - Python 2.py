# A program created to allow the user to enter the total amount of sales each month and be displayed in a graph.
# Created On: March 22/2023
# Author: Samantha Hynes

# Imports.
import matplotlib.pyplot as plt

# Create a list for the months.
Months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Empty list for user input of sales.
Sales = []

for i in range(0, 13):
    Jan = float(input("Enter total amount of sales for January: "))
    Sales.append(Jan)
    Feb = float(input("Enter total amount of sales for February: "))
    Sales.append(Feb)
    Mar = float(input("Enter total amount of sales for March: "))
    Sales.append(Mar)
    Apr = float(input("Enter total amount of sales for April: "))
    Sales.append(Apr)
    May = float(input("Enter total amount of sales for May: "))
    Sales.append(May)
    Jun = float(input("Enter total amount of sales for June: "))
    Sales.append(Jun)
    Jul = float(input("Enter total amount of sales for July: "))
    Sales.append(Jul)
    Aug = float(input("Enter total amount of sales for August: "))
    Sales.append(Aug)
    Sep = float(input("Enter total amount of sales for September: "))
    Sales.append(Sep)
    Oct = float(input("Enter total amount of sales for October: "))
    Sales.append(Oct)
    Nov = float(input("Enter total amount of sales for November: "))
    Sales.append(Nov)
    Dec = float(input("Enter total amount of sales for December: "))
    Sales.append(Dec)
    break

# Defining x/y-axis and lists for readability.
x_axis = Months
y_axis = Sales

# Plotting the graph ~with details~.
plt.bar(x_axis, y_axis, width=0.5, color="c")
plt.title("Total Amount of Sales each Month", fontweight="bold", fontsize="12")
plt.xlabel("Month", fontweight="bold")
plt.xticks(Months, rotation=60)
plt.ylabel("Sales($)", fontweight="bold")

# Present the graph.
plt.show()

