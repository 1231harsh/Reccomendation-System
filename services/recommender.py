# services/recommender.py

import numpy as np
from config import TOP_N_RECOMMENDATIONS

def recommend_books(user_id, ratings_matrix, user_similarity):
    
    if ratings_matrix is None or user_similarity is None:
        return []

    print(f"📊 Available User IDs: {list(ratings_matrix.index)}") 

    if user_id not in ratings_matrix.index:
        print("⚠️ User ID not found in dataset!")
        return []

    similar_users = np.argsort(-user_similarity[user_id])[:TOP_N_RECOMMENDATIONS + 1]
    similar_users = [u for u in similar_users if u != user_id]

    book_scores = ratings_matrix.loc[similar_users].mean().sort_values(ascending=False)

    return book_scores.head(TOP_N_RECOMMENDATIONS)
