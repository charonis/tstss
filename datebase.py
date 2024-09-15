from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings




engine = create_async_engine(
    settings.DATABASE_URL_ASYNC_PSYCOPG,
    # echo = True
)



session_async = async_sessionmaker(engine)


# async def get_123():
#     async with engine.connect() as conn:
#         res = await conn.execute(text("SELECT 1,2,3 UNION select 4,5,6"))
#         print(f"{res.first()=}")


