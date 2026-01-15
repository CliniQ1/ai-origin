# AI Content Analysis Service

This project is a FastAPI backend skeleton for an AI content analysis service. It provides endpoints for uploading files, checking the status of analysis tasks, and retrieving analysis results. The project is designed to be production-ready with a clear folder structure and is Docker-ready.

## Project Structure

```
ai-detector/
├── src/
│   ├── app/
│   │   ├── main.py                # Entry point of the FastAPI application
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── upload.py  # Endpoint for async file uploads
│   │   │       │   ├── status.py   # Endpoint to check analysis status
│   │   │       │   └── result.py   # Endpoint to retrieve analysis results
│   │   │       └── __init__.py
│   │   ├── core/
│   │   │   ├── config.py          # Application configuration settings
│   │   │   └── logger.py          # Logging setup
│   │   ├── db/
│   │   │   ├── base.py            # Base class for SQLAlchemy models
│   │   │   ├── session.py         # Database session management
│   │   │   └── models.py          # Database models for tasks
│   │   ├── crud/
│   │   │   └── tasks.py           # CRUD operations for tasks
│   │   ├── schemas/
│   │   │   └── task.py            # Pydantic schemas for task data
│   │   ├── services/
│   │   │   ├── queue.py           # Interaction with Redis as a task queue
│   │   │   └── worker_placeholder.py # Placeholder logic for task processing
│   │   └── utils/
│   │       ├── storage.py         # Utility functions for file storage
│   │       └── sio.py             # Utility functions for socket interactions
│   ├── alembic/
│   │   ├── env.py                 # Alembic migration tool setup
│   │   ├── script.py.mako         # Template for migration scripts
│   │   └── versions/              # Migration scripts directory
│   └── tests/
│       ├── test_upload.py         # Unit tests for upload endpoint
│       └── test_status.py         # Unit tests for status endpoint
├── docker/
│   ├── web/
│   │   └── Dockerfile             # Docker configuration for web service
│   └── worker/
│       └── Dockerfile             # Docker configuration for worker service
├── docker-compose.yml              # Docker services configuration
├── .env.example                    # Example environment variables
├── alembic.ini                     # Alembic configuration file
├── pyproject.toml                  # Python project configuration
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-detector
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database and run migrations:
   ```
   alembic upgrade head
   ```

5. Start the application:
   ```
   uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Usage

- **Upload Files**: Use the `/api/v1/upload` endpoint to upload files (text, image, video).
- **Check Status**: Use the `/api/v1/status` endpoint to check the status of an analysis task using the `session_id`.
- **Retrieve Results**: Use the `/api/v1/result` endpoint to get the analysis results based on the `session_id`.

## Docker

To run the application using Docker, use the following command:
```
docker-compose up --build
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.