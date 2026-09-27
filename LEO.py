from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Hello, Leo!"}

@app.get("/student/{name}")
def get_student(name: str):
    return {"student": name, "message": f"Hello,{name}!"}