# services/background_updater.py

import threading
import time
from services.data_fetcher import fetch_user_activity
from services.data_processor import process_data
from services.model_trainer import train_recommendation_model

class ModelUpdater:
    def __init__(self, update_interval=120):

        self.update_interval = update_interval
        self.ratings_matrix = None
        self.user_similarity = None
        self._stop_event = threading.Event()
        self.lock = threading.Lock()
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self._update_model_loop, daemon=True)

    def start(self):

        print("🔄 Auto-retraining enabled...")
        self.thread.start()

    def stop(self):

        self._stop_event.set()
        self.thread.join()

    def _update_model_loop(self):

        while not self._stop_event.is_set():
            print("📡 Checking for new data...")
            df = fetch_user_activity()
            df = process_data(df)
            
            if not df.empty:
                print("🚀 Updating recommendation model...")
                self.ratings_matrix, self.user_similarity = train_recommendation_model(df)
                print("✅ Model retrained successfully!")
            else:
                print("⚠️ No new data found.")

            time.sleep(self.update_interval)  

model_updater = ModelUpdater()
