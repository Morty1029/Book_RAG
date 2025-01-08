import uvicorn
import os
from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv


load_dotenv(".env")
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

app = FastAPI(title="back")
app.include_router(router)


def main():
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
