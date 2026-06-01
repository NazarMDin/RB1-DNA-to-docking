# Step 1: RB1 DNA Sequence Retrieval
# Gene: RB1 (Retinoblastoma 1)
# Source: NCBI Nucleotide — search for gene RB1, Homo sapiens
# Download the FASTA file manually from:
#   https://www.ncbi.nlm.nih.gov/nuccore/NM_000321
# Save it as: outputs/RB1_DNA.fasta

import os

# Input: downloaded FASTA from NCBI Nucleotide
input_file  = "outputs/RB1_DNA.fasta"
output_file = "outputs/RB1_DNA_cleaned.fasta"

if not os.path.exists(input_file):
    print("ERROR: Place your downloaded NCBI FASTA file at outputs/RB1_DNA.fasta")
    print("Download from: https://www.ncbi.nlm.nih.gov/nuccore/NM_000321")
else:
    seq_lines = []
    header = ""
    with open(input_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                header = line.strip()
            else:
                seq_lines.append(line.strip().upper())

    full_seq = "".join(seq_lines)

    with open(output_file, "w") as f:
        f.write(header + "\n")
        for i in range(0, len(full_seq), 70):
            f.write(full_seq[i:i+70] + "\n")

    print(f"Gene     : RB1")
    print(f"Organism : Homo sapiens")
    print(f"Source   : NCBI Nucleotide (NM_000321)")
    print(f"Length   : {len(full_seq)} bp")
    print(f"Saved to : {output_file}")
    print(f"\nFirst 70 bp:")
    print(f"5'-{full_seq[:70]}...-3'")
