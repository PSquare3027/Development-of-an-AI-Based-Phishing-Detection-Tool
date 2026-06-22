import pickle

with open("phishing_model.pkl","rb") as f:
    model, vectorizer = pickle.load(f)

while True:

    msg = input("\nEnter Message: ")

    vec = vectorizer.transform([msg])
    prediction = model.predict(vec)[0]
    probs = model.predict_proba(vec)[0]

    print()
    print("Prediction:",prediction)
    print(f"Ham Confidence: "f"{probs[0]*100:.2f}%")
    print(f"Spam Confidence: "f"{probs[1]*100:.2f}%")