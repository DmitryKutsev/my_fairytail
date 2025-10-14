# My Fairy Tale

A Django-based catalogue of interconnected fairy tales featuring keyword and rubric-style search.

## Features

- Django project with a single `FairyTale` model capturing title, content, author, country, and self-referential relationships for predecessors, successors, and similar tales.
- Keyword search across fairy tale titles and contents, plus rubric filters by author and country.
- Sample dataset loader (`python manage.py load_sample_stories`) to populate the database with interconnected tales.
- Docker Compose setup with separate containers for the Django web application and a PostgreSQL database.

## Getting started

### Requirements

- Docker and Docker Compose

### Running the project

1. Build and start the services:
   ```bash
   docker compose up --build
   ```
2. Apply migrations and load the sample data (done automatically when the web container starts). To reload sample data manually:
   ```bash
   docker compose exec web python manage.py load_sample_stories
   ```
3. Visit [http://localhost:8000](http://localhost:8000) to explore the fairy tale search interface.

### Local development without Docker

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Export PostgreSQL connection variables or set `DJANGO_USE_SQLITE=1` for a lightweight SQLite database during development.
3. Run migrations and load sample data:
   ```bash
   python manage.py migrate
   python manage.py load_sample_stories
   python manage.py runserver
   ```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
