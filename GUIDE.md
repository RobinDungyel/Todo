# Guide: Create repo, run app locally, and run CI/CD

1. Initialize git and push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Django Todo JWT"
gh repo create yourusername/todo-django --private --source=. --remote=origin --push
```
(Or create repo manually and push)

2. Set GitHub secrets (for CD pipeline)
- DOCKERHUB_USERNAME: your Docker Hub username
- DOCKERHUB_TOKEN: a Docker Hub access token (not your password)

3. Local run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Register at `POST /api/auth/register/` and obtain token at `POST /api/auth/token/`.

4. Run tests locally
```bash
pytest
# or
python manage.py test
```

5. CI & CD behavior
- On push to `main`, CI runs tests and linting.
- If CI passes, CD builds a Docker image and pushes to Docker Hub with tags `latest` and the commit SHA.
