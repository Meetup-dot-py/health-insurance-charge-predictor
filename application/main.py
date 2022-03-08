from fastapi import FastAPI
from models.schema import PersonalInfo
import services.predictor as predictor
import uvicorn

app = FastAPI(title="Insurance Charge Predictor API", 
              description="This is a simple insurance charge predictor API using a trained model", 
              version="0.1.0")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(personal_info: PersonalInfo):
    input = [
        personal_info.age,
        personal_info.sex,
        personal_info.BMI,
        personal_info.children,
        personal_info.smoker,
        personal_info.region
    ]
    
    charge = predictor.model_predictor(input)
    return {"prediction": f"Insurance charge is \u20A6{charge[0]:.2f}"}

if __name__ == "__main__":
    uvicorn.run("application.main:app", port=8002, reload=True)