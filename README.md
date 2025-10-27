# digittwin-config

A FastAPI-based configuration management API for Digital Twin.

## Features

- FastAPI framework for high-performance API development
- RESTful API endpoints
- Automatic API documentation (Swagger UI and ReDoc)
- Health check endpoint

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sunshinezxf/digittwin-config.git
cd digittwin-config
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint

## Development

To run the server with custom host and port:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## License

This project is licensed under the MIT License.