from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app import dynamic_memory_app

app = FastAPI()

# Allow CORS for your frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint (added to prevent Render's 404 error)
@app.get("/")
def read_root():
    return {"message": "Sigma Navigator API is running successfully!"}

# Health-check endpoint
@app.get("/healthz")
def health_check():
    return {"status": "healthy"}

# Chat endpoint for your frontend
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    question = body.get("question")
    history = body.get("history", [])
    state = {"question": question, "history": history}
    response = dynamic_memory_app.invoke(state)
    return response
