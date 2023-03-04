from fastapi import FastAPI
import asyncio
from app.configuration.server import Server


def create_app(_=None) -> FastAPI:
    
    app = FastAPI()
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    return Server(app).get_app()