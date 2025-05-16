.PHONY: init prepare_artifacts start init_docker

init:
	uv venv --python 3.12 && \
	. .venv/bin/activate && \
	uv sync

prepare_artifacts:
	uv run python main.py

start:
	uv run uvicorn app:app --reload --port 8000
