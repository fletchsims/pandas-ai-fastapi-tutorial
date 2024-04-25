from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config.config import create_agent_instance

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

agent = create_agent_instance()


@app.get("/chat")
async def get_my_chat(prompt: str):
    return agent.chat(prompt)