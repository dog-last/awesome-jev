# 实战手册

四个模式，每个都是独立可一口气读完的脚本，提交前都对**真实 Jev API** 跑过 —— 附真实输出。依赖内联声明（PEP 723），只需 `uv run`。

```bash
git clone https://github.com/dog-last/awesome-jev && cd awesome-jev/cookbooks
cp .env.example .env   # 填入你的 TYPESAFE_API_KEY
uv run 01_ticket_triage.py
```

所有请求都挂起并报 `TypeSafeAPITimeoutError`？设置 `JEV_TLS12=1` —— 某些网络会丢弃后量子 TLS 1.3 ClientHello（见 `common.py`）。

## 01 · 工单分类路由 —— 一次调用三种原语

每个问题都对同一 state 并行评估，因此混合 Choice + Score + Noul 的延迟约等于只问一个。（[源码](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/01_ticket_triage.py)）

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

::: tip 实测输出 · 2026-09-20
```
route to:   technical (confidence 0.69)
frustration: 1.0 / 2
urgent:      1.00
```
:::

## 02 · 置信度门控护栏

对每类策略问原子 Noul 问题，然后让*你的代码*决定：高置信命中直接处置，不确定的交给人工而不是硬猜。（[源码](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/02_confidence_gated_guardrail.py)）

```python
AUTO_BLOCK = 0.9   # 高于此值直接处置
REVIEW = 0.5       # 低于此值视为"模型不知道"

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

::: tip 实测输出 · 2026-09-20
```
    scam: p=0.98 -> BLOCK
    hate: p=0.01 -> PASS
  sexual: p=0.01 -> PASS
```
:::

## 03 · RAG 重排

给每个候选 chunk 按查询打分、排序，丢弃模型不确定的结果。便宜到可以在每次检索时运行。（[源码](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/03_rag_rerank.py)）

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

::: tip 实测输出 · 2026-09-20
```
score=2.0 confidence=1.00 | To rotate an API key, open Settings > Developers...
score=0.0 confidence=1.00 | Our pricing starts at $20/month...
score=1.1 confidence=0.88 | Old API keys are revoked automatically 24 hours...
```
:::

## 04 · 组合评分 —— 权重写在代码里

不要直接问"这个创业项目好不好" —— 分开问每个维度，再用公式组合。优先级变化时改的是系数，不是 prompt。（[源码](https://github.com/dog-last/awesome-jev/blob/main/cookbooks/04_composite_scoring.py)）

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

::: tip 实测输出 · 2026-09-20
```
         market: 2.0/4 (confidence 0.69) x 0.4
    feasibility: 2.4/4 (confidence 0.55) x 0.35
differentiation: 1.3/4 (confidence 0.68) x 0.25
composite: 0.49 / 1.00 -> ACT
```
:::
