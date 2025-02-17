# services/model_trainer.py

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def train_recommendation_model(df):
    """Train collaborative filtering model."""
    if df.empty:
        print("❌ No data available for training!")
        return None, None  


    ratings_matrix = df.pivot(index="user_id", columns="book_id", values="rating").fillna(0)
    print(f"📊 Ratings Matrix Shape: {ratings_matrix.shape}")  # ✅ Debug shape

    # if ratings_matrix.shape[0] < 2:
    #     print("⚠️ Not enough users for similarity calculations!")
    #     return None, None  

    user_similarity = cosine_similarity(ratings_matrix)
    user_similarity = pd.DataFrame(user_similarity, index=ratings_matrix.index, columns=ratings_matrix.index)
    print(f"📊 User Similarity Matrix Shape: {user_similarity.shape}")

    return ratings_matrix, user_similarity
