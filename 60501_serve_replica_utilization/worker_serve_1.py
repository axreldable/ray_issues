import asyncio

from ray import serve


@serve.deployment(max_ongoing_requests=4)
class WorkerDeployment:
    """A simple deployment that simulates work."""

    async def __call__(self, duration: float):
        """Process a request by sleeping for the given duration."""
        await asyncio.sleep(duration)
        return f"Processed request in {duration}s"


worker_app = WorkerDeployment.bind()
handle = serve.run(worker_app)

if __name__ == '__main__':
    rez = handle.remote(1.0).result()
    print(rez)
