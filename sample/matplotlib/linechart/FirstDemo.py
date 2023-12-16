import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/
# https://matplotlib.org/stable/plot_types/index.html
# https://matplotlib.org/cheatsheets/

# 单个图
def draw_line_chart():
    # 画布：
    # figsize 画布大小
    # dpi       分辨率
    # facecolor 背景色
    plt.figure(figsize=(10, 8), dpi=100, facecolor='gray')

    x = np.linspace(0, 2 * np.pi, 100)

    # color     颜色    
    # linestyle 线样式
    # label     标签
    plt.plot(x, np.sin(x), color='r', linestyle='-.', label='y=sin(x)')
    plt.plot(x, np.cos(x), color='g', linestyle='--', label='y=cos(x)')
    plt.plot(x, -np.sin(x), color='orange', linestyle='-.', label='y=-sin(x)')
    plt.plot(x, -np.cos(x), color='b', linestyle='--', label='y=-cos(x)')
    
    # 网格
    plt.grid()
    
    # 显示图
    plt.show()

# 多图示例
def draw_multi_line_chart():
    # 画布：
    # figsize 画布大小
    # dpi       分辨率
    # facecolor 背景色
    fig = plt.figure(figsize=(10, 8), dpi=100, facecolor='gray')

    x = np.linspace(0, 2 * np.pi, 100)

    # color     颜色    
    # linestyle 线样式
    # label     标签
    
    # 2行2列第1个图
    axes1 = plt.subplot(2, 2, 1)
    axes1.plot(x, np.sin(x), color='r', linestyle='-.')
    axes1.set_label('子图1: y=sin(x)')
    axes1.set_xlabel("t(time/s)")
    axes1.set_ylabel("v(v/opt)")
    
    # 2行2列第2个图
    axes2 = plt.subplot(2, 2, 2)
    axes2.plot(x, np.cos(x), color='g', linestyle='--')
    axes2.set_label('子图2: y=cos(x)')
    axes2.set_xlabel("t(time/s)", color='b')
    axes2.set_ylabel("v(v/opt)")
    
    
    # 2行2列第3个图
    axes3 = plt.subplot(2, 2, 3)
    axes3.plot(x, -np.sin(x), color='orange', linestyle='-.')
    axes3.set_label('子图3: y=-sin(x)')
    axes3.set_xlabel("t(time/s)")
    axes3.set_ylabel("v(v/opt)")
    
    # 2行2列第4个图
    axes4 = plt.subplot(2, 2, 4)
    axes4.plot(x, -np.cos(x), color='b', linestyle='--')
    axes4.set_label('子图4: y=-cos(x)')
    axes4.set_xlabel("t(time/s)")
    axes4.set_ylabel("v(v/opt)")

    
    # 网格
    plt.grid()
    
    # 自动调整布局
    fig.tight_layout()
    
    # 显示图
    plt.show()

if __name__ == '__main__':
    draw_multi_line_chart()