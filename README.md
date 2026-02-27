# XRWVM Full Stack Developer Capstone

### Repository Name: xrwvm-fullstack_developer_capstone
### Project Name: XRWVM Full Stack Developer Capstone

This repository contains a containerized full-stack web application built using Django (backend) and Node/JavaScript (frontend). The project demonstrates full-stack development concepts including REST APIs, frontend integration, containerization, and deployment configuration.

## Project Architecture

The application consists of:

Django Backend

Frontend (Node/JavaScript)

Database

Dockerized Deployment Setup

## Getting Started
### Prerequisites

Make sure you have installed the following:

Python 3.x

Node.js (if frontend uses Node/React)

Docker & Docker Compose (optional but recommended)

### Backend Setup (Django)

Clone the repo

Navigate to the server folder:

cd server

### Install dependencies:

pip install -r requirements.txt

### Run database migrations:

python manage.py migrate

### Start development server:

python manage.py runserver

### Build and run the backend in a container:

docker build -t capstone-server ./server
docker run -p 8000:8000 capstone-server

Replace server with your backend directory if different.

## Contributing

Contributions and improvements are welcome!

Fork the repository

Create a feature branch

Submit a pull request

Make sure builds and tests pass before creating a PR.

## License

This project retains the original licensing as provided in the capstone template (usually Apache-2.0). Check the LICENSE file in the repo for full terms.

## Contact

For questions or support, open an issue or reach out to the repository maintainer.
