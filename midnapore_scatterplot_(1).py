# -*- coding: utf-8 -*-
"""Midnapore_scatterplot_(1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R35CGPHazBKWMn3DcpCyqVU5JuhyAVbf
"""

!pip install rasterio

!pip install pathlib

!pip insatll path

import os
from pathlib import Path
import rasterio
import matplotlib.pyplot as plt
from google.colab import drive

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Define the function to load bands from a folder
def load_image_band(img_folder, bands, width=None):
    """Load specific bands from a folder and return the image and dataset dictionaries."""
    image = {}
    dataset = {}
    path = Path(img_folder)

    # Determine the desired output shape if width is provided
    out_shape = (int(width / 7601 * 7761), width) if width else None
    if width:
        print(f"Using output shape: {out_shape}")

    # Read the specified bands and store them in dictionaries
    for band in bands:
        file = next(path.glob(f"*{band}.tif"), None)
        if not file:
            raise FileNotFoundError(f"The Band {band} not found in {img_folder}")

        print(f"Opening file: {file}")
        dataset[band] = rasterio.open(file)
        image[band] = dataset[band].read(1, out_shape=out_shape)

    return image, dataset

# Step 3: Set the folder paths in Google Drive
liss3_folder = "/content/drive/MyDrive/Mid/LISS3"
liss4_folder = "/content/drive/MyDrive/Mid/LISS4"

# Step 4: Load Images
img_l3, image_dataset_l3 = load_image_band(liss3_folder, ['BAND2', 'BAND3', 'BAND4', 'BAND5'], width=1000)
img_l4, image_dataset_l4 = load_image_band(liss4_folder, ['BAND2', 'BAND3', 'BAND4'], width=1000)

# Step 5: Function to plot scatterplots for all band combinations
def plot_scatterplots(image, title_prefix, save_path):
    """Generate scatterplots for all band combinations and save them."""
    band_keys = list(image.keys())
    num_combinations = len(band_keys) * (len(band_keys) - 1) // 2
    rows = (num_combinations + 2) // 3
    plt.figure(figsize=(18, rows * 6))

    count = 1
    for i in range(len(band_keys)):
        for j in range(i + 1, len(band_keys)):
            x_band, y_band = band_keys[i], band_keys[j]
            x_data, y_data = image[x_band].ravel(), image[y_band].ravel()

            plt.subplot(rows, 3, count)
            plt.scatter(x_data, y_data, s=1, alpha=0.5)
            plt.title(f"{title_prefix}: {x_band} vs {y_band}")
            plt.xlabel(x_band)
            plt.ylabel(y_band)
            count += 1

    # Save the figure
    os.makedirs(save_path, exist_ok=True)
    file_name = os.path.join(save_path, f"{title_prefix}_scatterplots.png")
    plt.tight_layout()
    plt.savefig(file_name, dpi=300)
    plt.close()
    print(f"Scatterplots saved as {file_name}")

# Step 6: Define save paths
save_path_l3 = "/content/drive/MyDrive/LISS3"
save_path_l4 = "/content/drive/MyDrive/LISS4"

# Step 7: Generate scatterplots and save them
plot_scatterplots(img_l3, "LISS-3", save_path_l3)
plot_scatterplots(img_l4, "LISS-4", save_path_l4)

