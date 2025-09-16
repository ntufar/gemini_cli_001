from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import Union, List

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # React frontend default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: Union[str, None] = None
    url: Union[HttpUrl, None] = None

class AnalyzeResponse(BaseModel):
    propaganda_score: float
    identified_techniques: List[str]
    explanation: str

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    from .utils import fetch_url_content

    content_to_analyze = ""
    if request.text:
        content_to_analyze = request.text
    elif request.url:
        content_to_analyze = fetch_url_content(str(request.url))
        if not content_to_analyze:
            raise HTTPException(status_code=400, detail="Could not fetch content from the provided URL.")
    else:
        raise HTTPException(status_code=400, detail="Either 'text' or 'url' must be provided.")
    
    from .gemini_service import analyze_text_with_gemini

    analysis_result = analyze_text_with_gemini(content_to_analyze)
    
    return AnalyzeResponse(
        propaganda_score=analysis_result["propaganda_score"],
        identified_techniques=analysis_result["identified_techniques"],
        explanation=analysis_result["explanation"]
    )
