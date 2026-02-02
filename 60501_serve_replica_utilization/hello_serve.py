from ray import serve

from starlette.requests import Request


# name: HelloWorld
# num_replicas: 1
# max_ongoing_requests: 5
# max_queued_requests: -1
# user_config: null
# graceful_shutdown_wait_loop_s: 2
# graceful_shutdown_timeout_s: 20
# health_check_period_s: 10
# health_check_timeout_s: 30
# ray_actor_options:
#   num_cpus: 2
# request_router_config:
#   request_router_class: ray.serve._private.request_router:PowerOfTwoChoicesRequestRouter
#   request_router_kwargs: {}
#   request_routing_stats_period_s: 10
#   request_routing_stats_timeout_s: 30
@serve.deployment(
    ray_actor_options={"num_cpus": 2}
)
class HelloWorld:
    def __call__(self, request: Request):
        return f"Hello, world from Ray Serve! {type(request)}"

app = HelloWorld.bind()
