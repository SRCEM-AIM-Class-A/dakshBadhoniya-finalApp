# Flask & Django Web Applications with Docker Compose

## 📌 Overview

This project demonstrates the development and deployment of two simple web applications built using Flask and Django frameworks, containerized using Docker, and orchestrated with Docker Compose.

- 🧠 **Flask App:** A basic app showcasing routing, forms, and input validation.
- 🏗️ **Django App:** A full-stack application that lists documents, allows item creation, deletion, and includes an admin panel.
- 🐳 **Docker Compose:** Both apps run in isolated containers and are exposed via different ports locally.

---

## 🚀 Technologies Used

- Python 3
- Flask
- Django
- Docker
- Docker Compose
- HTML/CSS (Bootstrap 4)

---

## 📁 Project Structure

```
project-root/
│
├── flask_app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   │   └── greet.html
│   └── Dockerfile
│
├── django_app/
│   ├── myproject/
│   ├── documents/
│   │   └── templates/documents/document_list.html
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🔥 Features

### Flask App
- 🏠 Homepage that says **"Hello, World!"**
- 📥 Form for user's name and age.
- 🙅 Error handling for invalid inputs.

### Django App
- 📃 Homepage displays list of documents (pre-filled).
- ➕ Add new documents.
- ❌ Delete existing documents.
- 🔐 Admin panel to manage documents.

---

## 🛠️ How to Run

### 🚨 Prerequisites:
- Docker installed
- Docker Compose installed

---

### 🧪 Steps to Run Locally:

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/flask-django-docker-app.git
cd flask-django-docker-app
```

2. **Build and Start Containers:**

```bash
docker-compose up --build
```

3. **Access Applications:**
- Flask App: [http://localhost:5000](http://localhost:5000)
- Django App: [http://localhost:8000](http://localhost:8000)
- Django Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

### 🔑 Django Admin Credentials

| Field       | Value        |
|-------------|--------------|
| Username    | admin        |
| Password    | admin123     |

---

## 🐋 Docker Hub Links

- Flask Image: [https://hub.docker.com/r/pilcrow3000/final-flask-app](https://hub.docker.com/r/pilcrow3000/final-flask-app)
- Django Image: [https://hub.docker.com/r/pilcrow3000/final-django-app](https://hub.docker.com/r/pilcrow3000/final-django-app)

---

## 👤 Developer

**Daksh Badhoniya**  
📫 Email: dakshbadhoniya1@gmail.com  
📍 Location: Nagpur, India  
💼 Aspiring AIML Engineer
