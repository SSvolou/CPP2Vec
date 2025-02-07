# Pre-processing code to trasform datasets (when necessary) from their raw form to the form used in CPP2Vec.

input_file = "CPP2Vec/Data/Test Datasets/64-peptides_Intensities.txt" # Dataset with intensities 
output_file = "CPP2Vec/Data/Test Datasets/64-peptides_01_labels.txt" # Dataset with assigned labels '1','0'

# Assigns the label '1' to peptides that demonstrated a 3-fold or greater improvement in eGFP fluorescence, '0' differently.
def assign_labels (input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            peptide, value = line.strip().split(',')
            label = '1' if float(value) >= 3 else '0'
            outfile.write(f"{peptide},{label}\n")

assign_labels(input_file, output_file)

# Substitutes β-alanine (B) with α-alanine (A) and 6-aminohexanoic acid (X) with lysine (K)
def aa_substitution(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            sequence, label = line.strip().split(',')
            modified_sequence = sequence.replace('B', 'A').replace('X', 'K')
            outfile.write(f"{modified_sequence},{label}\n")
            
aa_substitution(input_file, output_file)