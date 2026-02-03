import asyncio

import ray
from ray import serve
from starlette.requests import Request


@serve.deployment(max_ongoing_requests=4)
class WorkerDeployment:
    """A simple deployment that simulates work."""

    # 	curl "http://localhost:8000/?duration=2.0"
    # 	curl -X POST http://localhost:8000/ \
    # 		-H "Content-Type: application/json" \
    # 		-d '{"duration": 2.0}'

    async def __call__(self, request: Request):
        """Process a request by sleeping for the given duration."""
        # Get duration from query param or JSON body
        if request.method == "GET":
            duration = float(request.query_params.get("duration", 0.5))
        else:
            body = await request.json()
            duration = float(body.get("duration", 0.5))

        await asyncio.sleep(duration)
        return f"Processed request in {duration}s"


worker_app = WorkerDeployment.bind()
handle = serve.run(worker_app)

if __name__ == '__main__':
    print(123)
