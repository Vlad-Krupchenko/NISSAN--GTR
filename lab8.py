import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Вхідні дані
x = np.array([1.4, 1.6, 2, 2.5, 3.1])
y = np.array([2.39, 3.85, 2.74, 1.58, 3.15])

# Розрахунок кубічних сплайнів
cs = CubicSpline(x, y)

# Значення сплайну у вузлових точках
y_cs = cs(x)

# Побудова графіка сплайну
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Вузли')
plt.plot(x, y_cs, label='Сплайн')
plt.title('Графік кубічного сплайну')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
