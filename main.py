import os
from pickletools import int4

import uvicorn
from fastapi import FastAPI
from router import user




app = FastAPI()


app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001, log_level="info")