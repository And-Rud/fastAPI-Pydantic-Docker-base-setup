from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import delete_tables, create_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB is clear")
    await create_tables()
    print("DB is ready")
    yield
    print('Disconnecting')

app = FastAPI(lifespan=lifespan)

#add new router
app.include_router(task_router)




