from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime,timezone

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; you can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    current_datetime_utc = datetime.now(timezone.utc)
    iso_8601_utc = current_datetime_utc.isoformat(timespec="seconds").replace("+00:00", "Z")

    return {
  "email": "anoffcaleb@gmail.com",
  "current_datetime": iso_8601_utc,
  "github_url": "https://github.com/Anofff/HNG12-PublicAPI"
}   