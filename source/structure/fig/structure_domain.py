import numpy as np
import matplotlib.pyplot as plt
import os,sys
from matplotlib.patches import Rectangle


DIR_CASE     = os.path.abspath(os.path.join(__file__, "../.."))
DIR_THIS     = os.path.abspath(os.path.join(__file__, "../"))
DIR_SOURCE   = os.path.abspath(os.path.join(DIR_CASE, "../"))
DIR_PYSCRIPT = os.path.abspath(os.path.join(DIR_SOURCE, "py_script"))

sys.path.append(DIR_PYSCRIPT)
from env_para import *


def plot(path):
    print(path)
    # print(os.path.abspath(p))
    plt.rc('mathtext', fontset='cm')  # Computer Modern 字体，类似 LaTeX 风格
    plt.rc('font', family='serif')

    cycle = plt.rcParams['axes.prop_cycle']
    colors = [prop['color'] for prop in cycle]

        # 生成数据
    x = [0, 0, 5, 5, 0]
    y = [0, 5, 5, 0, 0]

    # 创建图形
    fig, ax = plt.subplots(figsize=(6, 6), dpi=300)

    # 绘制正弦曲线
    ax.plot(x, y, label=r'Boundary', color=colors[0], linewidth=2)
    rect = Rectangle((0, 0), 5, 5, 
                    facecolor=colors[0], 
                    alpha=0.2, 
                    label=r'Domain')
    ax.add_patch(rect)
    # mathbb
    # mathcal
    # mathscr
    ax.text(2.5, 2.5, r'$\mathbb{Z}^2$', 
            fontsize=16, color='black', ha='center', va='bottom')
    ax.plot([1.7, 2], [5, 5.2], color="k", linewidth=1)
    ax.text(2., 5.2, r'$\Gamma$', 
        fontsize=16, color='black', ha='left', va='bottom')


        # ax.set_title(r'The Sine Function: $y = \sin(x)$', fontsize=16, pad=10)
    ax.set_xlabel(r'$x$', fontsize=16)
    ax.set_ylabel(r'$y$', fontsize=16)

    # ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=12)

    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig(path + "/structure_domain")

# plot(DIR_CASE+"/fig")

if __name__ == '__main__':
    plot(DIR_THIS)
    # print("a")