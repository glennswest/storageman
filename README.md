# StorageMan

A web-based management interface for NVMe storage targets. Provides a dashboard and REST API for viewing and managing NVMe target devices.

## Features

- Web dashboard with interactive data grid (Tabulator.js)
- REST API for querying NVMe targets
- RQLite distributed database for node tracking
- Flask-based backend with SQLAlchemy ORM

## Tech Stack

**Backend:**
- Flask 3.1.0
- SQLAlchemy 2.0 with Flask-SQLAlchemy
- RQLite (distributed SQLite) via pyrqlite
- Flask-Migrate for database migrations
- Gunicorn for production deployment

**Frontend:**
- Tabulator.js for data tables
- jQuery 3.7.1

## Requirements

- Python 3.x
- Podman (for RQLite container)
- nvmetarget library (external dependency)

## Installation

1. Clone the repository and create a virtual environment:
```bash
cd storageman
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the RQLite database container:
```bash
./bin/run-rqlite.sh
```

3. Initialize the database schema:
```bash
flask --app ./setup_schema.py db init
flask --app ./setup_schema.py db migrate -m "Initial migration"
flask --app ./setup_schema.py db upgrade
```

4. Install the nvmetarget dependency:
```bash
pip install ../nvmetarget
```

## Running

**Development:**
```bash
./bin/bootstrap.sh
```
Or manually:
```bash
export FLASK_APP=./storageman.py
flask --debug run -h 0.0.0.0
```

**Production:**
```bash
gunicorn -w 4 -b 0.0.0.0 'storageman:app'
```

The application will be available at http://localhost:5000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web dashboard |
| GET | `/api/v1/devices` | Returns list of NVMe targets |
| GET | `/js/<path>` | Static JavaScript files |
| GET | `/css/<path>` | Static CSS files |

## Database Schema

The `Node` model tracks NVMe storage nodes:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| name | String(128) | Node name (indexed) |
| ip | String(32) | IP address (indexed) |
| enable | Boolean | Whether node is enabled |
| alive | Boolean | Node health status |

## Configuration

Environment variables are loaded from `.env`:

```
SQLALCHEMY_DATABASE_URI=rqlite+pyrqlite://localhost:4001/
```

## Project Structure

```
storageman/
├── storageman.py        # Main Flask application
├── setup_schema.py      # Database models and migration setup
├── requirements.txt     # Python dependencies
├── .env                 # Environment configuration
├── templates/
│   └── index.html       # Dashboard template
├── js/                  # JavaScript libraries
├── css/                 # Tabulator CSS themes
├── migrations/          # Alembic database migrations
└── bin/
    ├── bootstrap.sh     # Development server runner
    ├── run-rqlite.sh    # RQLite container launcher
    ├── build-rqlite.sh  # RQLite build script
    └── deploy.sh        # Production deployment
```

## Development Status

Work in progress. The nvmetarget dependency is currently commented out in the codebase.
