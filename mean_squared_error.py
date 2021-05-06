from math import pow
# a line equation
# y = 1.2*x + 2
points = ((2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14))
mean_squared_error = 0
for point in points:
    y_hat = 1.2*point[0]+2
    mean_squared_error += pow(point[1]-y_hat, 2)
mean_squared_error /= len(points)
print(mean_squared_error)
