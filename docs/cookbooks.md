# Cookbooks

Four patterns, each a single self-contained script, each executed against the **live Jev API** before being committed — real outputs shown. Dependencies are declared inline (PEP 723), so `uv run` is all you need.

```bash
git clone https://github.com/dog-last/awesome-jev && cd awesome-jev/cookbooks
cp .env.example .env   # paste your TYPESAFE_API_KEY
uv run 01_ticket_triage.py
```

Every request hanging with `TypeSafeAPITimeoutError`? Set `JEV_TLS12=1` — some networks drop the post-quantum TLS 1.3 ClientHello (see `common.py`).

## 01 · Ticket triage — three primitives in one call

Every question is evaluated in parallel against the same state, so mixing Choice + Score + Noul costs about the same latency as one question. ([source](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/01_ticket_triage.py))

```python
response = client.system_one(
    state=ticket,
    questions={
        "department": Choice(
            instructions="Which team should handle this",
            criteria={"billing": "Payment or subscription issues",
                      "technical": "Bugs or integration problems",
                      "sales": "Pricing or account questions"},
        ),
        "frustration": Score(
            instructions="How frustrated the customer appears",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry"],
        ),
        "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
    },
)
```

::: tip VERIFIED OUTPUT — OUR RUN, 2026-09-20
```
route to:   technical (confidence 0.69)
frustration: 1.0 / 2
urgent:      1.00
```
:::

## 02 · Confidence-gated guardrail

Ask atomic Noul questions per policy category, then let *your code* decide: act on high-confidence hits, route uncertain cases to a human instead of guessing. ([source](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/02_confidence_gated_guardrail.py))

```python
AUTO_BLOCK = 0.9   # act without a human above this
REVIEW = 0.5       # below this, treat as "model doesn't know"

response = client.system_one(
    state=post,
    questions={
        "scam":   Noul(instructions="The content is a financial scam or 'get rich quick' scheme"),
        "hate":   Noul(instructions="The content contains hateful or harassing language"),
        "sexual": Noul(instructions="The content contains sexual or adult material"),
    },
)

for name, answer in response.answers.items():
    p = answer.noul
    verdict = "BLOCK" if p >= AUTO_BLOCK else "REVIEW" if p >= REVIEW else "PASS"
    print(f"{name:>8}: p={p:.2f} -> {verdict}")
```

::: tip VERIFIED OUTPUT — OUR RUN, 2026-09-20
```
    scam: p=0.98 -> BLOCK
    hate: p=0.01 -> PASS
  sexual: p=0.01 -> PASS
```
:::

## 03 · RAG reranking

Score each candidate chunk against the query, sort, and drop anything the model is unsure about. Cheap enough to run on every retrieval. ([source](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/03_rag_rerank.py))

```python
for chunk in candidates:
    response = client.system_one(
        state=f"Query: {query}\n\nDocument chunk: {chunk}",
        questions={
            "relevance": Score(
                instructions="How useful is this chunk for answering the query",
                criteria=["Irrelevant", "Tangentially related", "Directly answers the query"],
            )
        },
    )
    ans = response.answers["relevance"]
    print(f"score={ans.score:.1f} confidence={ans.confidence:.2f} | {chunk[:60]}...")
```

::: tip VERIFIED OUTPUT — OUR RUN, 2026-09-20
```
score=2.0 confidence=1.00 | To rotate an API key, open Settings > Developers...
score=0.0 confidence=1.00 | Our pricing starts at $20/month...
score=1.1 confidence=0.88 | Old API keys are revoked automatically 24 hours...
```
:::

## 04 · Composite scoring — weights in code, not prompts

Don't ask "is this a good startup pitch?" — ask each factor separately and combine with a formula. When priorities change, you change a coefficient, not a prompt. ([source](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/04_composite_scoring.py))

```python
WEIGHTS = {"market": 0.4, "feasibility": 0.35, "differentiation": 0.25}
MIN_CONFIDENCE = 0.5

response = client.system_one(
    state=pitch,
    questions={
        dim: Score(instructions=f"Assess the {dim} of this business", criteria=levels)
        for dim in WEIGHTS
    },
)

total, confident = 0.0, True
for dim, weight in WEIGHTS.items():
    ans = response.answers[dim]
    total += weight * ans.score / (len(levels) - 1)
    confident &= ans.confidence >= MIN_CONFIDENCE

print("ACT" if confident else "REVIEW (low confidence)")
```

::: tip VERIFIED OUTPUT — OUR RUN, 2026-09-20
```
         market: 2.0/4 (confidence 0.69) x 0.4
    feasibility: 2.4/4 (confidence 0.55) x 0.35
differentiation: 1.3/4 (confidence 0.68) x 0.25
composite: 0.49 / 1.00 -> ACT
```
:::
