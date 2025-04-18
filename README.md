# 📬 Clearmail

A simple Django web app that uses a trained machine learning model to detect whether a message is **spam** or **not spam**.

## ✨ Features

- 🧠 ML-based spam detection (Naive Bayes classifier)
- 🖥️ Paste message directly into a clean web interface
- ⚡ Built with Django + Tailwind CSS
- 🧪 Includes trained model: `spam_model.pkl`

## 🚀 Quick Start

```bash
# Clone the repo
git clone git@github.com:nic-thompson/clearmail.git
cd clearmail

# Run setup script
chmod +x setup_and_run.sh
./setup_and_run.sh
```

Then open your browser at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📸 Screenshot

> _(Paste a screenshot here of the form + prediction result)_

## 🧠 Tech Stack

- Django 5.2
- Python 3.11+
- scikit-learn
- Tailwind CSS
- joblib (for loading the saved model)

## 🛠 Project Structure

```
clearmail/
├── clearmail/         # Django project settings
├── spam_api/          # App with views, model, templates
├── manage.py
├── setup_and_run.sh   # Automates venv + install + runserver
└── spam_model.pkl     # Pretrained spam detector
```

## 🧪 Model Details

- Trained on a small toy dataset for demo purposes
- Uses `CountVectorizer` + `MultinomialNB`
- You can easily retrain on a larger dataset

## 📄 License

MIT License — free to use, fork, and build on!
