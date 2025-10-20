import os
import requests
import zipfile
from io import BytesIO

def download_and_extract_data():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Download the dataset
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    print("Downloading MovieLens dataset...")
    response = requests.get(url)
    
    # Extract the zip file
    print("Extracting files...")
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        # Extract only the movies.csv and ratings.csv files
        for file in zip_ref.namelist():
            if file.endswith('movies.csv') or file.endswith('ratings.csv'):
                zip_ref.extract(file, 'data')
                # Rename the files to remove the directory prefix
                old_path = os.path.join('data', file)
                new_path = os.path.join('data', os.path.basename(file))
                if old_path != new_path:
                    os.rename(old_path, new_path)
    
    print("Dataset downloaded and extracted successfully!")

if __name__ == "__main__":
    download_and_extract_data() 