# Updated Async API Documentation

## Project

HearMe Customer Support Async API

## Overview

The API demonstrates synchronous and asynchronous FastAPI endpoints together with middleware, background tasks, dependency injection, validation, API versioning, and performance benchmarking.

## API Versions

### Version 1

Version 1 represents the synchronous implementation.

Base path:

`/api/v1`

### Version 2

Version 2 represents the asynchronous implementation.

Base path:

`/api/v2`

## GET /

Checks whether the application is running.

### Response

```json
{
  "status": "running",
  "message": "HearMe Async API is running."
}