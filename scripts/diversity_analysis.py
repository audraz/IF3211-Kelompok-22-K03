from skbio import DNA
from skbio.alignment import TabularMSA
import numpy as np

# Baca hasil alignment
msa = TabularMSA.read('data/panthera_tigris_aligned.fasta', constructor=DNA)

# Nucleotide diversity (π)
def nucleotide_diversity_manual(msa):
    n = len(msa)
    L = msa.shape.position
    total_pi = 0
    for i in range(L):
        column = [str(seq[i]) for seq in msa]
        freqs = {}
        for base in column:
            if base not in freqs:
                freqs[base] = 0
            freqs[base] += 1
        pi_site = 0
        for b1 in freqs:
            for b2 in freqs:
                if b1 < b2:
                    pi_site += (freqs[b1] * freqs[b2])
        total_pi += (2 * pi_site) / (n * (n - 1))
    return total_pi / L

pi = nucleotide_diversity_manual(msa)

# Haplotype diversity (Hd)
seq_strings = [str(record) for record in msa]
unique, counts = np.unique(seq_strings, return_counts=True)
n = sum(counts)
Hd = (n / (n - 1)) * (1 - sum((c / n) ** 2 for c in counts))

# Print
print(f"✅ Nucleotide Diversity (π): {pi:.4f}")
print(f"✅ Haplotype Diversity (Hd): {Hd:.4f}")