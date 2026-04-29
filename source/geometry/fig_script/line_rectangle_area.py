import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Polygon, Rectangle


DIR_CASE = os.path.abspath(os.path.join(__file__, "../.."))
DIR_THIS = os.path.abspath(os.path.join(__file__, "../"))
DIR_FIG = os.path.abspath(os.path.join(DIR_CASE, "fig"))
DIR_SOURCE = os.path.abspath(os.path.join(DIR_CASE, "../"))
DIR_PYSCRIPT = os.path.abspath(os.path.join(DIR_SOURCE, "_scripts"))

sys.path.append(DIR_PYSCRIPT)
from env_para import *

plt.style.use(os.path.join(DIR_PYSCRIPT, "web.mplstyle"))


def phi(point, a, b, c):
    x, y = point
    return a * x + b * y + c


def clip_polygon_positive(points, a, b, c):
    clipped = []

    for i, p_i in enumerate(points):
        p_j = points[(i + 1) % len(points)]
        phi_i = phi(p_i, a, b, c)
        phi_j = phi(p_j, a, b, c)
        inside_i = phi_i >= 0.0
        inside_j = phi_j >= 0.0

        if inside_i and inside_j:
            clipped.append(p_j)
        elif inside_i and not inside_j:
            t = phi_i / (phi_i - phi_j)
            clipped.append(p_i + t * (p_j - p_i))
        elif not inside_i and inside_j:
            t = phi_i / (phi_i - phi_j)
            clipped.append(p_i + t * (p_j - p_i))
            clipped.append(p_j)

    return np.array(clipped)


def plot(path):
    plt.rc("mathtext", fontset="cm")
    plt.rc("font", family="serif")

    cycle = plt.rcParams["axes.prop_cycle"]
    colors = [prop["color"] for prop in cycle]

    x1, x2 = 0.7, 3.7
    y1, y2 = 0.3, 2.55
    a, b, c = -0.75, 1.0, -0.15

    rect_points = np.array([
        [x1, y1],
        [x2, y1],
        [x2, y2],
        [x1, y2],
    ])
    positive_poly = clip_polygon_positive(rect_points, a, b, c)

    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)

    rect = Rectangle((x1, y1), x2 - x1, y2 - y1,
                     facecolor="none",
                     edgecolor=colors[2],
                     alpha=0.00,
                     linewidth=2,
                     label=r"Rectangle")
    ax.add_patch(rect)

    negative_patch = Rectangle((x1, y1), x2 - x1, y2 - y1,
                               facecolor=colors[1],
                               edgecolor="none",
                               alpha=0.3)
    ax.add_patch(negative_patch)

    positive_patch = Polygon(positive_poly,
                             closed=True,
                             facecolor=colors[0],
                             edgecolor="none",
                             alpha=0.3)
    ax.add_patch(positive_patch)

    xb = [x1, x2, x2, x1, x1]
    yb = [y1, y1, y2, y2, y1]
    ax.plot(xb, yb, color=colors[2], linewidth=2)

    xs = np.linspace(x1 - 0.45, x2 + 0.45, 200)
    ys = -(a * xs + c) / b
    ax.plot(xs, ys, color="k", linewidth=2.2, label=r"$\phi=0$")

    intersections = []
    for i, p_i in enumerate(rect_points):
        p_j = rect_points[(i + 1) % len(rect_points)]
        phi_i = phi(p_i, a, b, c)
        phi_j = phi(p_j, a, b, c)
        if phi_i * phi_j < 0.0:
            t = phi_i / (phi_i - phi_j)
            intersections.append(p_i + t * (p_j - p_i))

    if intersections:
        intersections = np.array(intersections)
        ax.plot(intersections[:, 0], intersections[:, 1],
                "o", color="k", markersize=5, label=r"Intersections")
        for index, point in enumerate(intersections, start=1):
            dx = 0.09 if index == 1 else -0.12
            dy = -0.16 if index == 1 else 0.14
            ax.text(point[0] + dx, point[1] + dy,
                    rf"$I_{index}$", fontsize=15,
                    ha="center", va="center")

    ax.plot([x1, x1], [y1 - 0.3, y2 + 0.3], "--", color="grey", linewidth=1)
    ax.plot([x2, x2], [y1 - 0.3, y2 + 0.3], "--", color="grey", linewidth=1)
    ax.plot([x1 - 0.3, x2 + 0.3], [y1, y1], "--", color="grey", linewidth=1)
    ax.plot([x1 - 0.3, x2 + 0.3], [y2, y2], "--", color="grey", linewidth=1)

    ax.annotate(r"$x_1$", xy=(x1, y1), xytext=(x1, -0.25),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$x_2$", xy=(x2, y1), xytext=(x2, -0.25),
                fontsize=16, ha="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_1$", xy=(x1, y1), xytext=(x1 - 0.5, y1),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"$y_2$", xy=(x1, y2), xytext=(x1 - 0.5, y2),
                fontsize=16, va="center",
                arrowprops=dict(arrowstyle="->"))

    ax.text((x1 + x2) * 0.5, -0.10,
            r"$[x_1,x_2]\times[y_1,y_2]$",
            fontsize=15, ha="center", va="center")
    ax.text(1.35, 2.15, r"$R\cap\Omega^+$",
            fontsize=17, color=colors[0], ha="center", va="center")
    ax.text(2.55, 0.75, r"$R\cap\Omega^-$",
            fontsize=17, color=colors[1], ha="center", va="center")
    ax.text(2.35, 1.25, r"$\phi(x,y)=a x+b y+c$",
            fontsize=15, rotation=36, ha="center", va="bottom")

    handles = [
        Patch(facecolor=colors[0], alpha=0.3, label=r"$R\cap\Omega^+$"),
        Patch(facecolor=colors[1], alpha=0.3, label=r"$R\cap\Omega^-$"),
        Patch(facecolor=colors[2], edgecolor=colors[2], alpha=0.10, label=r"Rectangle"),
        Line2D([0], [0], color="k", linewidth=2.2, label="Line " + r"$\phi=0$"),
        Line2D([0], [0], marker="o", color="k", linestyle="none",
               markersize=5, label=r"Intersections"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.1, 0.7),
              fontsize=12)

    ax.set_xlim(-0.65, 4.35)
    ax.set_ylim(-0.55, 3.35)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(os.path.join(path, "line_rectangle_area.png"))


if __name__ == "__main__":
    os.makedirs(DIR_FIG, exist_ok=True)
    plot(DIR_FIG)
