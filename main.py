from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["GET"],  
    allow_headers=["*"],  
)

@app.get("/")
async def get_info():
    return {
        "email": "labanrotich6544@gmail.com", 
        "current_datetime": datetime.utcnow().isoformat() + "Z", 
        "github_url": "https://github.com/Laban254/backend-stg0", 
    }