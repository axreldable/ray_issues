"""
gRPC client for Ray Serve Greeter service with nested protos.
"""
import grpc
from proto_1 import greet_pb2, greet_pb2_grpc
from proto_2 import dependency_pb2


def check(port: int):
    """
    Connect to Ray Serve gRPC endpoint and send a request.
    """
    # Connect to Ray Serve gRPC proxy (default port 9000)
    with grpc.insecure_channel(f'localhost:{port}') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        # Create UserInfo from proto_2 (cross-directory dependency)
        user_info = dependency_pb2.UserInfo(
            user_id="user-456",
            email="alice@example.com",
            age=28
        )

        # Create HelloRequest from proto_1 with UserInfo from proto_2
        hello_request = greet_pb2.HelloRequest(
            name="Alice",
            user_info=user_info
        )

        # Make the gRPC call
        hello_reply, call = stub.SayHello.with_call(hello_request)
        print(f"Response: {hello_reply.message}")


if __name__ == "__main__":
    check(9000)
