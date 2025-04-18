#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install django scikit-learn joblib
python manage.py migrate
python manage.py runserver
