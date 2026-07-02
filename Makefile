.PHONY: run lint format type-check docker-build docker-run

run:
	uv run uvicorn app.main:app --reload

lint:
	uv run ruff check .

format:
	uv run ruff format .

type-check:
	uv run mypy app

docker-build:
	docker build -t catalyst .

docker-run:
	docker run -p 8000:8000 catalyst