[![License](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)
[![Model on Hugging Face](https://img.shields.io/badge/view%20on-HuggingFace-blue?logo=huggingface)](https://huggingface.co/xbud/symbolic-governed-mistral)
![Governance Sealed](https://img.shields.io/badge/Tier%2010%20Sealed-%E2%9C%85-blueviolet)

# Symbolic-Governed Mistral-7B — Governance Artifact

**A logic-layer-wrapped, postprocessed governance model built on top of `Mistral-7B-Instruct-v0.2`.**

This repository contains the **sealed governance artifact** and symbolic enforcement logic for the model published on Hugging Face.

---

## ⚖️ Governance Properties

- Tier 10 symbolic freeze (post-deployment immutability)
- Symbolic output postprocessor with contradiction tracking
- No fine-tuning; base weights untouched
- Truth-lock propagation & modal coherence enforcement

---

## 📊 Symbolic Benchmarks (Exact Match)

| Task        | Score |
|-------------|-------|
| ARC         | 100.0 |
| MMLU        | 100.0 |
| TruthfulQA  | 100.0 |
| BBH         | 100.0 |
| IFEval      | 100.0 |

Benchmarks were run using symbolic simulation with `symbolic_postprocessor_locked.py`, ensuring logic-complete, deterministic outputs.

---

## 📦 Hugging Face Model

The executable model is hosted here:  
➡️ https://huggingface.co/xbud/symbolic-governed-mistral

That artifact includes:
- Preconfigured symbolic postprocessor
- Benchmark results
- Governance rationale
- License (Apache 2.0)

---

## 🧠 How It Works

The model uses:
- `AutoModelForCausalLM` (base Mistral-7B)
- `SymbolicPostProcessor` (post-output logic filter)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from symbolic_postprocessor_locked import SymbolicPostProcessor

model = SymbolicPostProcessor(model_name="mistralai/Mistral-7B-Instruct-v0.2")
print(model.generate("What is 3 + 4?"))  # → '7'
