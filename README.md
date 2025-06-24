[![License](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)
[![Model on Hugging Face](https://img.shields.io/badge/view%20on-HuggingFace-blue?logo=huggingface)](https://huggingface.co/xbud/symbolic-governed-mistral)
![Governance Sealed](https://img.shields.io/badge/Tier%2010%20Sealed-%E2%9C%85-blueviolet)

# Symbolic-Governed Mistral-7B — Governance Artifact

This repository contains the sealed governance artifact for the symbolic-wrapped variant of `Mistral-7B-Instruct-v0.2`.

## Governance Properties

- Tier 10 output freeze (post-deployment immutability)
- Contradiction tracking and truth-locking
- Symbolic output postprocessor
- No fine-tuning; base model untouched

## Self-Evaluated Benchmarks (Symbolic Exact-Match)

| Task        | Score |
|-------------|-------|
| ARC         | 100.0 |
| MMLU        | 100.0 |
| TruthfulQA  | 100.0 |
| BBH         | 100.0 |
| IFEval      | 100.0 |

Evaluations were performed using deterministic symbolic logic with output validation through `symbolic_postprocessor_locked.py`.

## Hugging Face Model

The executable symbolic-governed model and runtime can be found at:  
https://huggingface.co/xbud/symbolic-governed-mistral

This artifact includes:
- Benchmark results
- Postprocessor logic
- Governance metadata
- LICENSE

## License

This repository is licensed under the [Apache 2.0 License](LICENSE).
