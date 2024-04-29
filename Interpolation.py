import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(x, y, x_new):
    n = len(x)
    f = np.zeros_like(x_new)

    for k in range(n):
        f_k = y[k]
        for j in range(k):
            f_k = f_k * (x_new - x[j]) / (x[k] - x[j])
        f += f_k

    return f

def function(x):
    return np.sin(x)  # Пример функции f(x) = sin(x)

# Ввод границ отрезка пользователем
def input_bounds():
    bounds = input("Введите границы отрезка [a, b] через запятую: ")
    a, b = map(float, bounds.split(','))
    return a, b

# Ввод границ отрезка
a, b = input_bounds()

# Узлы интерполяции
n = 4  # Количество узлов для интерполяции
x_interp = np.linspace(a, b, n)

# Значения функции в узлах интерполяции
y_interp = function(x_interp)

# Область для интерполяции
x_new = np.linspace(a, b, 1000)

# Интерполяция
y_new = newton_interpolation(x_interp, y_interp, x_new)

# Построение графика
plt.plot(x_new, y_new, label='Интерполяционный многочлен Ньютона')
plt.plot(x_interp, y_interp, 'o', label='Узлы интерполяции')
plt.legend()
plt.grid()
plt.show()
