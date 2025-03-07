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
    # print(os.path.abspath(p))
    plt.rc('mathtext', fontset='cm')  # Computer Modern 字体，类似 LaTeX 风格
    plt.rc('font', family='serif')

    cycle = plt.rcParams['axes.prop_cycle']
    colors = [prop['color'] for prop in cycle]

    x = [0, 0, 5, 5, 0]
    y = [0, 5, 5, 0, 0]

    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)

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
    
    #grid
    x = [1, 1, np.nan, 2, 2, np.nan, 3, 3, np.nan, 4,4]
    y = [0, 5, np.nan, 0, 5, np.nan, 0, 5, np.nan, 0,5] 
    ax.plot(x, y, color="k", linewidth=1)
    x2 = [0, 5, np.nan, 0, 5, np.nan, 0, 5, np.nan, 0,5] 
    y2 = [1, 1, np.nan, 2, 2, np.nan, 3, 3, np.nan, 4,4]
    ax.plot(x2, y2, color="k", linewidth=1)
    rectv = Rectangle((1, 1), 1, 1, 
                    facecolor=colors[2], 
                    alpha=0.4, 
                    label=r'Control Volume')
    ax.add_patch(rectv)
    #center point
    xn = [1.5]
    yn = [1.5]
    ax.plot(xn, yn, ".", color="k", linewidth=1)
    plt.annotate(
        "Center",           #
        xy=[xn[0], yn[0]],  # 
        xytext=(2.2, 1.6),  # 
        arrowprops=dict(arrowstyle="->") 
    )
    ax.annotate("$i,j$", [xn[0], yn[0] - 0.1], va="top", ha ="center")
    
    bvx = [1, 1, 2, 2, 1]
    bvy = [1, 2, 2, 1, 1]
    ax.plot(bvx, bvy, label="Control Volume\nBoundary", color=colors[1], linewidth=2)

    ax.set_xlabel(r'$x$', fontsize=16)
    ax.set_ylabel(r'$y$', fontsize=16)

    ax.legend(fontsize=12)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig(path + "/structure_fv")


if __name__ == '__main__':
    plot(DIR_THIS)
    # print("a")