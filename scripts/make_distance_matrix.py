from skbio import DistanceMatrix, DNA
from skbio.alignment import TabularMSA
from skbio import read
import pandas as pd

# Baca file hasil alignment
msa = TabularMSA.read('data/panthera_tigris_aligned.fasta', constructor=DNA)

# Fungsi untuk menghitung p-distance (prosentase mismatch)
def p_distance(seq1, seq2):
    mismatches = sum([1 for a, b in zip(str(seq1), str(seq2)) if a != b])
    return mismatches / len(seq1)

# Ambil label ID dari sequence
labels = [str(record.metadata['id']) for record in msa]

# Buat matriks jarak
matrix = []
for seq1 in msa:
    row = []
    for seq2 in msa:
        row.append(p_distance(seq1, seq2))
    matrix.append(row)

# Simpan sebagai dataframe
df = pd.DataFrame(matrix, index=labels, columns=labels)
df.to_csv('data/distance_result.tsv', sep='\t')

print("✅ Distance matrix saved to data/distance_result.tsv")