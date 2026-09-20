# Cookbook 实战手册

[English](README.md) | [简体中文](README.zh-CN.md)

可运行的 Jev 模式。每个脚本提交前都对**真实 Jev API** 跑通过 —— 下方附真实输出，拒绝纸面代码。

## 准备

需要 [uv](https://docs.astral.sh/uv/)。依赖已内联声明在每个脚本里（PEP 723），无需手动安装：

```bash
cd cookbooks
cp .env.example .env   # 填入你的 TYPESAFE_API_KEY
uv run 01_ticket_triage.py
```

还没有 API key？去 [typesafe.ai](https://typesafe.ai) 申请，或通过 [Vercel AI Gateway](https://vercel.com/ai-gateway) 调用 `typesafe-ai/jev`（免排队）。

> 如果所有请求都挂起并以 `TypeSafeAPITimeoutError` 告终，设置 `JEV_TLS12=1` —— 某些网络会丢弃后量子 TLS 1.3 ClientHello，详见 `common.py`。

## 模式

| # | 脚本 | 模式 | 你会学到 |
|---|---|---|---|
| 01 | [01_ticket_triage.py](01_ticket_triage.py) | 意图路由 | Choice + Score + Noul 混合单次并行调用 |
| 02 | [02_confidence_gated_guardrail.py](02_confidence_gated_guardrail.py) | 置信度门控护栏 | 原子 Noul 检查 → 拦截/人工/放行 |
| 03 | [03_rag_rerank.py](03_rag_rerank.py) | RAG 重排 | 候选 chunk 打分、排序、丢弃低置信 |
| 04 | [04_composite_scoring.py](04_composite_scoring.py) | 组合评分 | 权重写在代码里，而不是 prompt 里 |

## 实测输出

2026-09-20 对 `jev-latest` 实测记录（概率输出，每次运行数值会略有波动）：

**01 工单分类路由**
```
route to:   technical (confidence 0.69)
frustration: 1.0 / 2
urgent:      1.00
```

**02 置信度门控护栏**
```
    scam: p=0.98 -> BLOCK
    hate: p=0.01 -> PASS
  sexual: p=0.01 -> PASS
```

**03 RAG 重排**
```
score=2.0 confidence=1.00 | To rotate an API key, open Settings > Developers...
score=0.0 confidence=1.00 | Our pricing starts at $20/month...
score=1.1 confidence=0.88 | Old API keys are revoked automatically 24 hours...
```

**04 组合评分**
```
         market: 2.0/4 (confidence 0.69) x 0.4
    feasibility: 2.4/4 (confidence 0.55) x 0.35
differentiation: 1.3/4 (confidence 0.68) x 0.25
composite: 0.49 / 1.00 -> ACT
```
