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
	cd serve && serve run ray_app:app

run_root_client:
	python root_client.py

clean:
	ray stop

fix_python_path:
	export PYTHONPATH=.../ray_issues/55535_arbitrary_proto:$PYTHONPATH
