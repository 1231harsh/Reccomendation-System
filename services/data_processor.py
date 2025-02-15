# services/data_processor.py

from config import ACTION_TYPE_RATING

def process_data(df):
    """Process user activity data and convert action types to ratings."""
    if df.empty:
        return df  
    
    df["user.id"] = df["user"].apply(lambda x: x["id"])
    df["book.id"] = df["book"].apply(lambda x: x["id"])
    df["rating"] = df["actionType"].map(ACTION_TYPE_RATING).fillna(1)  

    df = df[["user.id", "book.id", "rating"]]
    df.columns = ["user_id", "book_id", "rating"] 
    return df
