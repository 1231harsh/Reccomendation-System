# services/model_trainer.py

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def train_recommendation_model(df):
    """Train collaborative filtering model."""
    if df.empty:
        return None, None  # Handle empty data case

    # Pivot table: Users as rows, Books as columns
    ratings_matrix = df.pivot(index="user_id", columns="book_id", values="rating").fillna(0)

    # Calculate similarity using cosine similarity
    user_similarity = cosine_similarity(ratings_matrix)

    return ratings_matrix, user_similarity
