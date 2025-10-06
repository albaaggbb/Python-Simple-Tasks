import sys

# Set of valid DNA bases including IUPAC codes
VALID_BASES = set("ACGTRYSWKMBDHVN")

# Get sequences from command line arguments
seqs = sys.argv[1:]

if not seqs:
    print("Please provide one or more DNA sequences as arguments.")
    sys.exit(1)

for seq in seqs:
    seq = seq.upper()  # normalize to uppercase
    if all(base in VALID_BASES for base in seq):
        count_A = seq.count('A')
        print(f"Sequence '{seq}' has {count_A} adenine(s).")
    else:
        invalid_chars = set(seq) - VALID_BASES
        print(f"Error: sequence '{seq}' contains invalid characters: {', '.join(invalid_chars)}")
