# Simple Tasks

This repository contains small Python scripts and examples for practicing common tasks, scientific or biochemical calculations, and data manipulation.  

## Repository Structure
```bash
simple-tasks/
├── README.md
├── chemistry/
│   └── peptide_bond_distance.py
├── bioinformatics/
│   ├── sequence_length_calculator.py
│   └── adenine_counter.py
├── visualization/
│   ├── 3d_surface_plot.py
│   ├── string_visualization.py
│   └── trig_functions_plot.py
└── utils/
    └── ip_validator.py

```

## Scripts Overview

### chemistry/

- **peptide_bond_distance.py**  
  Calculates the distance of a peptide bond between a carbon (C) atom of the carbonyl group and a nitrogen (N) atom of the next amino acid residue using 3D Euclidean distance.  
**Usage:**  
 ```bash 
  python chemistry/peptide_bond_distance.py
 ``` 
**Expected Output:** distance in Ångstroms (~1.23 Å) 

### bioinformatics/

- **sequence_length_calculator.py**  
  Calculates the length of one or more DNA sequences provided as command-line arguments.  
  Supports **all IUPAC nucleotide codes** (`A, C, G, T, R, Y, S, W, K, M, B, D, H, V, N`).  
  If a sequence contains invalid characters, it prints an error message instead of calculating the length.
**Usage:**  
 ```bash 
  python bioinformatics/sequence_length_calculator.py ATGC NRYTG
 ``` 
**Example Output:** 4

- **adenine_counter.py**  
  Counts the number of adenines (A) in one or more DNA sequences provided as command-line arguments.  
  Supports **all IUPAC nucleotide codes** (`A, C, G, T, R, Y, S, W, K, M, B, D, H, V, N`).  
  If a sequence contains invalid characters, it prints an error message instead of counting.  
  **Usage:**  
```bash
  python bioinformatics/adenine_counter.py ATGCA NRYTGA
```

  **Example Output:** 
``` python
  Sequence 'ATGCA' has 2 adenine(s).
  Sequence 'NRYTGA' has 1 adenine(s).
```

### visualization/

- **3d_surface_plot.py**  
  Plots the 3D surface of the function `f(x, y) = cos(x) + 2*sin(y)` using Matplotlib.  
  - Creates a grid in the range [-π, π] for both x and y.  
  - Uses `ax.plot_surface` with the `RdBu` colormap.  
  - Adds axis labels, title, and color bar for clarity.  
  - Can display the plot in Jupyter or save it to a file.

**Usage in Jupyter:**
```python
%run visualization/3d_surface_plot.py
```

**Usage from the terminal:**
```python
from visualization.3d_surface_plot import plot_3d_surface

plot_3d_surface(output_file="3d_surface_plot.png")
```

**Example output:**
A 3D surface plot of `f(x, y) = cos(x) + 2*sin(y)` over the interval [-π, π] for x and y.

- **barcelona_meteo.py**  
  Visualizes meteorological data for Barcelona Airport.  
  The script generates two plots:
  1. **Temperature plot**: maximum, minimum, and average monthly temperatures.  
  2. **Rain & humidity plot**: monthly rainfall as a bar chart with relative humidity overlaid as a line.  

  Features:
  - Automatically creates a `plots/` folder inside `visualization/` to save PNGs when running from a terminal.  
  - Uses `matplotlib` for both line and bar plots.  
  - Axis labels, titles, legends, and y-axis limits included for clarity.  

**Usage in terminal (.py file):**
```bash
python visualization/barcelona_meteo.py
```

**Usage in Jupyter Notebook:**
```python
from visualization.barcelona_meteo import plot_temperature, plot_rain_humidity

plot_temperature(meteo)
plot_rain_humidity(meteo)
```


- **trig_functions_plot.py**  
  Plots the `arcsin(x)` and `arccos(x)` functions over the interval [-1, 1] in radians using Matplotlib.  
  - Adds title, axis labels, legend, and grid for clarity.  
  - Can display the plot in Jupyter or save it to a file.

**Usage in Jupyter:**
```python
from visualization.trig_functions_plot import plot_trig_functions

plot_trig_functions()
```
**Usage from the terminal (save plot to file)**
```python
from visualization.trig_functions_plot import plot_trig_functions

plot_trig_functions("arcsin_arccos_plot.png")
```

**Example output**
A plot showing arcsin(x) in red and arccos(x) in green over the interval [-1, 1] radians.

- **words_string_visualization.py**  
  Creates a colorful, dynamically sized text visualization of a list of words.  
  - Works with **any list of words**.  
  - Each letter is assigned a **random color** and a **dynamic font size** that grows toward the middle of the string and then decreases.  
  - Can display the visualization in **Jupyter/IPython** or generate an **HTML file** for viewing in a browser.

**Usage in Jupyter:**
```python
  from visualization.words_string_visualization import visualize_words_string

  words = ["Hello", "World", "Python"]
  visualize_words_string(words)
```

**Usage from the terminal:**
```bash
  python visualization/words_string_visualization.py Hello World Python
```

**Example Output:** 
  The letters of `"HelloWorldPython"` will appear in varying sizes and random colors.

### utils/

- **ip_validator.py**  
  Validates an IPv4 address provided by the user.  
  - Checks that the address has **exactly 4 fields** separated by dots.  
  - Each field must be an **integer between 0 and 255**.  
  - If the IP is invalid, prints a clear **error message** and exits.  
  - Can be used **interactively** or by passing the IP as a command-line argument.

**Usage from the terminal (with argument):**
```bash
  python utils/ip_validator.py 192.168.0.1
```

**Usage interactively (no argument):**
```bash
python utils/ip_validator.py
# Then input an IP when prompted
```

**Example output:**
```bash
The address '192.168.0.1' is a valid IPv4 address.
```

