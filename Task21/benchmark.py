import asyncio
import httpx
import time
import csv
import statistics

BASE_URL = "http://127.0.0.1:8000"

TOTAL_REQUESTS = 80

PAYLOAD = {
    "query": "Analyze customer support request",
    "delay": 0.5
}

async def send_request(
    client,
    url
):
    start = time.perf_counter()

    try:
        response = await client.post(
            url,
            json=PAYLOAD
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        return {
            "success": response.status_code == 200,
            "latency": elapsed
        }

    except Exception:
        elapsed = (
            time.perf_counter() - start
        ) * 1000

        return {
            "success": False,
            "latency": elapsed
        }

async def run_benchmark(
    endpoint,
    name
):
    url = BASE_URL + endpoint

    limits = httpx.Limits(
        max_connections=100,
        max_keepalive_connections=100
    )

    async with httpx.AsyncClient(
        timeout=30,
        limits=limits
    ) as client:

        start = time.perf_counter()

        tasks = [
            send_request(
                client,
                url
            )
            for _ in range(TOTAL_REQUESTS)
        ]

        results = await asyncio.gather(
            *tasks
        )

        total_time = (
            time.perf_counter() - start
        )

    successful = [
        result
        for result in results
        if result["success"]
    ]

    latencies = [
        result["latency"]
        for result in successful
    ]

    if not latencies:
        raise RuntimeError(
            f"No successful requests for {name}"
        )

    return {
        "API": name,
        "Requests": TOTAL_REQUESTS,
        "Successful": len(successful),
        "Total_Time_Seconds": round(
            total_time,
            3
        ),
        "Average_Latency_MS": round(
            statistics.mean(latencies),
            2
        ),
        "Median_Latency_MS": round(
            statistics.median(latencies),
            2
        ),
        "Min_Latency_MS": round(
            min(latencies),
            2
        ),
        "Max_Latency_MS": round(
            max(latencies),
            2
        ),
        "Throughput_Requests_Per_Second": round(
            len(successful) / total_time,
            2
        )
    }

async def main():

    print(
        "===== API PERFORMANCE BENCHMARK ====="
    )

    print(
        "\nBenchmarking synchronous API..."
    )

    sync_result = await run_benchmark(
        "/api/v1/process-sync",
        "Synchronous API"
    )

    print(
        "Synchronous benchmark completed."
    )

    print(
        "\nBenchmarking asynchronous API..."
    )

    async_result = await run_benchmark(
        "/api/v2/process-async",
        "Asynchronous API"
    )

    print(
        "Asynchronous benchmark completed."
    )

    results = [
        sync_result,
        async_result
    ]

    print(
        "\n===== PERFORMANCE RESULTS ====="
    )

    for result in results:

        print(
            "\nAPI:",
            result["API"]
        )

        print(
            "Total Time:",
            result["Total_Time_Seconds"],
            "seconds"
        )

        print(
            "Average Latency:",
            result["Average_Latency_MS"],
            "ms"
        )

        print(
            "Throughput:",
            result[
                "Throughput_Requests_Per_Second"
            ],
            "requests/sec"
        )

    with open(
        "benchmark_results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    sync_time = sync_result[
        "Total_Time_Seconds"
    ]

    async_time = async_result[
        "Total_Time_Seconds"
    ]

    improvement = (
        (sync_time - async_time)
        / sync_time
    ) * 100

    sync_throughput = sync_result[
        "Throughput_Requests_Per_Second"
    ]

    async_throughput = async_result[
        "Throughput_Requests_Per_Second"
    ]

    throughput_improvement = (
        (
            async_throughput
            - sync_throughput
        )
        / sync_throughput
    ) * 100

    comparison_table = f"""# Performance Comparison Table

| Metric | Synchronous API | Asynchronous API |
|---|---:|---:|
| Total Requests | {sync_result["Requests"]} | {async_result["Requests"]} |
| Successful Requests | {sync_result["Successful"]} | {async_result["Successful"]} |
| Total Time (seconds) | {sync_result["Total_Time_Seconds"]} | {async_result["Total_Time_Seconds"]} |
| Average Latency (ms) | {sync_result["Average_Latency_MS"]} | {async_result["Average_Latency_MS"]} |
| Median Latency (ms) | {sync_result["Median_Latency_MS"]} | {async_result["Median_Latency_MS"]} |
| Minimum Latency (ms) | {sync_result["Min_Latency_MS"]} | {async_result["Min_Latency_MS"]} |
| Maximum Latency (ms) | {sync_result["Max_Latency_MS"]} | {async_result["Max_Latency_MS"]} |
| Throughput (requests/sec) | {sync_result["Throughput_Requests_Per_Second"]} | {async_result["Throughput_Requests_Per_Second"]} |

## Measured Improvement

Overall batch completion time improvement:

**{improvement:.2f}%**

Throughput improvement:

**{throughput_improvement:.2f}%**

These results were measured on the local development machine and may vary depending on hardware, operating system, server configuration, concurrency, and workload.
"""

    with open(
        "Performance_Comparison_Table.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            comparison_table
        )

    report = f"""# API Performance Benchmark Report

## Objective

The purpose of this benchmark was to compare the performance of a synchronous FastAPI endpoint with an asynchronous FastAPI endpoint for an I/O-bound workload.

## APIs Compared

Synchronous endpoint:

`POST /api/v1/process-sync`

Asynchronous endpoint:

`POST /api/v2/process-async`

## Test Configuration

Total concurrent requests tested:

**{TOTAL_REQUESTS}**

Simulated I/O delay per request:

**{PAYLOAD["delay"]} seconds**

## Synchronous API Results

Total execution time:

**{sync_result["Total_Time_Seconds"]} seconds**

Average request latency:

**{sync_result["Average_Latency_MS"]} ms**

Throughput:

**{sync_result["Throughput_Requests_Per_Second"]} requests/second**

## Asynchronous API Results

Total execution time:

**{async_result["Total_Time_Seconds"]} seconds**

Average request latency:

**{async_result["Average_Latency_MS"]} ms**

Throughput:

**{async_result["Throughput_Requests_Per_Second"]} requests/second**

## Performance Improvement

Measured batch completion time improvement:

**{improvement:.2f}%**

Measured throughput improvement:

**{throughput_improvement:.2f}%**

## Analysis

The asynchronous endpoint uses `await asyncio.sleep()` to represent non-blocking I/O.

During the waiting period, the event loop can continue handling other requests.

The synchronous endpoint uses `time.sleep()`, which represents blocking work.

The benchmark therefore demonstrates how asynchronous programming can improve concurrency for I/O-bound API workloads.

The exact results depend on the development machine, operating system, FastAPI thread pool, request concurrency, and server configuration.

Async programming does not automatically make CPU-bound work faster. Its primary benefit in this experiment is improved handling of concurrent I/O-bound operations.

## Conclusion

The benchmark compared synchronous and asynchronous implementations using the same request workload.

The measured results demonstrate the performance characteristics of each implementation on the local development environment.

The asynchronous implementation is particularly useful when an API spends significant time waiting for operations such as databases, external APIs, files, or network services.
"""

    with open(
        "Benchmark_Report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            report
        )

    print(
        "\n===== IMPROVEMENT ====="
    )

    print(
        "Batch completion improvement:",
        round(improvement, 2),
        "%"
    )

    print(
        "Throughput improvement:",
        round(
            throughput_improvement,
            2
        ),
        "%"
    )

    print(
        "\nFiles generated:"
    )

    print(
        "benchmark_results.csv"
    )

    print(
        "Performance_Comparison_Table.md"
    )

    print(
        "Benchmark_Report.md"
    )

if __name__ == "__main__":
    asyncio.run(main())