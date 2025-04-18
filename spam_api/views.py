import joblib
from django.shortcuts import render

vectorizer, model = joblib.load("spam_api/spam_model.pkl")

def index(request):
    prediction = None
    if request.method == "POST":
        message = request.POST.get("message", "")
        X = vectorizer.transform([message])
        pred = model.predict(X)[0]
        prediction = "Spam" if pred == 1 else "Not Spam"
    return render(request, "spam_api/index.html", {"prediction": prediction})
