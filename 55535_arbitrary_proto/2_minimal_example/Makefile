reinstall_dependencies:
	rm -rf .venv
	uv venv
	source .venv/bin/activate
	uv pip install -r requirements.txt --native-tls

compile:
	python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. \
        proto_1/greet.proto \
        proto_2/dependency.proto


ray_serve_run:
	ray start --head || true
	serve start \
		--grpc-port 9000 \
		--grpc-servicer-functions proto_1.greet_pb2_grpc.add_GreeterServicer_to_server
	serve run ray_app:app


grpc_root_run:
	python root_server.py

run_root_client:
	python root_client.py

clean:
	ray stop
