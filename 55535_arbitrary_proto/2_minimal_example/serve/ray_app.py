"""
Ray Serve gRPC server using nested proto structure.
This demonstrates that Ray Serve works with cross-directory proto dependencies.
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import from proto_1 and proto_2
sys.path.insert(0, str(Path(__file__).parent.parent))
# Alternatively, add path to the folder to PYTHONPATH: `export PYTHONPATH=/path/to/proto/root:$PYTHONPATH`

from proto_1 import greet_pb2, greet_pb2_grpc
from proto_2 import dependency_pb2

from ray import serve


@serve.deployment
class GreeterDeployment:
    def SayHello(self, request: greet_pb2.HelloRequest) -> greet_pb2.HelloReply:
        """
        Handle SayHello RPC call.

        Args:
            request: HelloRequest with name and user_info (from proto_2)

        Returns:
            HelloReply with greeting message
        """
        print("SayHello Request Made:")
        print(f"  Name: {request.name}")
        print(f"  User Info: user_id={request.user_info.user_id}, "
              f"email={request.user_info.email}, age={request.user_info.age}")

        # Create response using data from cross-directory proto
        message = f"Hello from Ray, {request.name}! Your email is {request.user_info.email}"

        return greet_pb2.HelloReply(message=message)


# Bind the deployment
app = GreeterDeployment.bind()
