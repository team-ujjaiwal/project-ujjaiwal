
from flask import Flask, request
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/gpt-3.5-turbo", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return {"response": response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    app.run()
