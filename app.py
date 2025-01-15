from flask import Flask, render_template, request, jsonify
import spacy
import requests

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for processing chatbot input
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    doc = nlp(user_input)
    entities = [ent.text for ent in doc.ents]
    if "job" in user_input.lower():
        return jsonify({"response": fetch_job_listings(entities[0] if entities else "IT")})
    return jsonify({"response": f"Analyzed input: {', '.join(entities)}"})

# Function to fetch job listings
APP_ID = "a46a0ccf"
APP_KEY = "7dd48025bf0bbbb3cd086091ee3964d3"

def fetch_job_listings(query):
    url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        "app_id": "app_id",
        "app_key": "api_key",
        "what": query,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        jobs = response.json().get("results", [])
        return "\n".join([f"{job['title']} at {job['company']['display_name']}" for job in jobs[:5]])
    return "No jobs found."

if __name__ == "__main__":
    app.run(debug=True)
