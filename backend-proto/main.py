#!/usr/bin/env python3

# Source: https://fastapi.tiangolo.com/tutorial/first-steps/
# Run with `uvicorn main:app --reload`

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
