import tkinter as tk
import pickle

with open("phishing_model.pkl","rb") as f:
    model, vectorizer = pickle.load(f)


def analyze():

    msg = textbox.get("1.0",tk.END)
    vec = vectorizer.transform([msg])

    prediction = model.predict(vec)[0]
    probs = model.predict_proba(vec)[0]
    spam_conf = probs[1] * 100
    if spam_conf >= 80:
        risk = "HIGH!!!"
    elif spam_conf >= 50:
        risk = "MEDIUM!!!"
    else:
        risk = "LOW!!!"
    result.config(
        text=
        f"Prediction: {prediction}\n"
        f"Ham: {probs[0]*100:.2f}%\n"
        f"Spam: {probs[1]*100:.2f}%\n"
        f"Risk Level: {risk}"
    )


root = tk.Tk()
root.title("AI phishing detector")
root.geometry("500x350")

label = tk.Label(root,text="Enter message")
label.pack()

textbox = tk.Text(root,height=10)
textbox.pack()

button = tk.Button(root,text="Analyze",command=analyze)
button.pack()

result = tk.Label(root,text="")
result.pack()
root.mainloop()

