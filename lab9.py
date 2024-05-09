import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 * np.sin(2*x)
def taylor_approximation(x):
    return x**2
x_values = np.linspace(-2, 2, 400)
y_f = f(x_values)
y_taylor = taylor_approximation(x_values)
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_f, label='f(x) = x^2 * sin(2x)', color='blue')
plt.plot(x_values, y_taylor, label='Тейлор (другий порядок)', linestyle='--', color='red')
plt.title('Графік функції та наближення поліномом Тейлора')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()