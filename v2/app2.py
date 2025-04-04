import google.generativeai as genai
from flask import Flask, request, render_template, jsonify
# Configure the API key
genai.configure(api_key="AIzaSyCDGcW16cNh_IFDhafVEV16kW6-lbaxhho")  # Replace with your actual API key
# Use a consistent model name
MODEL_NAME = "gemini-1.5-flash-latest"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index2.html")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        print(f"User Input: {user_input}")  # Debug print
        
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(user_input)
        print(f"API Response: {response.text}")  # Debug print
        
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)

