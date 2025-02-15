# services/model_trainer.py

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def train_recommendation_model(df):
    """Train collaborative filtering model."""
    if df.empty:
        return None, None  


    ratings_matrix = df.pivot(index="user_id", columns="book_id", values="rating").fillna(0)

    user_similarity = cosine_similarity(ratings_matrix)

    return ratings_matrix, user_similarity
