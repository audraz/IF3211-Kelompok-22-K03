# Measurement of Genetic Diversity Analysis of _Panthera tigris_ using COI Gene DNA Barcoding Data

## **Project Overview**

This project analyzes the genetic diversity of *Panthera tigris* (tiger) using mitochondrial COI gene data. The goal is to measure intra-species variation and visualize potential subspecies clusters using bioinformatics tools.

### **Features:**
- COI sequence analysis using Python
- Multiple sequence alignment with MUSCLE
- Calculation of nucleotide diversity (π) and haplotype diversity (Hd)
- Visualization using heatmap and Principal Coordinates Analysis (PCoA)

## **Requirements**

Before running, install the following Python libraries:

```bash
pip install biopython scikit-bio pandas matplotlib seaborn scikit-learn
```

---

## **How to Run**

1. **Put your input data** in `data/` folder (FASTA format).
2. **Run scripts in this order**:

```bash
python read_fasta.py
python clean_fasta.py
python run_alignment.py
python diversity_analysis.py
python make_distance_matrix.py
python visualization.py
```
