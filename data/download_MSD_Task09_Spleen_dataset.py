"""
This script downloads and extracts the MSD Task09 Spleen dataset from the official MSD repository.
The dataset is downloaded as a tar file, which is then extracted to the specified directory.
"""

import os 
from monai.apps import downlaod_and_extract

# Set up the download directory 
root_dir = "./data"
os.makedirs(root_dir, exist_ok=True)

# Define the URL for the MSD Task09 Spleen dataset
url = "https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar"
md5 = "410d4a301da4e5b2f6f86ec3ddba524e" 

# Target file name and location
target_file = os.path.join(root_dir, "Task09_Spleen.tar")
data_dir = os.path.join(root_dir, "Task09_Spleen")

# Download and extract the dataset
if not os.path.exists(data_dir):
    print("Downloading and extracting the MSD Task09 Spleen dataset...")
    downlaod_and_extract(url, target_file, data_dir, md5)
else:    
    print("MSD Task09 Spleen dataset already exists. Skipping download.")