import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv(r"D:\Code Stuff\Python\Project2\kagglehub\datasets\uciml\sms-spam-collection-dataset\versions\1\spam.csv",encoding="latin-1")
data = data[["v1", "v2"]]
data.columns = ["label","message"]

X = data["message"]
y = data["label"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

predict = model.predict(X_test)
accuracy = accuracy_score(y_test,predict)


import pickle

with open("phishing_model.pkl", "wb") as f:
    pickle.dump(
        (model, vectorizer),
        f
    )

print("Model Saved")




'''print(f"Accuracy: {accuracy * 100:.2f}%")

while True:
    msg = input("\nEnter message: ")
    vec = vectorizer.transform([msg])
    prediction = model.predict(vec)[0]
    probs = model.predict_proba(vec)[0]

    print()
    print("Prediction:", prediction)
    print(f"Ham Confidence : {probs[0]*100:.2f}%")
    print(f"Spam Confidnce: {probs[1]*100:.2f}%")

    spam_conf = probs[1] * 100

    if spam_conf >= 80:
        print("Risk level: HIGH")
    elif spam_conf >= 50:
        print("Risk level: MEDIUM")
    else:
        print("Risk level: LOW")
'''


