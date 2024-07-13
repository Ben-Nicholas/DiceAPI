from fastapi import FastAPI
import random
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/random")
def random_number():
    return random.randint(1, 6)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)