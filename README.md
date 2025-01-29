# HNG-PublicAPI
# FastAPI Public API for HNG12 Stage 0 Task

This repository contains a simple FastAPI-based public API that fulfills the HNG12 Stage 0 backend task requirements. The API provides basic information including the current UTC datetime, registered email address, and the GitHub repository URL.

## Features

- Provides the current UTC datetime in ISO 8601 format.
- Returns registered email and GitHub repository URL.
- Handles Cross-Origin Resource Sharing (CORS) with proper configuration.
- Designed to be deployed on a publicly accessible endpoint.

## API Endpoints

### **1. Root Endpoint**
**URL:** `/`

**Method:** `GET`

**Response Example:**
```json
{
  "email": "anoffcaleb@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Anofff/HNG12-PublicAPI"
}
```

## Requirements

- **Programming Language/Framework:** Python (FastAPI)
- **Deployment:** Hosted on a publicly accessible platform (e.g., Render).
- **Version Control:** Public GitHub repository.
- **Response Format:** JSON.

## Setup Instructions

### **1. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/Anofff/HNG12-PublicAPI.git
cd HNG12-PublicAPI
```

### **2. Install Dependencies**
Ensure you have Python 3.8+ installed, then run:
```bash
pip install -r requirements.txt
```

### **3. Run the API Locally**
Start the FastAPI server using Uvicorn:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### **4. Access the API**
- Base URL: `http://127.0.0.1:8000/`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Deployment Instructions

### **1. Deploy to Render**
This API can be deployed to Render. Follow these steps:

1. Push your code to GitHub.
2. Log in to [Render](https://render.com) and create a new Web Service.
3. Use the following configurations:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Deploy and note the public URL provided by Render.

### **2. Test the Public API**
Once deployed, access the API at the public URL, e.g.,:
```
https://your-app.onrender.com/
```

## Documentation

### API Specification
- **Endpoint:** `/`
- **Method:** `GET`
- **Response Format:** JSON

### Example Response
```json
{
  "email": "anoffcaleb@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Anofff/HNG12-PublicAPI"
}
```

## Additional Resources

For more details about HNG12 backend roles and hiring, visit:
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Golang Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)

## Contact

- **Email:** anoffcaleb@gmail.com
- **GitHub:** [Anofff](https://github.com/Anofff)


