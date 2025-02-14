# services/data_processor.py

from config import ACTION_TYPE_RATING

def process_data(df):
    """Process user activity data and convert action types to ratings."""
    if df.empty:
        return df  # Return empty DataFrame if no data
    
    df["rating"] = df["actionType"].map(ACTION_TYPE_RATING).fillna(1)  # Default to VIEW rating

    # Keep only relevant columns
    df = df[["user.id", "book.id", "rating"]]
    df.columns = ["user_id", "book_id", "rating"]  # Rename columns

    return df
