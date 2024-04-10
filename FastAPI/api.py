import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()  


class Inputs(BaseModel):
   inp: int
   inp2: str


@app.get("/exemplo")
def example() -> str:
   return "Olá Mundo"

@app.post("/exemplo2")
def example2(inputs: Inputs) -> str:
   return inputs.inp2

if __name__ == "__main__":
   uvicorn.run(app, port=8000)

