reinstall_dependencies:
	rm -rf .venv
	uv venv
	source .venv/bin/activate
	uv pip install -r requirements.txt --native-tls

server:
	python hello_serve.py

run:
	serve run hello_serve:app --route-prefix /hello-world-1

client:
	curl http://localhost:8000/hello-world-1
