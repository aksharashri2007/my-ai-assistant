from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question
    )

    return jsonify({"answer": response.output_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

