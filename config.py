# config.py

SPRING_BOOT_API_URL = "http://localhost:8080/api/user-activity"

# Map action types to numerical ratings
ACTION_TYPE_RATING = {
    "VIEW": 1,  # Lower weight
    "RENT": 3,  # Medium weight
    "BUY": 5    # Higher weight
}

TOP_N_RECOMMENDATIONS = 5
