
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()
 
model = joblib.load('models/model.pkl')

class InputData(BaseModel):
    MedInc: float  
    HouseAge: float  
    AveRooms: float  
    AveOccup: float  
    Latitude: float 
    Longitude: float  
    Population: float  
    Households: float  

@app.post("/predict/")
async def predict(data: InputData):
    try:
        # Prepare the input for the model
        input_data = [[
            data.MedInc, data.HouseAge, data.AveRooms, data.AveOccup,
            data.Latitude, data.Longitude, data.Population, data.Households
        ]]
        
        prediction = model.predict(input_data)
        
        prediction_value = prediction[0].item() 
        
        return {"prediction": prediction_value}
    except Exception as e:
        print(f"Error occurred: {str(e)}")  
        raise HTTPException(status_code=500, detail=str(e))
