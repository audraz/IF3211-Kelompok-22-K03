import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import MDS

# Bersihkan label dari kata 'Panthera' jika ada
def clean_labels(raw_labels):
    cleaned = []
    for label in raw_labels:
        if 'Panthera' in label:
            cleaned.append(label.replace('Panthera', '').strip())
        else:
            cleaned.append(label.strip())
    return cleaned

# Ambil prefix (4 huruf pertama) sebagai pengelompokan awal
def extract_prefix(sample_id):
    return sample_id[:4]

# Plot PCoA dengan warna per grup
def plot_pcoa(distance_matrix, labels, save_path='pcoa_plot.png'):
    pcoa = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    coords = pcoa.fit_transform(distance_matrix)

    df = pd.DataFrame(coords, columns=["PCo1", "PCo2"])
    df["SampleID"] = labels
    df["Group"] = [extract_prefix(label) for label in labels]

    plt.figure(figsize=(12, 10))
    sns.scatterplot(data=df, x="PCo1", y="PCo2", hue="Group", s=80, palette="tab10")

    # Tentukan batas axis dengan margin ekstra supaya titik tidak terlalu rapat di tepi
    margin = 0.1
    x_min, x_max = df["PCo1"].min(), df["PCo1"].max()
    y_min, y_max = df["PCo2"].min(), df["PCo2"].max()
    plt.xlim(x_min - margin, x_max + margin)
    plt.ylim(y_min - margin, y_max + margin)

    # Geser label titik lebih jauh (0.01 atau coba-coba sampai pas)
    for i in range(len(df)):
        plt.text(df["PCo1"][i] + 0.01, df["PCo2"][i] + 0.01, df["SampleID"][i], fontsize=7)

    plt.title("PCoA Plot Variasi Genetik Panthera tigris")
    plt.xlabel("PCo 1")
    plt.ylabel("PCo 2")
    plt.legend(title="Kelompok (Prefix ID)")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# Plot heatmap jarak genetik
def plot_heatmap(distance_matrix, labels, save_path='heatmap_genetik.png'):
    df = pd.DataFrame(distance_matrix, index=labels, columns=labels)
    plt.figure(figsize=(12, 10))
    sns.heatmap(df, cmap="mako", annot=False, linewidths=0.5)
    plt.title("Heatmap Matriks Jarak Genetik COI")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# Main function
if __name__ == "__main__":
    # Baca matriks jarak
    df = pd.read_csv("data/result.tsv", sep="\t", index_col=0)
    labels_raw = df.index.tolist()
    labels = clean_labels(labels_raw)
    distance_matrix = df.values

    # Panggil visualisasi
    plot_pcoa(distance_matrix, labels, save_path="pcoa_plot_colored.png")
    plot_heatmap(distance_matrix, labels, save_path="heatmap_genetik.png")
