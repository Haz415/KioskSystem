import uvicorn
from fastapi import FastAPI

app = FastAPI()

uvicorn.run("port.py",port=8000, reload=True)  