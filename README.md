#  Resume Collector API

A REST API built using FastAPI that allows users to upload resumes,
store candidate details, filter candidates, and delete resumes.

------------------------------------------------------------------------

#  Python Version

This project was developed using:

Python 3.11.9

------------------------------------------------------------------------

#  Installation Steps

##  Clone the Repository

https://github.com/YASARAR33/Mini-Resume-Collector.git
cd resume-api

##  Create Virtual Environment

python -m venv venv

Activate Virtual Environment:

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source venv/bin/activate

##  Install Required Dependencies

pip install fastapi uvicorn python-multipart

------------------------------------------------------------------------

#  Steps to Run the Application

Run the FastAPI server using:

uvicorn main:app --reload

Application will start at:

http://127.0.0.1:8000

------------------------------------------------------------------------

# API Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

# Example API Request & Response

## Example: Upload Resume

POST /resume

Form Data:

name: John Doe\
dob: 2000-05-10\
email: john@example.com\
phone: 9876543210\
address: Kerala, India\
education: B.Tech Computer Science\
graduation_year: 2022\
skills: Python\
skills: FastAPI\
experience: 2\
file: resume.pdf

### Example Success Response

{ "message": "Resume uploaded successfully", "resume_id": 1 }

------------------------------------------------------------------------

## Example: Get Resume by ID

GET /resume/1

### Example Response

{ "id": 1, 
"name": "John Doe", 
"dob": "2000-05-10", 
"email":"john@example.com",
"phone": "9876543210",
"address": "Kerala, India",
"education": "B.Tech Computer Science", 
"graduation_year": 2022,
"skills": \["Python", "FastAPI"\], 
"experience": 2, 
"file_path":"uploads/resume.pdf" }

------------------------------------------------------------------------

# Error Handling

400 → Invalid file type\
404 → Resume not found

------------------------------------------------------------------------

#  Current Limitations

-   Data stored in memory (no database)
-   Files saved locally
-   No authentication
-   File overwrite possible if same filename uploaded

------------------------------------------------------------------------


