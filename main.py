import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

koef = [-12, -18, 5, 10, -30]
x_limit = [-1000, 1000]
x = np.arange(x_limit[0], x_limit[1], 0.01)
color = 'r'
x_change = []
x_root = []
func_direct = -1

def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

for i in range(len(x) - 1):
    if func_direct == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            func_direct = 1
            x_change.append((x[i], func(x[i], *koef)))
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            func_direct = -1
            x_change.append((x[i], func(x[i], *koef)))

for i in range(len(x) - 1):
    if (func(x[i], *koef) > 0 and func(x[i+1], *koef) < 0) or (func(x[i], *koef) < 0 and func(x[i+1], *koef) > 0):
        x_root.append((x[i], func(x[i], *koef)))


print(len(x_root))
print(x_root)

x_cur = np.arange(x_limit[0], x_change[0][0], 0.1)
plt.plot(x_cur, func(x_cur, *koef), change_color())
for i in range(len(x_change) - 1):
    x_cur = np.arange(x_change[i][0], x_change[i+1][0], 0.1)
    plt.plot(x_cur, func(x_cur, *koef), change_color())
x_cur = np.arange(x_change[-1][0], x_limit[1], 0.1)
plt.plot(x_cur, func(x_cur, *koef), change_color())

for x_cur in x_root:
    plt.plot(x_cur[0], func(x_cur[0], *koef), 'go')

plt.grid(visible=True)

plt.show()