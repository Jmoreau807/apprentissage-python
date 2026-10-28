import polars as pl
import sklearn
import numpy as np

print("NumPy :", np.__version__)
print("scikit-learn :", sklearn.__version__)

df = pl.DataFrame({"x": [1, 2, 3, 4, 5]})
print(df)
print("Moyenne :", df["x"].mean())