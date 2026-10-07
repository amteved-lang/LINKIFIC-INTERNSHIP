from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from support_router import route_support_query

app = FastAPI(
    title="HearMe Support Routing API",
    description=(
        "Routes customer queries to AI support "
        "or human support."
    ),
    version="1.0"
)

class SupportRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=2,
        max_length=300
    )

@app.get("/")
async def home():
    return {
        "status": "running",
        "service": "HearMe Support Routing API"
    }

@app.post("/api/v1/support-route")
async def support_route(
    request: SupportRequest
):
    try:
        result = route_support_query(
            request.query
        )

        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except TypeError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unexpected routing error."
        )