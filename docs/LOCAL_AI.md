# Local AI development

The current Intel Mac has an installed, tested local inference and notebook environment. It supports experimenting with prompts, calling a local model API, Python utilities, and dataset exploration. It is separate from the game's runtime and does not imply AI will be embedded in the game.

## Start from the repository root

Open a new terminal after installation. Exact Python dependencies are in [uv.lock](../tools/local-ai/uv.lock), with intent in [pyproject.toml](../tools/local-ai/pyproject.toml). Use [the environment README](../tools/local-ai/README.md) for commands.

```sh
uv sync --project tools/local-ai --frozen
uv run --project tools/local-ai --frozen python --version
ollama run qwen2.5-coder:1.5b
```

Ollama must be running. The installed small coding model is approximately 986 MB, Q4_K_M, ID `d7372fd82851`, under Apache-2.0 according to [its published model record](https://ollama.com/library/qwen2.5-coder:1.5b). The pre-existing `gemma4:26b` model was retained and was not benchmarked. A tiny smoke prompt completed locally with the answer `READY`; this verifies connectivity/generation, not coding quality.

For notebooks, keep private scratch and datasets in ignored `work/`:

```sh
mkdir -p work/local-ai
uv run --project tools/local-ai --frozen jupyter lab --no-browser --ip=127.0.0.1 --ServerApp.root_dir=work/local-ai
```

Open the local URL printed by Jupyter in your browser; keep its access token private. Ctrl-C stops it. In VS Code, select the interpreter at `tools/local-ai/.venv/bin/python` when opening notebooks. No extra Python packages are installed into Apple's system Python.

## Local API example

From `uv run --project tools/local-ai --frozen python`, or a notebook using that environment:

```python
import httpx

response = httpx.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "qwen2.5-coder:1.5b",
        "prompt": "Explain a variable using one short example.",
        "stream": False,
        "options": {"num_ctx": 2048, "num_predict": 128},
    },
    timeout=120,
)
response.raise_for_status()
print(response.json()["response"])
```

Keep Ollama bound to loopback unless a separate authenticated access design is approved. No cloud AI account, remote model endpoint, automatic repository editing, or cross-tool chat collector was configured here. Project-relevant prompts, responses, decisions, and handoffs still follow [AGENTS.md](../AGENTS.md) and the [conversation recording policy](conversations/README.md); a notebook alone is not canonical project memory.

## Hardware and next choices

[Ollama's macOS documentation](https://docs.ollama.com/macos) specifies CPU-only execution on x86 Macs. Use small models for short experiments here. The RTX 4090 desktop is the proposed place for heavier inference/fine-tuning, but its OS, drivers, framework, model, and dataset must be checked before installation; nothing was installed remotely on it.

PyTorch/Transformers training, CUDA, fine-tuning, and model evaluation are not set up or tested. The current default is local inference/AI app development while the owner's optional training-versus-inference preference remains unanswered. Each future dataset/model needs its own rights and provenance review before use or distribution.

## Verification

Python 3.12.15 imported HTTPX 0.28.1, NumPy 2.5.3, Pydantic 2.13.5, Hugging Face Hub 1.33.0, ipykernel 7.4.0, and JupyterLab 4.6.4. A Jupyter kernel executed a NumPy sum and returned `3`; Ollama generation returned `READY`. These checks cover setup, not a trained model or game feature. See [the installation session](conversations/2026-10-06-development-toolchain.md).
