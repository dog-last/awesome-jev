# 研究

Jev 权重闭源、无论文。社区几天内就逆向出了推理形态 —— 但 RLCD 校准训练仍是真正的壁垒。下面是复现项目，以及检验官方说法的独立评测。

## 开源复现（训练管线）

| 项目 | ★ | 为什么值得看 |
|---|---|---|
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 2.1k | RTX 3090 零训练复现 "semantic if"：读 Qwen3.5-4B 选项 logits。共享前缀复用后 20 决策/秒；公开子集一致率 0.845（Jev 为 0.883） |
| [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) | 1k | 最早出圈的复现；选项作为 query 做 attention 池化。作者明确声明不是 RLCD 复现 |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 1.2k | 中文作者；0.6B 端到端训练流水线 + paired proper-reward learning —— 目前最接近 RLCD 的公开实现，权重和数据集在 HF |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 692 | 与官方 `/v1/systemone` API 完全兼容。关键数据：同分布仅差 1.8pp，但 **OOD 差 19.1pp** —— 证明校准训练才是壁垒 |
| [arnabgho/rlcd-lite](https://github.com/arnabgho/rlcd-lite) | 1 | GRPO + Brier 奖励重实现；核心消融：proper scoring rule 奖励产生校准，二元奖励摧毁校准 |
| [DECRUX9812/openjev-lm](https://github.com/DECRUX9812/openjev-lm) | 1 | 最低成本入门：纯 CPU LoRA 训练 89 分钟、$0，与 API 答案一致率 92.9% |

更多：[LightJev](https://github.com/rongxinzy/LightJev) · [jev-visual](https://github.com/hr98w/jev-visual) · [razorback16/openjev](https://github.com/razorback16/openjev) · [typed-decisions](https://github.com/kotoba-lang/typed-decisions) · [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)

## 推理层复现（零训练）

| 项目 | ★ | 做什么 |
|---|---|---|
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 206 | Qwen3.6-35B-A3B + SGLang，prefill-only + radix cache，完整实现官方 HTTP API |
| [AlexWortega/openjev](https://huggingface.co/AlexWortega/openjev) | — | 最早开放权重；Qwen3.5-4B 改 3 类 NLI 交叉编码器，零样本玩 Doom |
| [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) | 40 | Apple Silicon MLX |
| [r-ms/mini-jev](https://github.com/r-ms/mini-jev) | 26 | 冻结 Qwen3-4B 读选项字母 logits |
| [Trecto34/openjev-fighting-ring](https://github.com/Trecto34/openjev-fighting-ring) | 0 | Diffusion/RLCD/Block-Causal/NLI 各方案同场竞技 |

## 大规模 / 预注册评测

| 评测 | 结论 |
|---|---|
| [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) | 9 组对抗实验、123,805 次请求、$12.69：域内校准 ECE 0.075，但 **OOD 完全失效**（随机 3-SAT）；礼貌的权威注入能改变 147/200 个答案；255 问题批处理真的免费 |
| [exs-brady/jev-eval-evidence](https://github.com/exs-brady/jev-eval-evidence) | 55,347 条类型化判断，Jev 对阵 10 个 LLM + 关键词/正则基线，预注册 + 跨模型家族盲复现 |
| [ickma2311/jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) | Banking77/CLINC150：Jev 0.832/0.870，但 9ms 的 bge-small + 逻辑回归基线达 **0.933**；实测延迟仅为 nano-LLM 的 2.2 倍 —— 经典基线在某些赛道仍然更强 |
| [Fox-Islam/jev-bias-bench](https://github.com/Fox-Islam/jev-bias-bench) | 反事实偏见基准，11,984 次调用：29 种人设属性 × 招聘/信贷/临床/保释等场景，含噪声底线与阴性对照 |
| [kokuren333/jev-jmle-benchmark](https://github.com/kokuren333/jev-jmle-benchmark) | 9 年日本医师国家考试（3,556 题）：**88.58%**；配套论文已投 medRxiv |
| [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | OpenBookQA 94.2% / ECE 0.024；但在不可知的规则任务上准确率 44.7% 而自报 p 0.74 —— 校准偏差方向随题型翻转 |
| [EmilLindfors/jev-horingssvar-eval](https://github.com/EmilLindfors/jev-horingssvar-eval) | 挪威听证会文件：准确率与 DeepSeek V4.1 Flash 持平，但 **$0.22 vs $3.08 / 千份**，中位 0.32s vs 26s |

## 细分任务评测

| 评测 | 结论 |
|---|---|
| [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) | 直接问：62.6%（正则 91.8%）；原子化拆解 + 逻辑回归：**95.0%** |
| [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | 18.5k 封邮件 98.3% ≈ TF-IDF；但**分布漂移下 97.3% vs 72.5%** —— 抗漂移是真优势 |
| [mahlernim/jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark) | 阅读几乎无损；输入重排会改变 13–14% 的答案 |
| [rorshopping/jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) | 1.5B 写不出 28 字段 JSON，却能 0.4 秒做 28 个 schema 合法决策；7B 是甜点规模 |
| [jev-poker](https://backnotprop.com/blog/jev-poker/) | 与求解器吻合仅 63% 且置信度倒挂 —— 必须喂"嚼碎"的中间结论 |

更多：[jev-banking77-experiment](https://github.com/simonmesmith/jev-banking77-experiment) · [jev-vs-open-decision-models](https://github.com/elcronos/jev-vs-open-decision-models) · [mnist-text-input](https://github.com/segavvy/mnist-text-input-benchmark) · [jev-ja-eval](https://github.com/uesgugikouhei-oss/jev-ja-eval) · [jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks) · [does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything) · [decision-model-benchmark](https://github.com/nibzard/decision-model-benchmark) · [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)

## 深度报告与文章

| 文章 | 为什么读 |
|---|---|
| [sgnt.ai — "You could have built Jev"](https://sgnt.ai/p/jev/) | 最佳技术解析；重建了单 token logits 方案并交叉比对各复现结果 |
| [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) | 首个基于数据的 Jev 应用生态综述与分析：研究 2,170 个公开 GitHub 项目，记录早期增长、应用领域和决策用途分布；不等同于部署量或模型准确率研究。 |
| [HackSing/jev-report](https://github.com/HackSing/jev-report) | 52 页独立研究报告（中文） |
| [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) | 聚合发布首周 714 条 X 帖子（226 个演示视频、114 篇长文）—— 视频洪流入口 |
| [掘金：发布 3 天登顶 HN，我把 Jev 的源码和黑料都扒了一遍](https://juejin.cn/post/7686669083098775562) | 扒 Vercel AI SDK 源码 |
| [lindfors.no — A first look at Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) | 基于真实文档的严谨成本/延迟测量 |
| [ic.work：TypeSafe 发布 Jev 模型](https://www.ic.work/article/typesafe-releases-jev-system-one-model) | 质疑向分析 |

更多：[ickas.dev](https://ickas.dev/writing/benchmarking-jev-battleship) · [southbridge.ai](https://www.southbridge.ai/blog/jev-entity-resolution) · [classmethod](https://dev.classmethod.jp/en/articles/jev-for-llm-model-routing/) · [mikulskibartosz.name](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew)

## 其他 Awesome 清单

- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) —— 最大目录，提交需附证据
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) —— 策展最严，有明确收录标准
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) —— 中文清单，每日更新，敢写反面数据
- [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) —— 覆盖整个 TypeSafe 生态
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) —— 公开评审笔记与证据来源
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) —— 提交由 Jev 亲自评审
