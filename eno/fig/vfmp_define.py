import matplotlib.pyplot as plt
from cycler import cycler

import numpy as np
from scipy import interpolate

from matplotlib import rcParams
# rcParams['mathtext.default'] = 'regular'
rcParams['mathtext.fontset'] = 'cm'
rcParams['font.size']        = 12.0 
#                    red        blue       green      yellow
cc = (cycler(color=["#EA4235", "#4385F5", "#34A853", "#FCBC05"]))
rcParams['axes.prop_cycle']  = cc

def tick_face(plt, ax, xi):
    x = [xi,  xi ]
    y = [-0.2, 0.2]
    ax.plot(x,y, color = "k")

def add_curve(plt, ax, arrx, arry):
    x    = arrx
    y    = arry
    tck  = interpolate.splrep(x, y, s=0)
    xnew = np.arange(0, 2, 0.05)
    ynew = interpolate.splev(xnew, tck, der=0)
    plt.plot(xnew, ynew, "-")
    return xnew, ynew

def add_text(plt, ax):
    ax.text(1.0, -.5, r"$x_i$", ha="center")

    ax.text(0.5, -.7, r"$x_{i-\frac{1}{2}}$", ha="center")
    ax.text(1.5, -.7, r"$x_{i+\frac{1}{2}}$", ha="center")


def main():
    # matplot size in inches
    # beamer default size 128mm x 96mm
    # 1mm = 0.0393 inch
    fw = 128 * 0.0393 # inch
    fh = 96 * 0.0393  # inch
    fig, ax = plt.subplots(figsize=[fw * 0.8 , fh * 0.4])

    arrdot_x  = [1]
    arrdot_y1 = [0]
    arrface   = [0.5,1.5]
    for f in arrface:
        tick_face(plt, ax, f)

    dot,    = ax.plot(arrdot_x, arrdot_y1, ".", markersize=10, color = "k")

    # first solid line ==== 
    l1x = [0.2, 1.7]
    l1y = [0.0, 0.0]
    l1,     = ax.plot(l1x, l1y, color = "k")

    # second dash line ==== 
    l2x = [-0.2, 0.2]
    l2y = [0.0, 0.0]
    l2,     = ax.plot(l2x, l2y, "--", color = "k")

    # second dash line ==== 
    l3x = [1.7, 2.0]
    l3y = [0.0, 0.0]
    l3,     = ax.plot(l3x, l3y, "--", color = "k")
    # curve v(x)
    arrx = [0.0, 0.5, 1.0, 1.5, 2.0]
    arry = [1.0, 1.5, 1.8, 2.3, 3.1]
    add_curve(plt, ax, arrx, arry)
    ax.text(0.0, 1.3, r"$v(x)$", ha="center", color = "C0")

    # average fill
    avg = 1.7
    x = [0.5, 1.5, 1.5, 0.5, 0.5]
    y = [0.0, 0.0, avg, avg, 0.0]
    
    ax.plot([0.5, 0.5], [0.2, 2.5], "--", color = "k",  lw=1)
    ax.plot([1.5, 1.5], [0.2, 2.5], "--", color = "k",  lw=1)

    ax.annotate(r'$v^{+}_{x_{i-\frac{1}{2}}}$', xy=(0.5, 1.5), xytext=(0.9, 0.8),
            arrowprops=dict(facecolor='black', headlength = 5, headwidth=4, width=0.1, shrink=0.05), 
            horizontalalignment='right', va='center')

    ax.annotate(r'$v^{-}_{x_{i+\frac{1}{2}}}$', xy=(1.5, 2.3), xytext=(1.3, 0.8),
            arrowprops=dict(facecolor='black', headlength = 5, headwidth=4, width=0.1, shrink=0.05), 
            horizontalalignment='right', va='center')

    add_text(plt, ax)

    # add_deltax(plt, ax)

    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.set_ylim([-1.5, 3.5])
    plt.axis('off')
    plt.tight_layout(0.1)

    plt.savefig("vfmp_define.pdf")


if __name__ == '__main__':
    main()

