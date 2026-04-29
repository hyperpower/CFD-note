import numpy as np
import matplotlib.pyplot as plt
import os,sys
from matplotlib.patches import Circle, Patch, Rectangle


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

    cx, cy = 2.0, 1.7
    radius = 1.4
    x1, x2 = 0.8, 3.6
    y1, y2 = 0.2, 2.6

    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)

    rect = Rectangle((x1, y1), x2 - x1, y2 - y1,
                     facecolor=colors[2],
                     edgecolor=colors[2],
                     alpha=0.16,
                     linewidth=2,
                     label=r"Cell")
    ax.add_patch(rect)

    circle = Circle((cx, cy), radius,
                    facecolor=colors[0],
                    edgecolor=colors[0],
                    alpha=0.16,
                    linewidth=2,
                    label=r"Circle")
    ax.add_patch(circle)

    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(cx + radius * np.cos(theta),
            cy + radius * np.sin(theta),
            color=colors[0],
            linewidth=2)

    xb = [x1, x1, x2, x2, x1]
    yb = [y1, y2, y2, y1, y1]
    ax.plot(xb, yb, color=colors[2], linewidth=2)

    nx, ny = 300, 300
    xs = np.linspace(x1, x2, nx)
    ys = np.linspace(y1, y2, ny)
    X, Y = np.meshgrid(xs, ys)
    inside = (X - cx) ** 2 + (Y - cy) ** 2 <= radius ** 2
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

    angle = np.deg2rad(30)
    xr = cx + radius * np.cos(angle)
    yr = cy + radius * np.sin(angle)
    ax.annotate("",
                xy=(xr, yr),
                xytext=(cx, cy),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))
    ax.text((cx + xr) * 0.5 + 0.10, (cy + yr) * 0.5 - 0.08,
            r"$R$", fontsize=18, ha="left", va="top")

    ax.plot([x1, x1], [y1-0.3, y2+0.3], "--", color="grey", linewidth=1)
    ax.plot([x2, x2], [y1-0.3, y2+0.3], "--", color="grey", linewidth=1)
    ax.plot([x1-0.3, x2+0.3], [y1, y1], "--", color="grey", linewidth=1)
    ax.plot([x1-0.3, x2+0.3], [y2, y2], "--", color="grey", linewidth=1)

    ax.annotate(r"$x_1$", xy=(x1, y1), xytext=(x1, -0.3),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$x_2$", xy=(x2, y1), xytext=(x2, -0.3),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_1$", xy=(x1, y1), xytext=(x1-0.5, y1),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_2$", xy=(x1, y2), xytext=(x1-0.5, y2),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))

    ax.text((x1+x2)*0.5, -0.15, r"$[x_1,x_2]\times[y_1,y_2]$",
            fontsize=15, ha="center", va="center")
    ax.text((x1+x2)*0.45, 0.75, r"$\Omega_c\cap\Omega_r$",
            fontsize=16, ha="center", va="center")

    handles, labels = ax.get_legend_handles_labels()
    handles.append(intersection)
    ax.legend(handles=handles, fontsize=12)
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.1, 1))

    ax.set_xlim(-0.7, 4.3)
    ax.set_ylim(-0.7, 3.7)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(path + "/circle_rectangle_area")


if __name__ == '__main__':
    os.makedirs(DIR_FIG, exist_ok=True)
    plot(DIR_FIG)
