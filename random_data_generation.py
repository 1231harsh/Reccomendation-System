import pandas as pd
import numpy as np

def generate_random_data(num_users=100, num_books=50):
    """Generates random user-book interactions (ratings from 1 to 5)."""
    users = np.arange(1, num_users + 1)
    books = np.arange(1, num_books + 1)

    data = {
        "user_id": np.random.choice(users, 500),
        "book_id": np.random.choice(books, 500),
        "rating": np.random.randint(1, 6, 500),
    }

    df = pd.DataFrame(data)
    df.to_csv("sample_data.csv", index=False)
    print("Random dataset generated and saved as sample_data.csv.")

if __name__ == "__main__":
    generate_random_data()
