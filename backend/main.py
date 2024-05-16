from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

graphicsProject = FastAPI()

graphicsProject.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with your frontend URL
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@graphicsProject.get("/")
async def root():
    return {"message": "Our 630 Project"}


@graphicsProject.post("/receive_message")
async def receive_message(request: Request):
    data = await request.json()
    message = data.get('message')
    print(f"Received message: {message}")
    # Perform additional processing or storage of the message
    return {"message": "Message received successfully"}

