from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

class ExpertSystem:
    def __init__(self):
        self.disease_db = [
            ("Influenza", "Yes", "No", "Yes", "Yes", 19, "Female", "Low", "Normal", "Positive"),
            ("Common Cold", "No", "Yes", "Yes", "No", 25, "Female", "Normal", "Normal", "Negative"),
            ("Eczema", "No", "Yes", "Yes", "No", 25, "Female", "Normal", "Normal", "Negative"),
            ("Asthma", "Yes", "Yes", "No", "Yes", 25, "Male", "Normal", "Normal", "Positive"),
            ("Hyperthyroidism", "No", "Yes", "No", "No", 28, "Female", "Normal", "Normal", "Negative")
        ]

    def calculate_match_score(self, user_data, disease):
        score = 0
        attributes = ["fever", "cough", "fatigue", "difficultyBreathing", "age", "gender", "bloodPressure", "cholesterolLevel"]

        for i, attribute in enumerate(attributes):
            if attribute == "age":
                try:
                    age_difference = abs(int(user_data[attribute]) - disease[i + 1])
                    if age_difference <= 5:
                        score += 1
                except ValueError:
                    continue
            else:
                if user_data[attribute].lower() == disease[i + 1].lower():
                    score += 1
        return score

    def diagnose(self, user_data):
        possible_diseases = set()
        highest_score = 0

        for disease in self.disease_db:
            if disease[-1].lower() == "positive":
                score = self.calculate_match_score(user_data, disease)
                print(f"Comparing with disease: {disease[0]}, score: {score}")  # Debug print
                if score > highest_score:
                    highest_score = score
                    possible_diseases = {disease[0]}
                elif score == highest_score:
                    possible_diseases.add(disease[0])

        if highest_score > 6:
            return list(possible_diseases)
        else:
            return []

expert_system = ExpertSystem()

@app.route("/diagnose", methods=["POST"])
def diagnose():
    user_data = request.json
    print("Received user data:", user_data)  # Debug print
    diagnosis = expert_system.diagnose(user_data)
    print("Diagnosis result:", diagnosis)  # Debug print
    return jsonify({"diagnosis": diagnosis})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
