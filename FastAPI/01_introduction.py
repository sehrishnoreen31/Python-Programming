from fastapi import FastAPI
import uvicorn

# declare app object
app = FastAPI()

@app.get("/")
async def index():
    return {'message': 'Hello World'} # dict

@app.get("/list/")
async def return_list():
    return [1,2,3,4,5] # list

@app.get("/tuple/")
async def return_tuple():
    return (1,2,3,45,5) # tuple

@app.get("/set/")
async def return_set():
    return {1,2,3,40} # set

# use uvicorn 01_introduction:app --reload 

# or
if __name__ == "__main__":
    uvicorn.run("01_introduction:app", host="127.0.0.1", port=8000, reload=True)
# run simply with python 01_introduction.py