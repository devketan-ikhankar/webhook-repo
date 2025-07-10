from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
from dateutil import parser  # NEW line

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print("📦 Received webhook data:", data)

        # Validate data
        required_fields = ["request_id", "author", "action", "from_branch", "to_branch", "timestamp"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"❌ Missing field: {field}")

        # Convert timestamp safely
        timestamp = parser.parse(data["timestamp"])

        # Insert into MongoDB
        collection.insert_one({
            "request_id": data["request_id"],
            "author": data["author"],
            "action": data["action"],
            "from_branch": data["from_branch"],
            "to_branch": data["to_branch"],
            "timestamp": timestamp
        })

        print("✅ Inserted into MongoDB")
        return {"status": "saved"}, 200

    except Exception as e:
        print("❌ ERROR during webhook processing:", e)
        return {"error": str(e)}, 500

@app.route('/')
def index():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    return render_template("events.html", events=events)

if __name__ == '__main__':
    print("flask started")
    app.run(debug=True)