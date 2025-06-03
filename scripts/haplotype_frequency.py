from skbio import DNA
from skbio.alignment import TabularMSA
from collections import Counter
import matplotlib.pyplot as plt

# === Load aligned COI sequences ===
# Read the multiple sequence alignment from FASTA
msa = TabularMSA.read("data/panthera_tigris_aligned.fasta", constructor=DNA)

# Convert aligned sequences to string format
seq_strings = [str(record) for record in msa]

# === Count unique haplotype frequencies ===
counts = Counter(seq_strings)

# === Print haplotype frequency table ===
print(f"{'Haplotype ID':<15}{'Sequence (start)':<20}{'Count':<10}")
for i, (haplo, count) in enumerate(counts.most_common(), 1):
    print(f"H{i:<14}{haplo[:15]:<20}{count:<10}")

# === Generate bar chart for Top 5 haplotypes ===
top_n = 5
top_counts = counts.most_common(top_n)

# Create labels in the format: H1 (ATGTTCA...)
labels = [f"H{i+1}\n({seq[:10]})" for i, (seq, _) in enumerate(top_counts)]
values = [count for _, count in top_counts]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='teal')
plt.xlabel("Haplotype ID (Sequence Start)")
plt.ylabel("Number of Individuals")
plt.title("Top 5 Haplotype Frequencies in Panthera tigris")
plt.tight_layout()
plt.savefig("top5_haplotype_bar_chart.png")
plt.show()