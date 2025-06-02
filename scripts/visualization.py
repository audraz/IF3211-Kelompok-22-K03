import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import MDS

def clean_labels(raw_labels):
    """
    Bersihkan label dengan menghapus kolom 'Panthera' jika ada.
    """
    cleaned = []
    for label in raw_labels:
        if 'Panthera' in label:
            cleaned.append(label.replace('Panthera', '').strip())
        else:
            cleaned.append(label.strip())
    return cleaned

def plot_pcoa(distance_matrix, labels, save_path='pcoa_plot.png'):
    pcoa = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    coords = pcoa.fit_transform(distance_matrix)
    
    df = pd.DataFrame(coords, columns=["PCo1", "PCo2"])
    df["label"] = labels

    plt.figure(figsize=(8,6))
    plt.scatter(df["PCo1"], df["PCo2"])

    for i, txt in enumerate(df["label"]):
        plt.annotate(txt, (df["PCo1"][i], df["PCo2"][i]), fontsize=8)

    plt.title("PCoA Plot Variasi Genetik Panthera tigris")
    plt.xlabel("PCo 1")
    plt.ylabel("PCo 2")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_heatmap(distance_matrix, labels, save_path='heatmap_genetik.png'):
    df = pd.DataFrame(distance_matrix, index=labels, columns=labels)
    plt.figure(figsize=(12, 10))
    sns.heatmap(df, cmap="mako", annot=False, linewidths=0.5)
    plt.title("Heatmap Matriks Jarak Genetik COI")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    # Load dan bersihkan data
    df = pd.read_csv("data/result.tsv", sep="\t", index_col=0)
    labels_raw = df.index.tolist()
    labels = clean_labels(labels_raw)
    
    distance_matrix = df.values

    # Panggil visualisasi
    plot_pcoa(distance_matrix, labels)
    plot_heatmap(distance_matrix, labels)
