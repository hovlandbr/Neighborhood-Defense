# Isolated local AI development environment

Use Python notebooks and local Ollama API calls without modifying system Python. See [local AI guidance](../../docs/LOCAL_AI.md) and [installed versions](../../docs/DEVELOPMENT.md).

From the repository root:

```sh
uv sync --project tools/local-ai --frozen
uv run --project tools/local-ai --frozen python
uv run --project tools/local-ai --frozen jupyter lab --version
```

`uv.lock` pins dependency versions; `.venv/` is generated and ignored. The environment includes JupyterLab/ipykernel, HTTPX, NumPy, Pydantic, and Hugging Face Hub. Model weights are managed by Ollama outside Git. No training framework is included. Recreating this environment downloads Python/packages as needed; it does not install desktop applications or automatically download Ollama models.

To update dependencies intentionally, edit `pyproject.toml`, run `uv lock --project tools/local-ai` and `uv sync --project tools/local-ai`, recheck imports and a kernel/API call, and record the change in a session. Do not commit notebook access tokens, private datasets, environment folders, or generated model weights.
