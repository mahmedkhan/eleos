# Importing the pandas and numpy libraries, as well as particular modules from sklearn.
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing our resource database.
df = pd.read_csv('resources.csv')
print(df.head())
print('hey girl')
