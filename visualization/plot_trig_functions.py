import numpy as np
import matplotlib.pyplot as plt

def plot_trig_functions(output_file=None):
    """
    Plots arcsin(x) and arccos(x) over the interval [-1, 1] in radians.
    Can display the plot or save it to a file.
    """
    # Domain valid for arcsin and arccos
    x = np.linspace(-1, 1, 400)

    plt.plot(x, np.arcsin(x), 'r', label='arcsin(x)')
    plt.plot(x, np.arccos(x), 'g', label='arccos(x)')

    plt.title("Arcsin and Arccos Functions")
    plt.xlabel("x (radians)")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    if output_file:
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")
    else:
        plt.show()


if __name__ == "__main__":
    plot_trig_functions()
