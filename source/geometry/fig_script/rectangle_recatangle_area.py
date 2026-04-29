import numpy as np
import matplotlib.pyplot as plt
import os,sys
from matplotlib.patches import Patch, Rectangle


DIR_CASE     = os.path.abspath(os.path.join(__file__, "../.."))
DIR_THIS     = os.path.abspath(os.path.join(__file__, "../"))
DIR_FIG      = os.path.abspath(os.path.join(DIR_CASE, "fig"))
DIR_SOURCE   = os.path.abspath(os.path.join(DIR_CASE, "../"))
DIR_PYSCRIPT = os.path.abspath(os.path.join(DIR_SOURCE, "_scripts"))

sys.path.append(DIR_PYSCRIPT)
from env_para import *

plt.style.use(os.path.join(DIR_PYSCRIPT, "web.mplstyle"))


def plot(path):
    plt.rc('mathtext', fontset='cm')
    plt.rc('font', family='serif')

    cycle = plt.rcParams['axes.prop_cycle']
    colors = [prop['color'] for prop in cycle]

    x1, x2 = 0.4, 3.0
    y1, y2 = 0.45, 2.45
    u1, u2 = 1.55, 4.0
    v1, v2 = 1.25, 3.15

    xL, xR = max(x1, u1), min(x2, u2)
    yB, yT = max(y1, v1), min(y2, v2)

    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)

    rect1 = Rectangle((x1, y1), x2 - x1, y2 - y1,
                      facecolor=colors[2],
                      edgecolor=colors[2],
                      alpha=0.16,
                      linewidth=2,
                      label="Rectangle " + r"$R_1$")
    ax.add_patch(rect1)

    rect2 = Rectangle((u1, v1), u2 - u1, v2 - v1,
                      facecolor=colors[0],
                      edgecolor=colors[0],
                      alpha=0.16,
                      linewidth=2,
                      label="Rectangle " + r"$R_2$")
    ax.add_patch(rect2)

    intersection = Rectangle((xL, yB), xR - xL, yT - yB,
                             facecolor="yellow",
                             edgecolor="none",
                             alpha=0.89)
    ax.add_patch(intersection)
    intersection_handle = Patch(facecolor="yellow",
                                edgecolor="none",
                                alpha=0.89,
                                label=r"Intersection")

    xb1 = [x1, x1, x2, x2, x1]
    yb1 = [y1, y2, y2, y1, y1]
    ax.plot(xb1, yb1, color=colors[2], linewidth=2)

    xb2 = [u1, u1, u2, u2, u1]
    yb2 = [v1, v2, v2, v1, v1]
    ax.plot(xb2, yb2, color=colors[0], linewidth=2)

    ax.plot([xL, xL, xR, xR, xL],
            [yB, yT, yT, yB, yB],
            color="goldenrod", linewidth=2)

    for x in [x1, x2, u1, u2, xL, xR]:
        ax.plot([x, x], [0.05, 3.45], "--", color="grey",
                linewidth=0.9, alpha=0.65)
    for y in [y1, y2, v1, v2, yB, yT]:
        ax.plot([0.05, 4.35], [y, y], "--", color="grey",
                linewidth=0.9, alpha=0.65)

    ax.annotate(r"$x_1$", xy=(x1, y1), xytext=(x1, -0.28),
                fontsize=15, ha="center", color=colors[2],
                arrowprops=dict(arrowstyle="->", color=colors[2]))
    ax.annotate(r"$x_2$", xy=(x2, y1), xytext=(x2, -0.28),
                fontsize=15, ha="center", color=colors[2],
                arrowprops=dict(arrowstyle="->", color=colors[2]))
    ax.annotate(r"$u_1$", xy=(u1, v1), xytext=(u1, -0.28),
                fontsize=15, ha="center", color=colors[0],
                arrowprops=dict(arrowstyle="->", color=colors[0]))
    ax.annotate(r"$u_2$", xy=(u2, v1), xytext=(u2, -0.28),
                fontsize=15, ha="center", color=colors[0],
                arrowprops=dict(arrowstyle="->", color=colors[0]))

    ax.annotate(r"$y_1$", xy=(x1, y1), xytext=(-0.2, y1),
                fontsize=15, va="center", color=colors[2],
                arrowprops=dict(arrowstyle="->", color=colors[2]))
    ax.annotate(r"$y_2$", xy=(x1, y2), xytext=(-0.2, y2),
                fontsize=15, va="center", color=colors[2],
                arrowprops=dict(arrowstyle="->", color=colors[2]))
    ax.annotate(r"$v_1$", xy=(u1, v1), xytext=(-0.2, v1),
                fontsize=15, va="center", color=colors[0],
                arrowprops=dict(arrowstyle="->", color=colors[0]))
    ax.annotate(r"$v_2$", xy=(u1, v2), xytext=(-0.2, v2),
                fontsize=15, va="center", color=colors[0],
                arrowprops=dict(arrowstyle="->", color=colors[0]))

    ax.annotate("",
                xy=(xR, yT + 0.22),
                xytext=(xL, yT + 0.22),
                arrowprops=dict(arrowstyle="<->", linewidth=1.4))
    ax.text((xL + xR) * 0.5, yT + 0.30, r"$w$",
            fontsize=18, ha="center", va="bottom")

    ax.annotate("",
                xy=(xR + 0.22, yT),
                xytext=(xR + 0.22, yB),
                arrowprops=dict(arrowstyle="<->", linewidth=1.4))
    ax.text(xR + 0.30, (yB + yT) * 0.5, r"$h$",
            fontsize=18, ha="left", va="center")

    ax.text((x1 + x2) * 0.5, y1 + 0.25, r"$R_1$",
            fontsize=18, ha="center", va="center", color=colors[2])
    ax.text((u1 + u2) * 0.5 + 0.45, v2 - 0.25, r"$R_2$",
            fontsize=18, ha="center", va="center", color=colors[0])
    ax.text((xL + xR) * 0.5, (yB + yT) * 0.5,
            r"$R_1\cap R_2$",
            fontsize=16, ha="center", va="center")

    handles, labels = ax.get_legend_handles_labels()
    handles.append(intersection_handle)
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.18, 0.9),
              fontsize=12)

    ax.set_xlim(-1, 4.45)
    ax.set_ylim(-0.75, 3.65)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(path + "/rectangle_recatangle_area")


if __name__ == '__main__':
    os.makedirs(DIR_FIG, exist_ok=True)
    plot(DIR_FIG)
