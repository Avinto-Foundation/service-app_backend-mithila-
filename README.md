# Service-App Backend
 
The REST API behind Service-App: handles accounts, service listings, categories, and ratings so people can find and review local services like plumbers, electricians, and cleaners.
 
## Quick start
 
Docker isn't set up yet for this project — for now, clone the repo and follow [Setup](#setup) below. Once it's running, the app is available at `http://localhost:8000`.
 
## Features
 
- User accounts with token-based authentication
- Service listings with categories
- Service ratings
- REST API (Django REST Framework)
- SQLite database — no separate DB server to install
## Tech stack
 
- Python, Django, Django REST Framework
- SQLite
- Data tooling:asgiref==3.12.1
    - Django==6.1
    - djangorestframework==3.18.0
    - djangorestframework_simplejwt==5.5.1
    - PyJWT==2.13.0
    - sqlparse==0.5.5
    - tzdata==2026.3(only in windows)
(see `requirements.txt`)


## Project structure
 
```text
backend_service-app/
├── accounts/
├── categories/
├── ratings/
├── services/
├── backend_service_app/      # Django project settings & urls
├── manage.py
├── requirements.txt
├── seed_data.py
├── Dockerfile
├── .dockerignore
└── .gitignore
```
 
## Setup
 
### Requirements
 
- Python 3.14+
- pip
- Git
This project uses SQLite, so there's no separate database server to install or configure.
 
### Installation
 
1. **Clone the repo**
```bash
   git clone https://github.com/<your-username>/backend_service-app.git
   cd backend_service-app
```
 
2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate       # macOS / Linux
   venv\Scripts\activate          # Windows
```
 
3. **Install dependencies**
```bash
   pip install -r requirements.txt
```
 
4. **Run migrations**
```bash
   python manage.py migrate
```
 
   This creates `db.sqlite3` with all the tables. It starts out empty.
 
5. **Create a superuser** (needed for `/admin`)
```bash
   python manage.py createsuperuser
```
 
6. **(Optional) Add services, then backfill their images**
   `seed_data.py` only *updates* services that already exist (matched by name) — it doesn't create them. Add a few through `/admin` or the API first, then run:
```bash
   python seed_data.py
```
 
7. **Start the server**
```bash
   python manage.py runserver
```
 
## Configuration
 
Settings live in `backend_service_app/settings.py`. There's no `.env.example` in the repo yet, so check that file directly for things like `SECRET_KEY` and `DEBUG`. `.env` is already listed in `.gitignore`, so if you add environment-specific config later, that's where it goes.
 
## Usage
 
```bash
# Web server
python manage.py runserver
```
 
- Admin panel: `http://localhost:8000/admin/` — log in with the superuser you created
- API routes are defined per app (`accounts/`, `categories/`, `ratings/`, `services/`) — check `backend_service_app/urls.py` for the exact paths
- Backfill service images any time with `python seed_data.py`
## Troubleshooting
 
**`ModuleNotFoundError` right after installing dependencies**
Your virtual environment probably isn't active. Re-run the activate command from step 2, then try again.
 
**`django.db.utils.OperationalError: no such table`**
You haven't run migrations yet — run `python manage.py migrate`.
 
**`seed_data.py` prints "Updated 0 service image URLs."**
It only updates services that already exist and match by name (see the list inside `seed_data.py`). Add those services first, then re-run it.
 
**Port 8000 already in use**
Run on a different port: `python manage.py runserver 8001`.
 
## Contributing
 
```bash
python manage.py test
```

 