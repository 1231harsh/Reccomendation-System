# services/data_processor.py

from config import ACTION_TYPE_RATING

def process_data(df):
    """Process user activity data and convert action types to ratings."""
    if df.empty:
        return df  

    df = df.dropna(subset=["user", "book"]).copy()

    df["user.id"] = df["user"].apply(lambda x: x["id"] if isinstance(x, dict) else None)
    df["book.id"] = df["book"].apply(lambda x: x["id"] if isinstance(x, dict) else None)

    df = df.dropna(subset=["user.id", "book.id"]).copy()

    df["rating"] = df["actionType"].map(ACTION_TYPE_RATING).fillna(1)

    df = df[["user.id", "book.id", "rating"]].copy()
    df.columns = ["user_id", "book_id", "rating"] 

    df = df.groupby(["user_id", "book_id"], as_index=False).agg({"rating": "mean"}).copy()

    return df
