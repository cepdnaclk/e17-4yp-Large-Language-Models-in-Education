import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

embedder = SentenceTransformer('all-MiniLM-L6-v2')

class CacheLFU:
    def __init__(self, category):
        self.category = category
        self.size = 4
        # Initialize fixed size dataframe
        columns = ['Question', 'Response', 'Access Count']
        # Create a list of dictionaries with default values
        data = [{'Question': '', 'Response': '', 'Access Count': 0} for _ in range(self.size)]
        # Create a DataFrame from the list of dictionaries
        cache_df = pd.DataFrame(data, columns=columns)
        #encode questions
        embeddings_cache_questions = embedder.encode(cache_df['Question'])
        print(self.category, "cache initialized")
        print(len(embeddings_cache_questions))
