# CreatorOS

A personal system for managing the production pipeline of social media content. Designed for solo creators who want to organize ideas, scripts, videos, and publishing schedules without spending time browsing social media platforms.

## Prerequisites

- **Python 3.10+**
- **Docker** (Optional, if you want to use the included PostgreSQL database instead of the default SQLite).

## Quick Start (Local Setup)

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run database migrations**:
   By default, the project uses a local SQLite database for maximum portability (`db.sqlite3`).
   ```bash
   python manage.py migrate
   ```

   *(Optional)* If you want to use PostgreSQL, start the docker container and then run migrations:
   ```bash
   docker-compose up -d
   # Check if python works, if you get an error with psycopg2, ensure you are in the venv
   python manage.py migrate
   ```

3. **Create a superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the application**:
   Open a browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Features

- **Content Ideas:** Store and prioritize ideas across multiple platforms (TikTok, YouTube Shorts, etc.).
- **Production Pipeline:** Drag-and-drop Kanban board to move ideas from Scripting to Published.
- **Media Library:** Upload and preview your videos and thumbnails locally.
- **Content Calendar:** Keep track of when all your scheduled content is going live.
- **Minimal Dashboard:** See at a glance what needs to be published next.
