from datetime import date
from fastapi import FastAPI,UploadFile,Form,File,HTTPException
from pydantic import BaseModel
from typing import List,Optional
import os

app = FastAPI()

resume=[]
resume_id=1

Upload_folder='uploads'
if not os.path.exists(Upload_folder):
    os.makedirs(Upload_folder) 

@app.get("/")
def home():
    return {"message":"Welcome"}
@app.get("/health")
def health():
    return {"message":"Healthy"}
@app.post("/resume",status_code=201)
async def upload_resume(
    name: str = Form(...),
    dob:date=Form(...),
    email:str=Form(...),
    phone:str=Form(...),
    address:str=Form(...),
    education:str=Form(...),
    graduation_year:int=Form(...),
    skills:List[str]=Form(...),
    experience:int=Form(...),
    file:UploadFile=File(...)
    
):
    global resume_id

    allowed_extensions=["pdf","docx"]
    file_extension=file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400,detail="Invalid file type. Only PDF and DOCX are allowed.")
    

    file_location=os.path.join(Upload_folder,file.filename)
    with open(file_location,"wb") as f:
        f.write(await file.read())
    
    resume_data={
        "id":resume_id,
        "name":name,
        "dob":dob,
        "email":email,
        "phone":phone,
        "address":address,
        "education":education,
        "graduation_year":graduation_year,
        "skills":skills,
        "experience":experience,
        "file_path":file_location
    }
    resume.append(resume_data)
    resume_id+=1
    return {"message":"Resume uploaded successfully","resume_id":resume_data["id"]}

@app.get("/resume/{resume_id}")
def get_resume(resume_id:int):
    for r in resume:
        if r["id"]==resume_id:
            return r
    return HTTPException(status_code=404,detail="Resume not found")

@app.get("/resumes")
def list_resumes(
    skill:Optional[str]=None,
    experience:Optional[int]=None,
    graduation_year:Optional[int]=None
):
    filtered_resumes=resume
    if skill:
        filtered_resumes=[r for r in filtered_resumes if skill in r["skills"]]
    if experience is not None:
        filtered_resumes=[r for r in filtered_resumes if r["experience"]>=experience]
    if graduation_year is not None:
        filtered_resumes=[r for r in filtered_resumes if r["graduation_year"]==graduation_year]
    
    return filtered_resumes

@app.delete("/resume/{resume_id}")
def delete_resume(resume_id:int):
    for r in resume:
        if r["id"]==resume_id:
            resume.remove(r)
            os.remove(r["file_path"])
            return {"message":"Resume deleted successfully"}
    return {"message":"Resume not found"}