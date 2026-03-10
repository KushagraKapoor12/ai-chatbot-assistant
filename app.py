from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello 👋 I am your Transport Assistant AI. How can I help you?"

    elif "date" in message:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    elif "time" in message:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    elif "bus time" in message or "bus timing" in message or "schedule" in message:
        return "Bus services run from 6:00 AM to 10:00 PM. Peak hours are 8–10 AM and 5–7 PM."

    elif "route" in message:
        return "Major routes include City Center, Railway Station, Airport Road, University Route and Main Market."

    elif "price" in message or "fare" in message:
        return "Bus fares start from ₹10 depending on distance. Monthly student pass is around ₹300."

    elif "student pass" in message:
        return "Student passes provide discounted travel. Apply through the Bus Pass portal."

    elif "apply" in message:
        return "To apply for a bus pass: Register → Login → Apply Pass → Submit details."

    elif "status" in message:
        return "You can check your application status in the Status section."

    elif "admin" in message:
        return "Admin manages approvals and system monitoring."

    elif "help" in message:
        return "You can ask me about bus timings, routes, ticket prices, student passes or bus pass applications."

    elif "thank" in message:
        return "You're welcome 😊"

    elif "bye" in message:
        return "Goodbye 👋 Have a great day!"

    else:
        return "Sorry, I didn't understand. Try asking about bus timings, routes, fares, or bus passes."


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)