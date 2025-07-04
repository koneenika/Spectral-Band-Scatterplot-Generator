📊 Spectral Band Scatterplot Generator – LISS-3 & LISS-4

This project visualizes relationships between different spectral bands from LISS-3 and LISS-4 satellite images using scatterplots. It reads .tif files from Google Drive, extracts specified bands, and generates all possible band-to-band scatterplots for image analysis and comparison.

🚀 Features

Loads selected bands from .tif images in LISS-3 and LISS-4 datasets.

Optionally resizes images for faster plotting.

Generates and saves scatterplots of all band combinations for quick visual insights.

🧰 Tools Used

rasterio for reading .tif bands

matplotlib for plotting

Google Colab for cloud execution

os and pathlib for file handling

💡 Output

A grid of scatterplots for each satellite image set.

Files are saved as high-resolution .png images directly into your Google Drive.

