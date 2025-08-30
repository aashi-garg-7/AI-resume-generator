from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ResumeRequest(BaseModel):
    name: str
    job_role: str
    skills: list[str]

@app.post("/generate_resume/")
def generate_resume(req: ResumeRequest):
    resume = (
    f"# Resume\n\n"
    f"## Name: {req.name}\n\n"
    f"### Applying for: {req.job_role}\n\n"
    f"### Skills:\n"
    f"- " + "\n- ".join(req.skills)
)
    return {"resume_text": resume}
