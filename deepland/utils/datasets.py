import os
import requests
import tqdm
import zipfile


def fetch_data(url, filename, directory="."):
    """Data download helper method."""

    filepath = os.path.abspath(os.path.join(directory, filename))

    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
    except requests.ConnectionError as e:
        raise e
    
    # Save to disk in 10MB chunks and print progress
    #total_size = int(r.headers.get('content-length', 0))
    block_size = 4096 # 4 KB
    #t = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(filepath, 'wb') as f:
        for data in tdqm(response.iter_content(block_size)):
            #t.update(len(data))
            f.write(data)
    #t.close()
    #assert t.n == total_size, "Downloaded data is incomplete."
    
    with zipfile.ZipFile(filepath, 'r') as f:
        f.extract_all(os.path.abspath(directory))

    try:
        os.remove(filepath)
    except OSError as e:
        print(e)
        pass


def harvard_forest(dataset="hf004", directory="."):
    """Fetch datasets for Harvard Forest."""
    
    filename = dataset + ".zip"
    url = "harvardforest.fas.harvard.edu:8080/exist/apps/datasets/showData.html?id=" + dataset
    fetch_data(url, filename=filename, directory=directory)


