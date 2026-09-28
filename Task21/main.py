from fastapi import FastAPI, BackgroundTasks, Depends, Request
from pydantic import BaseModel, Field
from datetime import datetime
import asyncio
import time

app = FastAPI(
    title="HearMe Async API",
    description="FastAPI project demonstrating synchronous and asynchronous endpoints.",
    version="2.0"
)

class SupportRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        max_length=200
    )

    delay: float = Field(
        default=0.5,
        ge=0.05,
        le=2.0
    )

def get_service_info():
    return {
        "service": "HearMe Customer Support API",
        "environment": "Internship Demo"
    }

def write_background_log(
    version,
    query,
    processing_mode
):
    with open(
        "background_jobs.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()} | "
            f"{version} | "
            f"{processing_mode} | "
            f"{query}\n"
        )

@app.middleware("http")
async def performance_middleware(
    request: Request,
    call_next
):
    start_time = time.perf_counter()

    response = await call_next(request)

    total_time = (
        time.perf_counter() - start_time
    ) * 1000

    response.headers[
        "X-Process-Time-Milliseconds"
    ] = f"{total_time:.2f}"

    return response

@app.get("/")
async def home():
    return {
        "status": "running",
        "message": "HearMe Async API is running."
    }

@app.get("/api/v1/info")
def api_v1_info(
    service=Depends(get_service_info)
):
    return {
        "api_version": "v1",
        "type": "Synchronous API",
        "service": service
    }

@app.get("/api/v2/info")
async def api_v2_info(
    service=Depends(get_service_info)
):
    return {
        "api_version": "v2",
        "type": "Asynchronous API",
        "service": service
    }

@app.post("/api/v1/process-sync")
def process_sync(
    request: SupportRequest,
    background_tasks: BackgroundTasks,
    service=Depends(get_service_info)
):
    start = time.perf_counter()

    time.sleep(request.delay)

    processing_time = (
        time.perf_counter() - start
    ) * 1000

    background_tasks.add_task(
        write_background_log,
        "v1",
        request.query,
        "Synchronous"
    )

    return {
        "api_version": "v1",
        "processing_mode": "synchronous",
        "query": request.query,
        "answer": (
            "Customer support request processed "
            "using the synchronous API."
        ),
        "simulated_io_delay_seconds": request.delay,
        "endpoint_processing_time_ms": round(
            processing_time,
            2
        ),
        "service": service
    }

@app.post("/api/v2/process-async")
async def process_async(
    request: SupportRequest,
    background_tasks: BackgroundTasks,
    service=Depends(get_service_info)
):
    start = time.perf_counter()

    await asyncio.sleep(request.delay)

    processing_time = (
        time.perf_counter() - start
    ) * 1000

    background_tasks.add_task(
        write_background_log,
        "v2",
        request.query,
        "Asynchronous"
    )

    return {
        "api_version": "v2",
        "processing_mode": "asynchronous",
        "query": request.query,
        "answer": (
            "Customer support request processed "
            "using the asynchronous API."
        ),
        "simulated_io_delay_seconds": request.delay,
        "endpoint_processing_time_ms": round(
            processing_time,
            2
        ),
        "service": service
    }

@app.get("/api/v2/background-status")
async def background_status():
    try:
        with open(
            "background_jobs.log",
            "r",
            encoding="utf-8"
        ) as file:
            logs = file.readlines()

        return {
            "total_background_jobs": len(logs),
            "latest_jobs": logs[-5:]
        }

    except FileNotFoundError:
        return {
            "total_background_jobs": 0,
            "latest_jobs": []
        }