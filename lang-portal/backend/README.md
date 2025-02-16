uv venv
uv sync

source .venv/bin/activate

uv run fastapi dev

Now you have Alembic set up! Here's how to use it:
export PYTHONPATH=path_of_backend_directory
Initialize your first migration:
alembic revision --autogenerate -m "Initial migration"

Apply migrations:
alembic upgrade head

Rollback migrations:
alembic downgrade -1

View migration history:
alembic history

