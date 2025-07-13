'''
포트 확인 : netstat -ano | findstr 8000
포트 종료 : taskkill /f /pid [pid number] ex taskkill /f /pid 8000
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world"}


@app.get("/dev")
async def dev():
    return {"info" : "dev's channel"}

@app.get("/item/{item}")
async def items(item):
    return {"item" : item}