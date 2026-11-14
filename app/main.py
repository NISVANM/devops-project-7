from fastapi import FastAPI

app = FastAPI(title="DevOps CI/CD Project")

@app.get("/")
def home():
    return {
        "message": "Welcome to my DevOps CI/CD project!",
        "status": "Application is running successfully"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}