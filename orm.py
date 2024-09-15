from datebase import engine, session_async
from models import Base
import asyncio 

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        

asyncio.run(init_models())