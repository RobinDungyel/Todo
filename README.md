# Django Todo Application (JWT auth)

A simple Django REST Framework based Todo app with JWT authentication (SimpleJWT). Each user can register, log in, and manage their own todos (full CRUD).

## Features
- JWT authentication (access + refresh via SimpleJWT)
- Per-user todos
- Unit tests for auth & CRUD
- Dockerfile for containerization
- GitHub Actions CI (lint, tests, migrations) and CD (build & push Docker image)
- SQLite by default; easily switch to PostgreSQL via environment variables

## Quick start (local)
1. Create virtualenv and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Run migrations and start server:
```bash
python manage.py migrate
python manage.py runserver
```
3. Register a user and obtain JWT tokens via the API endpoints.

## Project structure (important files)
- `todo_project/` - Django project
- `api/` - DRF app with models, views, serializers, tests
- `Dockerfile` - image built from python:3.12-slim
- `.github/workflows/ci.yml` - CI pipeline
- `.github/workflows/cd.yml` - CD pipeline (build & push to Docker Hub)

## GitHub Actions
- `ci.yml` runs on `push`/`pull_request` to `main` and performs:
  - checkout, setup Python, set up services (Postgres), install dependencies, run migrations, lint (flake8), run tests

- `cd.yml` runs after successful CI (on push to `main`) and:
  - builds Docker image, tags with `latest` and commit SHA, pushes to Docker Hub (requires DOCKERHUB_USERNAME & DOCKERHUB_TOKEN secrets)

## Docker
Build locally:
```bash
docker build -t yourusername/todo-django:latest .
docker run -p 8000:8000 yourusername/todo-django:latest
```

## Creating a repo & running CI/CD (short guide included in the repo)
See `GUIDE.md` in the zip for a step-by-step guide to create the GitHub repo and run the app.
