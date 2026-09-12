# Django Chat App

A real-time chat application built with Django, featuring user authentication, room management, and image uploads.

## Features
- User authentication & profiles
- Create and join chat rooms
- Real-time messaging
- Image uploads (Cloudinary)
- User-friendly interface

## Tech Stack
- Django 6.1
- PostgreSQL
- Cloudinary (image storage)
- Bootstrap (frontend)
- Render (hosting)

## Live Demo
[Visit the app](https://django-code-prd-rsi5.onrender.com/)

## Setup Locally
```bash
git clone https://github.com/yourusername/django-chat-app.git
cd django-chat-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Deployment
Deployed on Render with automatic CI/CD from GitHub.
