# dakshBadhoniya-finalApp

# Final Project: Django & Flask Web Applications

This project contains two web applications:

- **Django App**: A modular web application featuring three sub-apps:
  - **Users**: Contains a personalized profile page.
  - **Dashboard**: Provides an overview with statistics and activity cards.
  - **Documents**: Lists and manages documents.

- **Flask App**: A lightweight web application serving a modern, Bootstrap-styled website.

Both applications are containerized using Docker and orchestrated via Docker Compose.

## Project Structure

finalProject/ <br>
├── docker-compose.yml <br>
├── Dockerfile-django <br>
├── Dockerfile-flask <br>
├── django_app/ <br>
│   ├── manage.py <br>
│   ├── myproject/ <br>
│   │   ├── settings.py <br>
│   │   ├── urls.py <br>
│   │   └── wsgi.py <br>
│   ├── users/ <br>
│   │   ├── views.py <br>
│   │   └── urls.py <br>
│   ├── dashboard/ <br>
│   │   ├── views.py <br>
│   │   └── urls.py <br>
│   ├── documents/ <br>
│   │   ├── views.py <br>
│   │   └── urls.py <br>
│   ├── templates/ <br>
│   │   ├── base.html <br>
│   │   ├── profile.html <br>
│   │   ├── dashboard.html <br>
│   │   └── document_list.html <br>
│   └── static/ <br>
│       └── css/ <br>
│           └── style.css <br>
└── flask_app/ <br>
    ├── app.py <br>
    ├── requirements.txt <br>
    ├── templates/ <br>
    │   └── index.html <br>
    └── static/ <br>
        └── css/ <br>
            └── style.css <br>

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.
- A Docker Hub account (if you plan to push images).

## Running the Applications

### With Docker Compose

1. **Build and Start Containers**  
   From the project root (`finalProject/`), run:
   docker-compose up --build
2. **Access the Apps**  
   - **Django App**:  
     - Home (Dashboard): [http://localhost:8000/](http://localhost:8000/)  
     - Users Profile: [http://localhost:8000/users/profile/](http://localhost:8000/users/profile/)
     - Documents: [http://localhost:8000/documents/](http://localhost:8000/documents/)
   - **Flask App**: [http://localhost:5000/](http://localhost:5000/)

## Building & Pushing Docker Images

### Build Images

- **Django Image:**
  docker build -t pilcrow3000/final-django-app:latest -f Dockerfile-django .

- **Flask Image:**
  docker build -t pilcrow3000/final-flask-app:latest -f Dockerfile-flask .

### Push Images to Docker Hub

Make sure you're logged in with:
docker login
Then push each image:

- **Django Image:**
  docker push pilcrow3000/final-django-app:latest

- **Flask Image:**
  docker push pilcrow3000/final-flask-app:latest
## About

- **Django App**: Built with Django 5.1.7, it showcases a multi-app architecture with a centralized template system and Bootstrap-enhanced styling.
- **Flask App**: A lightweight Flask application featuring a modern, responsive website.

## Author

**Daksh Badhoniya**  
Email: [dakshbadhoniya1@gmail.com](mailto:dakshbadhoniya1@gmail.com)  
Location: Nagpur, India  
AI/ML Engineer

## License

This project is licensed under the [MIT License](LICENSE).
