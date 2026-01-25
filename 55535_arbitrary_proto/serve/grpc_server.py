import sys
from pathlib import Path

# Add parent directory to path so we can import from proto_1 and proto_2
sys.path.insert(0, str(Path(__file__).parent.parent))

from concurrent import futures

from proto_1 import greet_pb2
from proto_1 import greet_pb2_grpc
import grpc


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        print(f"User Info: user_id={request.user_info.user_id}, email={request.user_info.email}, age={request.user_info.age}")

        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"Hello from nested Server, {request.name}! Your email is {request.user_info.email}"

        return hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50052")
    server.start()
    print("Server started on port 50052")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
