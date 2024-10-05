# 1- sequence_length_calculator.py
import sys

seqs = sys.argv[1:]

for seq in seqs:
    print(len(seq))