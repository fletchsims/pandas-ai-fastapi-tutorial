# pandas-ai-fastapi-tutorial

Quick example of using Pandas AI and FastAPI to create a simple REST API service.

# How to get started
- Install required dependencies: `pip install -r requirements.txt`
- Python 3.11+
- Use some sort of data (json, parquet, csv, etc.). The demo example I use is NY Taxi Yellow Cab Trip Data 2023-01 (parquet).
- Start the server from root directory: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
    - Example URL and usage: 
        - `http://0.0.0.0:8080/chat?prompt='{your prompt goes here}'`
        - `http://0.0.0.0:8080/chat?prompt='show me the top 3 records'`
