from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔑 paste your openrouter api key here
API_KEY = "sk-or-v1-28b...aaf"

# check server running
@app.route("/")
def home():
    return "AI Ad Generator Backend Running 🚀"

# main AI route
@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    product = data.get("product")
    price = data.get("price")
    offer = data.get("offer")

    prompt = f"""
    Create a catchy advertisement for:
    Product: {product}
    Price: {price}
    Offer: {offer}

    Give:
    - headline
    - description
    - tagline
    """

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=body)
    result = response.json()

    ad_text = result["choices"][0]["message"]["content"]

    return jsonify({"ad": ad_text})

app.run(debug=True)
