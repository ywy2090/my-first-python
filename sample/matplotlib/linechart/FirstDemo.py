import matplotlib.pyplot as plt
import numpy as np

def draw_line_chart():
    plt.rcParams['font.family'] = 'SimHei'
    # plt.rcParams['font.size'] = 20

    x = np.linspace(0, 2 * np.pi, 200)
    print(x)
    y = x**2

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    draw_line_chart()