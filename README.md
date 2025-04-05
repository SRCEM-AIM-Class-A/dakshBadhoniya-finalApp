# 🧩 FinalApp — Combined Flask & Django Microservices

This project is a full-stack application combining a **Flask microservice** and a **Django-based web system** using Docker Compose. The system is modular, scalable, and suitable for modern web deployment and containerization practices.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Docker
- Docker Compose

### 🔧 Build & Run the Project

```bash
docker-compose up --build
```

---

## 🗂 Project Structure

```
dakshBadhoniya-finalApp/
│
├── docker-compose.yml
├── Dockerfile-django
├── Dockerfile-flask
│
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── greeting.html
│
├── django_app/
│   ├── manage.py
│   ├── requirements.txt
│   ├── django_app/                 # Django config package
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── dashboard/                  # App 1
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── documents/                  # App 2
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── user/                       # App 3
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   └── templates/                 # Shared HTML templates
│       ├── base.html
│       ├── dashboard.html
│       ├── document_list.html
│       └── profile.html
```

---

## 🌐 Flask App Overview

- Serves a simple greeting page at `/hello`
- Lightweight and minimal for quick response microservices

---

## 🛠 Django App Overview

- Fully-featured Django project with:
  - User authentication system
  - Dashboard display
  - Document handling
- Modular apps:
  - `dashboard`: UI summaries
  - `documents`: CRUD operations
  - `user`: profile & auth

---

## 📦 Docker Compose Services

- `flask`: Flask microservice container
- `django`: Django web app container

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Author

Created by Daksh Badhoniya and team.
