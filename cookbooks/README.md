# Cookbooks

[English](README.md) | [简体中文](README.zh-CN.md)

Runnable Jev patterns. Every script was executed against the **live Jev API** before being committed — real outputs below. No vaporware.

## Setup

Requires [uv](https://docs.astral.sh/uv/). Dependencies are declared inline in each script (PEP 723), so there is nothing to install:

```bash
cd cookbooks
cp .env.example .env   # paste your TYPESAFE_API_KEY
uv run 01_ticket_triage.py
```

No API key yet? Apply at [typesafe.ai](https://typesafe.ai), or call `typesafe-ai/jev` through the [Vercel AI Gateway](https://vercel.com/ai-gateway) with no waitlist.

> If every request hangs and ends in `TypeSafeAPITimeoutError`, set `JEV_TLS12=1` — some networks drop the post-quantum TLS 1.3 ClientHello. See `common.py`.

## Patterns

| # | Script | Pattern | What you'll learn |
|---|---|---|---|
| 01 | [01_ticket_triage.py](01_ticket_triage.py) | Intent routing | Choice + Score + Noul in one parallel call |
| 02 | [02_confidence_gated_guardrail.py](02_confidence_gated_guardrail.py) | Confidence-gated guardrail | Atomic Noul checks → BLOCK/REVIEW/PASS |
| 03 | [03_rag_rerank.py](03_rag_rerank.py) | RAG reranking | Score chunks, sort, drop low-confidence |
| 04 | [04_composite_scoring.py](04_composite_scoring.py) | Composite scoring | Weights live in code, not prompts |

## Verified outputs

Recorded 2026-09-20 against `jev-latest` (values vary run to run — these are probabilities, not labels):

**01 ticket triage**
```
route to:   technical (confidence 0.69)
frustration: 1.0 / 2
urgent:      1.00
```

**02 confidence-gated guardrail**
```
    scam: p=0.98 -> BLOCK
    hate: p=0.01 -> PASS
  sexual: p=0.01 -> PASS
```

**03 RAG rerank**
```
score=2.0 confidence=1.00 | To rotate an API key, open Settings > Developers...
score=0.0 confidence=1.00 | Our pricing starts at $20/month...
score=1.1 confidence=0.88 | Old API keys are revoked automatically 24 hours...
```

**04 composite scoring**
```
         market: 2.0/4 (confidence 0.69) x 0.4
    feasibility: 2.4/4 (confidence 0.55) x 0.35
differentiation: 1.3/4 (confidence 0.68) x 0.25
composite: 0.49 / 1.00 -> ACT
```
