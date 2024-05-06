import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465])
yi = np.array([0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986])
x_values = [1.416, 1.431, 1.422, 1.416, 1.456, 1.462, 1.451]
def calculate_differences(y_values):
    differences = [y_values]
    n = len(y_values)
    for i in range(1, n):
        differences.append(np.diff(differences[-1]))
    return differences
def newton_coefficients(xi, yi):
    differences = calculate_differences(yi)
    coefficients = [differences[0][0]]
    n = len(xi)
    for i in range(1, n):
        coefficients.append(differences[i][0] / np.math.factorial(i))
    return coefficients
def interpolate_newton_polynomial(xi, coefficients, x_values):
    result = []
    for x in x_values:
        y = coefficients[0]
        for i in range(1, len(coefficients)):
            term = coefficients[i]
            for j in range(i):
                term *= (x - xi[j])
            y += term
        result.append(y)
    return result
coefficients = newton_coefficients(xi, yi)
interpolated_values = interpolate_newton_polynomial(xi, coefficients, x_values)
plt.figure(figsize=(10, 6))
plt.plot(xi, yi, 'bo', label='Дані')
plt.plot(x_values, interpolated_values, 'r-', label='Інтерполяційна функція')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Інтерполяція функції за допомогою багаточлена Ньютона')
plt.legend()
plt.grid(True)
plt.show()