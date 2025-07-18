from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Load the trained ensemble model
with open("voting_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the scaler (for normalizing the features)
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# List of possible states for OHE (same as during model training)
states = [
    "Andhra Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", 
    "Daman & Diu", "Daman, Diu, Dadra Nagar Haveli", "Delhi", "Goa", 
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", 
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Nagaland", "Odisha", "Pondicherry", 
    "Rajasthan", "Sikkim", "TamilNadu", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "class"
]

@app.route("/")
def home():
    return render_template("form.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "")
        last_name = request.form.get("lastName", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        subject = request.form.get("subject", "")
        message = request.form.get("message", "")

        full_message = f"""
        New Contact Form Submission:

        Name: {name} {last_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message:
        {message}
        """

        try:
            send_email("New Contact Form Submission", full_message, reply_to=email)
            return render_template("contact.html", success=True)
        except Exception as e:
            print(f"Error sending email: {e}")
            return render_template("contact.html", error=True)
    else:
        return render_template("contact.html")

def send_email(subject, body, reply_to=None):
    sender_email = "uchihagirl2000@gmail.com"  # factor gmail
    receiver_email = "waterqalityanalysis@gmail.com"
    password = "fvfpiltjeotsrpyh"  # App Password (from 2 factor authentication)

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    if reply_to:
        msg["Reply-To"] = reply_to  # key

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

@app.route("/result")
def result():
    return render_template("result.html")

def one_hot_encode_state(state):
    state_vector = [0] * len(states)  # Initialize with zeros
    if state in states:
        index = states.index(state)
        state_vector[index] = 1  # Set the corresponding index to 1
    return state_vector

# Define route for prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data from the user input
        data = request.form
        
        # Validate inputs
        required_fields = [
            "temperature", "do", "ph", "conductivity", 
            "bod", "nitrate", "fecalcoliform", "totalcoliform", "state"
        ]
        
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing required field: {field}"})
        
        # Process numeric inputs
        try:
            features = [
                float(data["temperature"]),
                float(data["do"]),
                float(data["ph"]),
                float(data["conductivity"]),
                float(data["bod"]),
                float(data["nitrate"]),
                float(data["fecalcoliform"]),
                float(data["totalcoliform"])
            ]
        except ValueError:
            return jsonify({"error": "All parameter values must be valid numbers"})
            
        # One-hot encode the selected state
        state_encoded = one_hot_encode_state(data["state"])
        
        # Append the one-hot encoded state to the feature list
        features.extend(state_encoded)
        
        # Scale the numeric features using the scaler.pkl
        features_scaled = scaler.transform([features])  # Apply scaling
        
        # Make the prediction using the trained ensemble model
        prediction = model.predict(features_scaled)
        
        # Convert output to readable format
        result = "Drinkable" if prediction[0] == 1 else "Not Drinkable"
        
        # Return the result as JSON
        return jsonify({"prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)