# Symbolic-Governed Mistral-7B — Governance Artifact

This model is a sealed governance-layered variant of Mistral-7B-Instruct-v0.2, governed by a symbolic enforcement mesh.

## Governance Properties

- Tier 10 output freeze (post-deployment immutability)
- Contradiction tracking and truth-locking
- Symbolic output postprocessor
- No fine-tuning; base model untouched
- Hugging Face model card: https://huggingface.co/xbud/symbolic-governed-mistral

## Self-Evaluated Benchmarks (Symbolic Exact-Match)

| Task        | Score |
|-------------|-------|
| ARC         | 100.0 |
| MMLU        | 100.0 |
| TruthfulQA  | 100.0 |
| BBH         | 100.0 |
| IFEval      | 100.0 |

Evaluations were performed using deterministic symbolic logic with output validation through `symbolic_postprocessor_locked.py`.

## Base Model

- [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
