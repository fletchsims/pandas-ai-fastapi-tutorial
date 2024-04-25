# pandas-ai-fastapi-tutorial

Quick example of using Pandas AI and FastAPI to create a simple RESTAPI service.

# How to get started
- Install required dependencies: `pip isntall -r requirements.txt`
- Use some sort of data (json, parquet, csv, etc.)
- Start the server from root directory: `uvicorn app.main:app --host 0.0.0.0 --port 8080`