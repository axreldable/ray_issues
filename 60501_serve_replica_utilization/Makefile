reinstall_dependencies:
	rm -rf .venv
	uv venv
	source .venv/bin/activate
	uv pip install -r requirements.txt --native-tls

server:
	python hello_serve.py

run:
	serve run hello_serve:app --route-prefix /hello-world-1
	serve run worker_serve:worker_app --route-prefix /worker_app
	serve shutdown

client:
	curl http://localhost:8000/hello-world-1
	curl http://localhost:8000/worker_app


debug:
	ray status
	serve status
	ray list actors --detail
	ps aux | grep -E "(ray|serve)" | grep -v grep
	tail -100 /tmp/ray/session_2026-02-02_15-58-32_930188_23669/logs/runtime_env_agent.out
	tail -100 /tmp/ray/session_2026-02-02_15-58-32_930188_23669/logs/runtime_env_agent.err
