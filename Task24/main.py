from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from pathlib import Path
from logging.handlers import RotatingFileHandler
import logging
import os
import time

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "HearMe Company API"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

API_VERSION = os.getenv(
    "API_VERSION",
    "v1"
)

Path("logs").mkdir(
    exist_ok=True
)

logger = logging.getLogger(
    "hearme_api"
)

logger.setLevel(
    getattr(
        logging,
        LOG_LEVEL.upper(),
        logging.INFO
    )
)

if not logger.handlers:
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

app = FastAPI(
    title=APP_NAME,
    version="1.0.0",
    description="Production readiness demo for the HearMe company project."
)

request_count = 0

company_knowledge = [
    "HearMe is an AI-powered voice agent platform.",
    "HearMe uses Speech-to-Text to convert customer speech into text.",
    "ASR performance can be measured using Word Error Rate, Character Error Rate, and inference time.",
    "RAG retrieves relevant company information before generating an answer.",
    "Text-to-Speech converts generated responses into spoken audio.",
    "Complex customer issues can be escalated to a human support agent."
]

class SearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=2,
        max_length=200
    )

def search_company_information(query: str):
    query_words = set(
        query.lower().split()
    )

    best_result = None
    best_score = 0

    for item in company_knowledge:
        item_words = set(
            item.lower().split()
        )

        score = len(
            query_words.intersection(
                item_words
            )
        )

        if score > best_score:
            best_score = score
            best_result = item

    return best_result

@app.middleware("http")
async def logging_middleware(
    request: Request,
    call_next
):
    global request_count

    request_count += 1

    start_time = time.perf_counter()

    logger.info(
        "Request started | %s %s",
        request.method,
        request.url.path
    )

    try:
        response = await call_next(
            request
        )

        duration = (
            time.perf_counter()
            - start_time
        ) * 1000

        logger.info(
            "Request completed | %s %s | Status: %s | %.2f ms",
            request.method,
            request.url.path,
            response.status_code,
            duration
        )

        response.headers[
            "X-Process-Time-MS"
        ] = f"{duration:.2f}"

        return response

    except Exception as error:
        logger.exception(
            "Unhandled request error: %s",
            error
        )

        raise

@app.get("/")
async def home():
    return {
        "application": APP_NAME,
        "environment": APP_ENV,
        "api_version": API_VERSION,
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": APP_NAME,
        "environment": APP_ENV
    }

@app.get("/metrics")
async def metrics():
    return {
        "total_requests": request_count,
        "service_status": "healthy"
    }

@app.get("/api/v1/company-info")
async def company_info():
    return {
        "company": "HearMe",
        "description": (
            "AI-powered voice agent platform "
            "for customer communication."
        )
    }

@app.post("/api/v1/search")
async def company_search(
    request: SearchRequest
):
    logger.info(
        "Company search query: %s",
        request.query
    )

    result = search_company_information(
        request.query
    )

    if result is None:
        logger.warning(
            "No company information found for query: %s",
            request.query
        )

        raise HTTPException(
            status_code=404,
            detail="No relevant company information found."
        )

    return {
        "query": request.query,
        "result": result
    }