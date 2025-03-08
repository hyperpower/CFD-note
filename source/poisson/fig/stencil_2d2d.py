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


    fig, ax = plt.subplots(figsize=(7.5, 5), dpi=300)
    # backgroud mesh
    xb = [0, 0, np.nan, -2, 2, np.nan,-2,  2, np.nan,-2,  2, np.nan,1,  1,  np.nan,-1,-1]
    yb = [-2,2, np.nan,  0, 0, np.nan,-1, -1, np.nan, 1,  1, np.nan,-2,  2, np.nan,-2, 2]
    ax.plot(xb, yb, color="lightgrey", linewidth=2, label=r"Mesh") 
    #points
    xn = [0,0, 0, 1, -1]
    yn = [0,1,-1,0, 0]
    ax.plot(xn, yn, "D", color="k", linewidth=1, label="Points")
    #link lines
    xn = [0, 0, np.nan, -1, 1]
    yn = [-1,1, np.nan,  0, 0]
    ax.plot(xn, yn, color="k", linewidth=2)
    # text
    ax.text(0.02, -0.02, r'$i,j$', 
            fontsize=16, color='black', ha='left', va='top')
    ax.text(1.02, -0.02, r'$i+1,j$', 
            fontsize=16, color='black', ha='left', va='top')
    ax.text(-0.98, -0.02, r'$i-1,j$', 
            fontsize=16, color='black', ha='left', va='top')
    ax.text(0.02, 0.98, r'$i,j+1$', 
            fontsize=16, color='black', ha='left', va='top')
    ax.text(0.02, -1.02, r'$i,j-1$', 
            fontsize=16, color='black', ha='left', va='top')

    # stencil value
    ax.text(-0.02, 0.02, r'-4',weight='bold', 
            fontsize=20, color='black', ha='right', va='bottom')
    ax.text(0.98,  0.02, r'1',weight='bold',  
            fontsize=20, color='black', ha='right', va='bottom')
    ax.text(-1.02, 0.02, r'1',weight='bold',  
            fontsize=20, color='black', ha='right', va='bottom')
    ax.text(-0.02, 1.02,  r'1',weight='bold',  
            fontsize=20, color='black', ha='right', va='bottom')
    ax.text(-0.02, -0.98, r'1',weight='bold',  
            fontsize=20, color='black', ha='right', va='bottom')
    
    ax.text(-1.1, 0.2, r'$\frac{1}{h^2} \times$', weight='bold',
            fontsize=24, color='black', ha='right', va='bottom')
    
    # corrdinate
    ax.arrow(-0.75, -0.75, 0.3, 0.0, width = 0.01,fc ="k") 
    ax.arrow(-0.75, -0.75, 0.0, 0.3, width = 0.01,fc ="k") 
    ax.text(-0.45, -0.75, r'$x$', 
             fontsize=16, color='black', ha='right', va='bottom')
    ax.text(-0.76, -0.45, r'$y$', 
             fontsize=16, color='black', ha='right', va='bottom')
    plt.axis('off') 

    # ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=12)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig(path + "/stencil_2d2d")

# plot(DIR_CASE+"/fig")

if __name__ == '__main__':
    plot(DIR_THIS)
    # print("a")