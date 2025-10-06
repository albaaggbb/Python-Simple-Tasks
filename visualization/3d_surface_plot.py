# visualization/3d_surface_plot.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_3d_surface(output_file=None):
    """
    Plots the 3D surface of the function f(x, y) = cos(x) + 2*sin(y)
    over a grid in the range [-π, π] for both x and y.
    
    Parameters:
    - output_file: if provided, saves the plot to a file.
    """
    # Grid for x and y
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.arange(-np.pi, np.pi, 0.1)
    x, y = np.meshgrid(x, y)
    
    # Function
    f = np.cos(x) + 2 * np.sin(y)
    
    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, f, vmin=f.min(), cmap=cm.RdBu)
    
    # Labels and title
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("f(x, y)")
    ax.set_title("3D Surface Plot: f(x, y) = cos(x) + 2*sin(y)")
    
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    
    if output_file:
        plt.savefig(output_file)
        print(f"3D surface plot saved to {output_file}")
    else:
        plt.show()


if __name__ == "__main__":
    plot_3d_surface()
