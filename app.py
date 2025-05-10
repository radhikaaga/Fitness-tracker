from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.nutritionix.nutrition_api import get_nutritional_info
from backend.nutritionix.exercise_api import get_exercise_info

app = Flask(__name__)
CORS(app)  # Enable CORS

# Replace with your actual username and graph ID
USERNAME = "riddhikhandelwal"
GRAPH_ID = "weight-gain"

@app.route("/nutrition", methods=["POST"])
def nutrition():
    data = request.get_json()
    print("Received nutrition request:", data)   # 🛠 Debug print

    if not data or 'query' not in data:
        return jsonify({"error": "No food provided"}), 400

    food_query = data['query']
    info = get_nutritional_info(food_query, USERNAME, GRAPH_ID)

    print("Nutrition info fetched:", info)    # 🛠 Debug print

    if isinstance(info, dict):
        return jsonify(info)
    else:
        return jsonify({"message": str(info)})

@app.route("/exercise", methods=["POST"])
def exercise():
    data = request.get_json()
    print("Received exercise request:", data)   # 🛠 Debug print

    if not data or 'query' not in data:
        return jsonify({"error": "No exercise provided"}), 400

    exercise_query = data['query']
    info = get_exercise_info(exercise_query, USERNAME, GRAPH_ID)

    print("Exercise info fetched:", info)   # 🛠 Debug print

    if isinstance(info, dict):
        return jsonify(info)
    else:
        return jsonify({"message": str(info)})

if __name__ == "__main__":
    app.run(debug=True)
