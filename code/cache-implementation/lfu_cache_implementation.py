import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

embedder = SentenceTransformer('all-MiniLM-L6-v2')

class CacheLFU:
    def __init__(self, category):
        """
        Create a new cache object.

        Args:
            category: The category of the cache.  

        Returns:
            None.
        """
        self.category = category
        self.size = 4
        # Initialize fixed size dataframe
        columns = ['Question', 'Response', 'Access Count']
        # Create a list of dictionaries with default values
        data = [{'Question': '', 'Response': '', 'Access Count': 0} for _ in range(self.size)]
        # Create a DataFrame from the list of dictionaries
        self.cache_df = pd.DataFrame(data, columns=columns)
        #encode questions
        self.embeddings_cache = embedder.encode(self.cache_df['Question'])
        print(self.category, "cache initialized")
        print(len(self.embeddings_cache))   
        
    def add_record(self, new_values):
        """
        Add a new record to the cache.

        Args:
            new_values (dict): The new record values. Ex - {'Question': 'How does TLB caching improve virtual memory performance?', 'Response': 'Resp 23', 'Access Count': 0}

        Returns:
            None.
        """

        # Check if the cache is full.
        if len(self.cache_df) == self.size:
            # Get the least accessed question in the cache.
            least_accessed_question = self.cache_df[self.cache_df['Access Count'] == self.cache_df['Access Count'].min()].iloc[0]
            print("Least accessed question:", least_accessed_question)
            removing_record_index = least_accessed_question.name
            print("Removing record with index", removing_record_index)
            
            self.cache_df.loc[removing_record_index] = new_values
            
            # Encode the new question
            encoded_question = embedder.encode(new_values['Question'])
            
            # Update the embeddings cache.
            self.embeddings_cache[removing_record_index] = encoded_question
    
    def update_count(self, index):
        """
        Update the access count of a record.

        Args:
            index (int): The index of the record to be updated.

        Returns:
            None.
        """
        self.cache_df.loc[index, 'Access Count'] += 1

    def get_response(self, index):
        """
        Get the response for a record.

        Args:
            index (int): The index of the record to be retrieved.

        Returns:
            str: The response for the record.
        """
        return self.cache_df.loc[index, 'Response']
