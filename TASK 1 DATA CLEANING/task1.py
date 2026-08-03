import pandas as pd
df = pd.read_csv("Dataset.csv")
df.head()
df.shape
df.info()
df.columns
df.isnull().sum()
df.duplicated().sum()
df["type"].unique()
df["rating"].unique()
df["country"].head()
df.to_csv("cleaned_netflix_dataset.csv", index= False)