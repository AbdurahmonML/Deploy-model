
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()
 
model = joblib.load('models/model.pkl')

class InputData(BaseModel):
    MedInc: float  # Median Income in block group
    HouseAge: float  # Median house age in block group
    AveRooms: float  # Average number of rooms per household
    AveOccup: float  # Average number of household members
    Latitude: float  # Latitude of the block group
    Longitude: float  # Longitude of the block group
    Population: float  # Population in the block group
    Households: float  # Number of households in the block group

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
