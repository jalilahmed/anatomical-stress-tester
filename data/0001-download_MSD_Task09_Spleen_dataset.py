"""
This script downloads and extracts the MSD Task09 Spleen dataset from the official MSD repository.
The dataset is downloaded as a tar file, which is then extracted to the specified directory.
"""

import argparse
import os 
import json
from monai.apps import download_and_extract
from monai.utils import first

def download_dataset():
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
        download_and_extract(url, target_file, data_dir, md5)
    else:    
        print("MSD Task09 Spleen dataset already exists. Skipping download.")


def validate_dataset():
    data_dir = "./data/Task09_Spleen/Task09_Spleen"
    json_path = os.path.join(data_dir, "dataset.json")
    with open(json_path, "r") as f:
        dataset_metadata = json.load(f)

    print(f"Dataset Name: {dataset_metadata['name']}")
    print(f"Number of Training Images: {dataset_metadata['numTraining']}")

    # Quick peek at the training data dictionary pairs
    training_samples = dataset_metadata["training"]
    print("\nFirst training sample pair:")
    print(first(training_samples))

def main(args=None):
    download_flag = args.download if args else False  
    validate_flag = args.validate if args else False  
    if download_flag:
        download_dataset()
    elif validate_flag:
        validate_dataset()
    else:
        print("Please specify an action: --download to download the dataset or --validate to validate the dataset.")

if __name__ == "__main__":
    # Pass arguments to the main function for controlling the flow of the script
    parser = argparse.ArgumentParser(description="Download and validate the MSD Task09 Spleen dataset")
    parser.add_argument("--download", action="store_true", help="Download the MSD Task09 Spleen dataset")
    parser.add_argument("--validate", action="store_true", help="Validate the downloaded MSD Task09 Spleen dataset")
    args = parser.parse_args()
    main(args)