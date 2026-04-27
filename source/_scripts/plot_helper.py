import math
from env_para import *

def plot_coordinate_2d(
    ax,
    origin=(-0.75, -0.75),
    length=0.3,
    width=0.01,
    x_color=COLOR_BLUE,
    y_color=COLOR_RED,
    fontsize=16,
):
    x0, y0 = origin
    ax.arrow(x0, y0, length, 0.0, width=width, color=x_color)
    ax.arrow(x0, y0, 0.0, length, width=width, color=y_color)
    ax.text(
        x0 + length,
        y0,
        r"$x$",
        fontsize=fontsize,
        color=x_color,
        ha="right",
        va="bottom",
    )
    ax.text(
        x0 - 0.01,
        y0 + length,
        r"$y$",
        fontsize=fontsize,
        color=y_color,
        ha="right",
        va="bottom",
    )


def plot_coordinate_3d_projected(
    ax,
    origin=(-0.45, 0.55),
    length=0.3,
    z_axis=(-0.9, -0.8),
    width=0.01,
    x_color=COLOR_BLUE,
    y_color=COLOR_RED,
    z_color=COLOR_GREEN,
    fontsize=16,
):
    x0, y0 = origin
    zx, zy = z_axis
    z_len = math.sqrt(zx * zx + zy * zy)

    ax.arrow(x0, y0, length, 0.0, width=width, color=x_color)
    ax.arrow(x0, y0, 0.0, length, width=width, color=y_color)
    ax.arrow(x0, y0, length * zx / z_len, length * zy / z_len, width=width, color=z_color)

    ax.text(
        x0 + length,
        y0,
        r"$x$",
        fontsize=fontsize,
        color=x_color,
        ha="right",
        va="bottom",
    )
    ax.text(
        x0 - 0.01,
        y0 + length,
        r"$y$",
        fontsize=fontsize,
        color=y_color,
        ha="right",
        va="bottom",
    )
    ax.text(
        x0 + 0.3 * length * zx / z_len,
        y0 + 1.1 * length * zy / z_len,
        r"$z$",
        fontsize=fontsize,
        color=z_color,
        ha="right",
        va="bottom",
    )


def sub(p1, p0):
    p = [p1[0]-p0[0],
         p1[1]-p0[1],
         p1[2]-p0[2]]
    return p

def mid(p1, p0):
    p = [(p1[0]+p0[0])*0.5,
         (p1[1]+p0[1])*0.5,
         (p1[2]+p0[2])*0.5]
    return p

def to_xyz(p0, p1, p2):
    res = [
      [p0[0], p1[0], p2[0]], #x
      [p0[1], p1[1], p2[1]], #y
      [p0[2], p1[2], p2[2]], #z
    ]
    return res
