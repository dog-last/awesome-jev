# Research

Jev is closed-weight with no paper. The community reverse-engineered the inference shape in days — but the RLCD calibration training remains the real moat. Below: reproductions, and the independent evaluations that test the official claims.

## Open-source reproductions (training pipelines)

| Project | ★ | Why it's worth your time |
|---|---|---|
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 2.1k | Zero-training "semantic if" on an RTX 3090: read option logits from Qwen3.5-4B. 20 decisions/s with shared-prefix reuse; 0.845 agreement vs Jev's 0.883 on the public subset |
| [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) | 1k | The first viral reimplementation; options-as-queries attention pooling. Explicitly *not* an RLCD reproduction |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 1.2k | 0.6B end-to-end training pipeline with paired proper-reward learning — closest public thing to RLCD. Chinese-friendly docs, weights + data on HF |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 692 | API-compatible with `/v1/systemone`. The money stat: −1.8pp in-distribution but **−19.1pp OOD** vs real Jev — proof calibration training is the moat |
| [arnabgho/rlcd-lite](https://github.com/arnabgho/rlcd-lite) | 1 | GRPO + Brier reward reimplementation; key ablation: proper-scoring-rule rewards produce calibration, binary rewards destroy it |
| [DECRUX9812/openjev-lm](https://github.com/DECRUX9812/openjev-lm) | 1 | Cheapest entry point: LoRA on CPU in 89 min at $0, 92.9% answer agreement with the API |

More: [LightJev](https://github.com/rongxinzy/LightJev) · [jev-visual](https://github.com/hr98w/jev-visual) · [razorback16/openjev](https://github.com/razorback16/openjev) · [typed-decisions](https://github.com/kotoba-lang/typed-decisions) · [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)

## Inference-layer reimplementations (no training)

| Project | ★ | What it does |
|---|---|---|
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 206 | Qwen3.6-35B-A3B + SGLang, prefill-only with radix cache, full official HTTP API |
| [AlexWortega/openjev](https://huggingface.co/AlexWortega/openjev) | — | First open weights; Qwen3.5-4B as a 3-class NLI cross-encoder, zero-shot Doom |
| [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) | 40 | Apple Silicon MLX |
| [r-ms/mini-jev](https://github.com/r-ms/mini-jev) | 26 | Frozen Qwen3-4B, option-letter logits |
| [Trecto34/openjev-fighting-ring](https://github.com/Trecto34/openjev-fighting-ring) | 0 | Puts Diffusion/RLCD/Block-Causal/NLI approaches in one arena |

## Large-scale / pre-registered evaluations

| Evaluation | Finding |
|---|---|
| [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) | 9 adversarial experiments, 123,805 requests, $12.69: calibration ECE 0.075 in-domain but **fails OOD** (random 3-SAT); polite authority injection moves 147/200 answers; batching 255 questions is genuinely free |
| [exs-brady/jev-eval-evidence](https://github.com/exs-brady/jev-eval-evidence) | 55,347 typed judgments, Jev vs 10 LLMs + keyword/regex floors, pre-registered with a blind cross-family replication |
| [ickma2311/jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) | Banking77/CLINC150: Jev 0.832/0.870, but a 9 ms bge-small + logistic-regression baseline hits **0.933**; measured latency only 2.2× vs a nano-LLM — classical baselines still win some lanes |
| [Fox-Islam/jev-bias-bench](https://github.com/Fox-Islam/jev-bias-bench) | Counterfactual bias bench, 11,984 calls: 29 persona attributes across hiring/lending/clinical/bail scenarios, with noise floors and negative controls |
| [kokuren333/jev-jmle-benchmark](https://github.com/kokuren333/jev-jmle-benchmark) | 9 years of Japanese Medical Licensing Exams (3,556 items): **88.58%**; companion manuscript on medRxiv |
| [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | OpenBookQA 94.2% / ECE 0.024, but on an unknowable rule-based task 44.7% acc with stated p 0.74 — miscalibration sign flips by question type |
| [EmilLindfors/jev-horingssvar-eval](https://github.com/EmilLindfors/jev-horingssvar-eval) | Norwegian hearing documents: equal accuracy to DeepSeek V4.1 Flash at **$0.22 vs $3.08 / 1k docs**, 0.32 s vs 26 s median |

## Focused task evals

| Evaluation | Finding |
|---|---|
| [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) | Naive question: 62.6% (regex: 91.8%). Atomic decomposition + logistic regression: **95.0%** |
| [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | 98.3% on 18.5k emails ≈ TF-IDF, but **97.3% vs 72.5% under distribution drift** — drift robustness is the real edge |
| [mahlernim/jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark) | Reading comprehension nearly lossless; input reordering changes 13–14% of answers |
| [rorshopping/jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) | A 1.5B model can't write 28-field JSON but makes 28 schema-valid decisions in 0.4s; 7B is the sweet spot |
| [jev-poker](https://backnotprop.com/blog/jev-poker/) | Only 63% agreement with a solver, inverted confidence — feed it pre-digested intermediate conclusions |

More: [jev-banking77-experiment](https://github.com/simonmesmith/jev-banking77-experiment) · [jev-vs-open-decision-models](https://github.com/elcronos/jev-vs-open-decision-models) · [mnist-text-input](https://github.com/segavvy/mnist-text-input-benchmark) · [jev-ja-eval](https://github.com/uesgugikouhei-oss/jev-ja-eval) · [jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks) · [does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything) · [decision-model-benchmark](https://github.com/nibzard/decision-model-benchmark) · [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)

## Deep dives & reports

| Piece | Why read it |
|---|---|
| [sgnt.ai — "You could have built Jev"](https://sgnt.ai/p/jev/) | Best technical explainer; reconstructs the single-token-logit recipe and cross-tabulates the reproduction results |
| [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) | Data-driven survey of 2,170 public GitHub Jev projects, mapping early growth, application domains, and decision-use patterns; not a deployment or model-accuracy study. |
| [HackSing/jev-report](https://github.com/HackSing/jev-report) | 52-page independent research report (中文) |
| [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) | Aggregator of 714 X posts (226 demo videos, 114 long-form) from launch week — the entry point to the video firehose |
| [掘金：发布 3 天登顶 HN，我把 Jev 的源码和黑料都扒了一遍](https://juejin.cn/post/7686669083098775562) | Vercel AI SDK source dive (中文) |
| [lindfors.no — A first look at Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) | Careful first-principles cost/latency measurement on real documents |
| [ic.work：TypeSafe 发布 Jev 模型](https://www.ic.work/article/typesafe-releases-jev-system-one-model) | Skeptical take (中文) |

More: [ickas.dev](https://ickas.dev/writing/benchmarking-jev-battleship) · [southbridge.ai](https://www.southbridge.ai/blog/jev-entity-resolution) · [classmethod](https://dev.classmethod.jp/en/articles/jev-for-llm-model-routing/) · [mikulskibartosz.name](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew)

## Other awesome lists

- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) — the largest directory; evidence-backed submission rules
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) — the strictest curation, explicit inclusion criteria
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) — 中文, updated daily, honest about negative results
- [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) — the whole TypeSafe ecosystem
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) — public review notes and evidence sources
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) — submissions reviewed by Jev itself
