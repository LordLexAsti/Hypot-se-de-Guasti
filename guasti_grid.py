import numpy as np
import matplotlib.pyplot as plt

def generate_guasti_grid(rows=18, cols=26):
    grid = np.full((rows, cols), "", dtype=object)
    grid[0] = list(range(cols))
    for i in range(1, rows):
        for j in range(cols):
            if j % i == 0:
                grid[i, j] = j
    return grid

def display_grid(grid):
    fig, ax = plt.subplots(figsize=(14, 10))
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != "":
                ax.text(j, i, str(grid[i, j]), ha='center', va='center', fontsize=8)
    ax.set_xticks(np.arange(grid.shape[1]))
    ax.set_yticks(np.arange(grid.shape[0]))
    ax.invert_yaxis()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    grid = generate_guasti_grid()
    display_grid(grid)
