from Bio import SeqIO

input_file = "data/panthera_tigris.fasta"
output_file = "data/panthera_tigris_cleaned.fasta"

min_length = 650
valid_sequences = []

for record in SeqIO.parse(input_file, "fasta"):
    is_long_enough = len(record.seq) >= min_length
    has_subspecies = "unknown" not in record.id.lower()
    
    if is_long_enough and has_subspecies:
        valid_sequences.append(record)

print(f"{len(valid_sequences)} sekuens lolos ke cleaned fasta dari total {len(list(SeqIO.parse(input_file, 'fasta')))}.")

SeqIO.write(valid_sequences, output_file, "fasta")
