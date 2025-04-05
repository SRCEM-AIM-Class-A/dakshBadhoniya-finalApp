# 🧩 Final Fullstack App (Flask + Django)

This project runs a Flask-based microservice alongside a Django-powered main application using Docker Compose. It is structured for modularity and easy deployment.

---

## 📁 Project Structure

```
dakshBadhoniya-finalApp/
│
├── docker-compose.yml
├── Dockerfile-flask
├── Dockerfile-django
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── greeting.html
│
└── django-app/
    ├── manage.py
    ├── requirements.txt
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── documents.html
    │   └── user.html
    └── django_app/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── asgi.py
    ├── dashboard/
    │   └── ...
    ├── documents/
    │   └── ...
    └── user/
        └── ...
```

---

## 🐍 Flask App

A simple Python Flask app displaying a greeting.

### 🔨 Build Image

```bash
docker build -t pilcrow3000/final-flask-app -f Dockerfile-flask ./flask_app
```

### ▶️ Run Container

```bash
docker run -p 5000:5000 pilcrow3000/final-flask-app
```

### 🌐 Access

[http://localhost:5000/hello](http://localhost:5000/hello)

---

## 🧠 Django App

A structured Django project with three apps: `dashboard`, `documents`, and `user`.

### 🔨 Build Image

```bash
docker build -t pilcrow3000/final-django-app -f Dockerfile-django ./django-app
```

### ▶️ Run Container

```bash
docker run -p 8000:8000 pilcrow3000/final-django-app
```

### 🌐 Access

[http://localhost:8000](http://localhost:8000)

---

## 🧰 Docker Compose (Run Both)

```bash
docker-compose up --build
```

This runs both apps simultaneously using `Dockerfile-flask` and `Dockerfile-django`.

### 🌐 Access the Apps

- **Flask App** → [http://localhost:5000/hello](http://localhost:5000/hello)
- **Django App** → [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Hub Images

- [Flask Image - pilcrow3000/final-flask-app](https://hub.docker.com/r/pilcrow3000/final-flask-app)
- [Django Image - pilcrow3000/final-django-app](https://hub.docker.com/r/pilcrow3000/final-django-app)

---

## 📬 Contact

Created by **Daksh Badhoniya**  
📧 Email: [dakshbadhoniya1@gmail.com](mailto:dakshbadhoniya1@gmail.com)

---
