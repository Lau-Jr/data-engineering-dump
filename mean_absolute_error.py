# a line equation
# y = 1.2*x + 2
points = ((2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14))
mean_absolute_error = 0
for point in points:
    y_hat = 1.2*point[0]+2
    mean_absolute_error += abs(point[1]-y_hat)
mean_absolute_error /= len(points)
print(mean_absolute_error)
