from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag.engine import rag_engine

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
async def query_rag(request: QueryRequest):
    try:
        results = rag_engine.query(request.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG query failed: {str(e)}")
