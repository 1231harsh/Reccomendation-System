# app.py

from flask import Flask, request, jsonify
from services.recommender import recommend_books
from services.background_updater import model_updater

app = Flask(__name__)

model_updater.start()

@app.route("/")
def home():
    return "Book Recommendation API is running!"


@app.route("/recommend", methods=["GET"])
def recommend():
    if model_updater.ratings_matrix is None or model_updater.user_similarity is None:
        return jsonify({"error": "Recommendation model not trained yet!"}), 500
    
    try:
        user_id = int(request.args.get("user_id"))
        recommendations = recommend_books(user_id, model_updater.ratings_matrix, model_updater.user_similarity)
        return jsonify({"user_id": user_id, "recommended_books": recommendations.index.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/force_retrain", methods=["POST"])
def force_retrain():
    """Manually retrain the model."""
    print("🔄 Manually retraining model...")
    model_updater._update_model_loop() 
    return jsonify({"message": "Model retrained successfully!"})

