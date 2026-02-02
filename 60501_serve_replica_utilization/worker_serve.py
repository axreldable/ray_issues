import asyncio

import ray
from ray import serve
from starlette.requests import Request

@serve.deployment(max_ongoing_requests=4)
class WorkerDeployment:
    """A simple deployment that simulates work."""

    async def __call__(self, duration: float):
        """Process a request by sleeping for the given duration."""
        duration = 0.5
        await asyncio.sleep(duration)
        return f"Processed request in {duration}s"


worker_app = WorkerDeployment.bind()
handle = serve.run(worker_app)
ray.get(handle.remote(1.0))