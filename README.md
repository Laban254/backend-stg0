

# HNG Stage 0 Task - FastAPI Public API

This is a simple FastAPI application that returns basic information in JSON format. It fulfills the requirements for the HNG Stage 0 Backend Task.

---

## Table of Contents
1. [API Endpoint](#api-endpoint)
2. [Response Format](#response-format)
3. [Setup Instructions](#setup-instructions)
4. [Running the App Locally](#running-the-app-locally)
5. [API Documentation](#api-documentation)
6. [Technologies Used](#technologies-used)
7. [Backlink](#backlink)

---

## API Endpoint

- **URL**: `https://your-render-url.onrender.com/`
- **Method**: `GET`

---

## Response Format

The API returns the following JSON response:

```json
{
  "email": "labanrotich6544@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Laban254/backend-stg0",
}
```
----------

## Setup Instructions

### Prerequisites

-   Python 3.7 or higher
    
-   Git (optional, for cloning the repository)
    

### Steps

1.  Clone the repository:
    

    
    git clone https://github.com/Laban254/backend-stg0
    
2.  Navigate to the project directory:
    
    
    cd [backend-stg0]
    
3.  Install dependencies:
    
    pip install -r requirements.txt
    

----------

## Running the App Locally

1.  Start the FastAPI server
    
		  ``` uvicorn main:app --reload ```
    
2.  Open your browser or use a tool like Postman to test the API:
    
    -   Visit  `http://127.0.0.1:8000/`  to see the JSON response.

## API Documentation

### Endpoint

-   **URL**:  `https://your-render-url.onrender.com/`
    
-   **Method**:  `GET`
    

### Request

No request body or parameters are required.

### Response

-   **Status Code**:  `200 OK`
    
-   **Response Body**:
    

    
    {
      "email": "your-email@example.com",
      "current_datetime": "2025-01-30T09:30:00Z",
      "github_url": "https://github.com/Laban254/backend-stg0"
    }
    

----------

## Technologies Used

-   **Programming Language**: Python
    
-   **Framework**: FastAPI
    
-   **ASGI Server**: Uvicorn
    
-   **Deployment Platform**: Heroku
    
-   **Version Control**: Git, GitHub
    

----------

## Backlink

For more information about hiring Python developers, visit:  
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

----------

## Author

-   **Your Name** Laban Kibet
    
-   **Email**:  [Labanrotich6544@gmail.com](mailto:Labanrotich6544@gmail.com)
    
-   **GitHub**:  [laban254](https://github.com/laban254)
    

----------

## License

This project is licensed under the MIT License.