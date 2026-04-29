import numpy as np
import matplotlib.pyplot as plt
import os,sys
from matplotlib.patches import Ellipse, Patch, Rectangle


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

    cx, cy = 2.0, 1.6
    ae, be = 1.7, 1.05
    x1, x2 = 0.7, 3.55
    y1, y2 = 0.35, 2.55

    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)

    rect = Rectangle((x1, y1), x2 - x1, y2 - y1,
                     facecolor=colors[2],
                     edgecolor=colors[2],
                     alpha=0.16,
                     linewidth=2,
                     label=r"Cell")
    ax.add_patch(rect)

    ellipse = Ellipse((cx, cy), 2 * ae, 2 * be,
                      facecolor=colors[0],
                      edgecolor=colors[0],
                      alpha=0.16,
                      linewidth=2,
                      label=r"Ellipse")
    ax.add_patch(ellipse)

    theta = np.linspace(0, 2 * np.pi, 500)
    ax.plot(cx + ae * np.cos(theta),
            cy + be * np.sin(theta),
            color=colors[0],
            linewidth=2)

    xb = [x1, x1, x2, x2, x1]
    yb = [y1, y2, y2, y1, y1]
    ax.plot(xb, yb, color=colors[2], linewidth=2)

    nx, ny = 320, 320
    xs = np.linspace(x1, x2, nx)
    ys = np.linspace(y1, y2, ny)
    X, Y = np.meshgrid(xs, ys)
    inside = ((X - cx) ** 2 / ae ** 2
              + (Y - cy) ** 2 / be ** 2 <= 1.0)
    ax.contourf(X, Y, inside.astype(float),
                levels=[0.5, 1.5],
                colors=["yellow"],
                alpha=0.89)
    intersection = Patch(facecolor="yellow",
                         edgecolor="none",
                         alpha=0.89,
                         label=r"Intersection")

    ax.plot(cx, cy, ".", color="k", markersize=8)
    ax.text(cx, cy - 0.1, r"$(c_x,c_y)$",
            fontsize=16, ha="center", va="top")

    ax.annotate("",
                xy=(cx + ae, cy),
                xytext=(cx, cy),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))
    ax.text(cx + 0.5 * ae, cy - 0.12,
            r"$a_e$", fontsize=18, ha="center", va="top")

    ax.annotate("",
                xy=(cx, cy + be),
                xytext=(cx, cy),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))
    ax.text(cx + 0.08, cy + 0.5 * be,
            r"$b_e$", fontsize=18, ha="left", va="center")

    ax.plot([x1, x1], [y1-0.3, y2+0.3], "--", color="grey", linewidth=1)
    ax.plot([x2, x2], [y1-0.3, y2+0.3], "--", color="grey", linewidth=1)
    ax.plot([x1-0.3, x2+0.3], [y1, y1], "--", color="grey", linewidth=1)
    ax.plot([x1-0.3, x2+0.3], [y2, y2], "--", color="grey", linewidth=1)

    ax.annotate(r"$x_1$", xy=(x1, y1), xytext=(x1, -0.25),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$x_2$", xy=(x2, y1), xytext=(x2, -0.25),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_1$", xy=(x1, y1), xytext=(x1-0.48, y1),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_2$", xy=(x1, y2), xytext=(x1-0.48, y2),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))

    ax.text((x1+x2)*0.5, -0.08, r"$[x_1,x_2]\times[y_1,y_2]$",
            fontsize=15, ha="center", va="center")
    ax.text((x1+x2)*0.46, 0.95, r"$\Omega_e\cap\Omega_r$",
            fontsize=16, ha="center", va="center")

    handles, labels = ax.get_legend_handles_labels()
    handles.append(intersection)
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.1, 1),
              fontsize=12)

    ax.set_xlim(-0.65, 4.25)
    ax.set_ylim(-0.55, 3.35)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(path + "/ellipse_rectangle_area")


if __name__ == '__main__':
    os.makedirs(DIR_FIG, exist_ok=True)
    plot(DIR_FIG)
