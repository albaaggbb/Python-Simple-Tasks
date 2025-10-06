# visualization/words_string_visualization.py
import sys
from IPython.display import Markdown as md
from IPython.display import display
from random import randint

def visualize_words_string(words, min_size=5, max_size=15, use_jupyter=True, output_file=None):
    """
    Creates a colorful, dynamically sized text visualization of a list of words.

    Parameters:
    - words: list of strings, words to visualize.
    - min_size: minimum font size.
    - max_size: maximum font size.
    - use_jupyter: if True, display in Jupyter; otherwise print HTML string.
    - output_file: if provided, saves the visualization as an HTML file.
    """

    if not words:
        print("Error: No words provided for visualization.")
        return

    words_string = "".join(words)
    length = len(words_string)
    increment = (max_size - min_size) / (length / 2)
    
    formatted_letters = ""
    for i, letter in enumerate(words_string):
        color = "#{:06X}".format(randint(0, 0xFFFFFF))
        if i <= length / 2:
            size = min_size + i * increment
        else:
            size = max_size + ((length / 2 - i) * increment)
        formatted_letters += f'<font size="{size}px" color="{color}">{letter}</font>'

    if output_file:
        # Save to HTML
        with open(output_file, "w") as f:
            f.write(f"<html><body>{formatted_letters}</body></html>")
        print(f"Visualization saved to {output_file}")
    elif use_jupyter:
        # Display in Jupyter
        display(md(formatted_letters))
    else:
        # Print HTML string in terminal
        print(formatted_letters)


if __name__ == "__main__":
    # Get words from command line arguments
    words_from_terminal = sys.argv[1:]
    if not words_from_terminal:
        print("No words provided via terminal. Using default sample words.")
        words_from_terminal = ["Python", "Visualization", "Fun", "Code"]
    
    visualize_words_string(words_from_terminal, use_jupyter=False, output_file="visualization.html")
