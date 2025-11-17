from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Create the instrumentator
instrumentator = Instrumentator()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    return {"input": text, "prediction": "placeholder"}

# Register the instrumentator with the app
instrumentator.instrument(app).expose(app)
