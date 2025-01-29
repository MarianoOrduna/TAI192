from fastapi import FastAPI 

app = FastAPI()

#endopoint home

@app.get("/")
def home():
    return{"hellow":"word FastAPI"}


