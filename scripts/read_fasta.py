import pandas as pd
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

df = pd.read_csv("data/result.tsv", sep="\t")
filtered_df = df[(df['marker_code'] == 'COI-5P') & (df['nuc'].notna())]

records = []
for idx, row in filtered_df.iterrows():
    record_id = row['processid'] or f"seq{idx}"
    species = row['species'] or "Panthera tigris"
    subspecies = row['subspecies'] if pd.notna(row['subspecies']) else "unknown"
    full_id = f"{record_id}|{species}|{subspecies}"
    sequence = row['nuc'].replace(" ", "").replace("\n", "")
    record = SeqRecord(Seq(sequence), id=full_id, description="")
    records.append(record)

SeqIO.write(records, "data/panthera_tigris.fasta", "fasta")
print(f"Disimpan {len(records)} sekuens ke panthera_tigris.fasta")