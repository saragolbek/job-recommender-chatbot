# Job Recommender Chatbot

This project is a chatbot designed to recommend technology-related careers, including roles in IT, software development, data science, and AI, based on user preferences. It integrates **Pandorabots**, **Flask**, and **API calls** to provide an interactive and insightful user experience.

## Features
- Conversational interface using **Pandorabots** with AIML scripts.
- **Flask** back-end for processing user input and fetching job listings.
- **NLP Integration** with `spaCy` to analyze user input.
- Fetches real-time job listings via the **Adzuna API**.

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`:
  ```
  flask
  requests
  spacy
  ```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/job-recommender-chatbot.git
cd job-recommender-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up NLP
Download the required `spaCy` language model:
```bash
python -m spacy download en_core_web_sm
```

### 4. Run the Flask App
Start the development server:
```bash
python app.py
```
Access the app at `http://127.0.0.1:5000`.

## Files Overview
- `app.py`: The Flask application logic for processing input and fetching job listings.
- `templates/index.html`: Front-end interface for the chatbot.
- `requirements.txt`: List of dependencies required for the project.

## Embedding Pandorabots
To integrate Pandorabots into the project:
1. Get your bot's embed key from the Pandorabots platform.
2. Update the `<script>` tag in `index.html` with your bot's key:
   ```html
   <script>
       new PandorabotsEmbed({
           botkey: "YOUR_BOT_KEY",
           placeholder: "Type here..."
       });
   </script>
   ```

## Future Enhancements
- Add more refined NLP capabilities to handle complex user queries.
- Enhance job recommendations with additional filtering options.
- Deploy the project on a cloud service (e.g., Heroku, Render).

