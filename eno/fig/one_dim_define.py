import matplotlib.pyplot as plt

import numpy as np

from matplotlib import rcParams
# rcParams['mathtext.default'] = 'regular'
rcParams['mathtext.fontset'] = 'cm'
rcParams['font.size']        = 12.0 

def tick_face(plt, ax, xi):
    x = [xi,  xi ]
    y = [0.8, 1.2]
    ax.plot(x,y, color = "k")

def add_text(plt, ax):
    # text face
    h = 0.4
    ax.text(0.5, h, r"$x_{\frac{1}{2}}$", ha="center")
    ax.text(1.5, h, r"$x_{\frac{3}{2}}$", ha="center")
    ax.text(2.5, h, r"$x_{i-\frac{1}{2}}$", ha="center")
    ax.text(3.5, h, r"$x_{i+\frac{1}{2}}$", ha="center")
    ax.text(5.5, h, r"$x_{N-\frac{1}{2}}$", ha="center")
    ax.text(6.5, h, r"$x_{N+\frac{1}{2}}$", ha="center")

    # text center
    h = 0.45
    ax.text(1.0, h, r"$x_{1}$", ha="center")
    ax.text(2.0, h, r"$x_{2}$", ha="center")
    ax.text(3.0, h, r"$x_{i}$", ha="center")
    ax.text(6.0, h, r"$x_{N}$", ha="center")


def add_cell(plt, ax):

    x = [2.5, 2.5]
    y = [1.6, 2.5]
    ax.plot(x,y, color = "k")

    x = [3.5, 3.5]
    y = [1.6, 2.5]
    ax.plot(x,y, color = "k")

    x = [2.5, 3.5]
    y = [2.1, 2.1]
    ax.plot(x,y, color = "k")

    ax.text(3.0, 2.3, r"$I_{i}$", ha="center")

def add_deltax(plt, ax):

    x = [ 2.5, 2.5]
    y = [-0.6, 0.0]
    ax.plot(x,y, color = "k")

    x = [3.5, 3.5]
    y = [-0.6, 0.0]
    ax.plot(x,y, color = "k")

    x = [2.5, 3.5]
    y = [-.3, -.3]
    ax.plot(x,y, color = "k")

    ax.text(3.0, -.8, r"$\Delta x_i$", ha="center")


def main():
    # matplot size in inches
    # beamer default size 128mm x 96mm
    # 1mm = 0.0393 inch
    fw = 128 * 0.0393 # inch
    fh = 96 * 0.0393  # inch
    fig, ax = plt.subplots(figsize=[fw * 0.9 , fh * 0.4])

    arrdot_x  = [1,2,3,5,6]
    arrdot_y1 = [1,1,1,1,1]
    arrface   = [0.5, 1.5, 2.5, 3.5, 5.5, 6.5]
    for f in arrface:
        tick_face(plt, ax, f)

    dot,    = ax.plot(arrdot_x, arrdot_y1, ".", markersize=10, color = "k")

    cutx1 = 3.7
    cutx2 = 4.8
    # first solid line ==== 
    l1x = [0.5, cutx1]
    l1y = [1.0, 1.0]
    l1,     = ax.plot(l1x, l1y, color = "k")

    # second solid line ==== 
    l2x = [cutx2, 6.5]
    l2y = [1.0, 1.0]
    l2,     = ax.plot(l2x, l2y, color = "k")

    # second solid line ==== 
    l3x = [cutx1, cutx2]
    l3y = [1.0, 1.0]
    l3,     = ax.plot(l3x, l3y, "--", color = "k")

    # a and b
    ax.text(0.5, 1.4, r"$a$", ha="center")
    ax.text(6.5, 1.4, r"$b$", ha="center")

    add_text(plt, ax)

    add_cell(plt, ax)

    add_deltax(plt, ax)

    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.set_ylim([-1.5, 3.5])
    plt.axis('off')
    plt.tight_layout(0.1)

    plt.savefig("one_dim_define.pdf")


if __name__ == '__main__':
    main()

