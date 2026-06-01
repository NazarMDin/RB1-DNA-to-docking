# Step 2: DNA to mRNA Conversion
# Rule: Replace every Thymine (T) with Uracil (U)
# This simulates the transcription of DNA into mRNA
#
# Input : outputs/RB1_DNA.fasta  (downloaded from NCBI Nucleotide)
# Output: outputs/RB1_mRNA.fasta

input_file  = "outputs/RB1_DNA.fasta"
output_file = "outputs/RB1_mRNA.fasta"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if line.startswith(">"):        # keep FASTA header unchanged
            outfile.write(line)
        else:                           # convert T → U on sequence lines
            rna_seq = line.strip().upper().replace("T", "U")
            outfile.write(rna_seq + "\n")

print(f"Conversion rule : T → U (Thymine → Uracil)")
print(f"Input           : {input_file}")
print(f"Output          : {output_file}")
print(f"RNA FASTA file saved as: {output_file}")
