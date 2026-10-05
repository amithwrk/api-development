from fastapi import FastAPI

app = FastAPI()

#home Route
@app.get("/")

def home():
    return {"message" : "Hello world with FASTAPI virtual environment"}


#about Route
@app.get("/about")

def about():
    return {"message" : "This is about page"}


#member Route
@app.get("/member")

def member():
    return {"users" : ["Mohit","Rohit","Amit"]}


