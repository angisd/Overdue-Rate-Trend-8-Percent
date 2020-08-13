# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# corresponding y axis values
y = [0.75, 0.42, 0.16, 0.14, 0.67, 0.89, 1.43, 1.33, 0.54, 1.04, 2.99, 6.01, 4.23, 3.95, 2.34, 1.90, 2.21, 1.77, 3.57, 4.84, 4.38, 4.87, 5.40, 6.60, 6.26, 5.78, 6.79, 7.54, 7.07, 8.50, 7.30, 7.50, 6.96, 9.11, 8.80, 8.08, 7.89, 8.43, 9.32, 8.23, 7.85, 8.64, 8.93, 9.03]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Month')
# naming the y axis
plt.ylabel('Overdue Rate')

# giving a title to my graph
plt.title('Trend of Overdue Rate')

# function to show the plot
plt.show()