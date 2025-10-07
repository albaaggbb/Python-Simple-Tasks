import numpy as np

def find_nearest(array, value):
    """
    Returns the index and value of the element in 'array' closest to 'value'.
    """
    array = np.array(array)
    differences = np.abs(array - value)
    index = np.argmin(differences)
    return index, array[index]

if __name__ == "__main__":
    # Example array
    Z = np.array([
        0.47370212,0.25529126,0.14185629,0.43800344,0.29842454,
        0.13811606,0.56393031,0.79486108,0.94497137,0.34532689
    ])
    
    # Target value
    v = 0.68724651
    
    index, nearest_value = find_nearest(Z, v)
    
    print("Index of nearest element:", index)
    print("Nearest element value:", nearest_value)