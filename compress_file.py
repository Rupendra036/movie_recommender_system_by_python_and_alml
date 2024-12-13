import gzip
import shutil

# Check that similarity.pkl exists
try:
    with open("similarity.pkl", "rb") as f_in:
        with gzip.open("similarity.pkl.gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("File compression successful!")
except FileNotFoundError:
    print("similarity.pkl not found in the directory.")
