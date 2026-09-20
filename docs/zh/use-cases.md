# 用例库

发布仅五天，社区用 Jev 构建的东西。Star 为 2026-09-20 时点数据，仍在快速变动。每个条目都核实过真实存在且确实使用了 TypeSafe 的 Jev。

## 旗舰级演示

| 项目 | ★ | 做什么 |
|---|---|---|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 10.1k | 浏览器智能体：**一次 Jev 调用同时选出动作和目标元素**，LLM 只在输入文字时调用。订苏黎世→伦敦机票端到端 **7.1 秒** |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | 11.8k | 开源 AI 交易操作系统，内置文档化的 Jev 盘前决策模块 |
| [vercel/eve](https://github.com/vercel/eve) | 5.3k | Vercel 智能体框架，Jev 是其 `evaluate` 路径的**默认模型** |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 4.5k | Claude Code 插件：用逐条 Jev 保留/丢弃决策替代摘要式压缩 —— 上下文保持原文（演示 156k→62k token） |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 853 | 官方智能体技能包，教 agent 使用 System One API |

## 浏览器与桌面智能体

| 项目 | ★ | 做什么 |
|---|---|---|
| [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) | 391 | 在 Codex Computer Use 中由 Jev 选择元素/动作/风险 —— 纯文本，无截图 |
| [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) | 217 | "Jev 点击，Codex 思考与验证" —— 浏览器操作快 5–10 倍 |
| [jkudish/jev-browser](https://github.com/jkudish/jev-browser) | 164 | 由 Jev 决策驱动的浏览器智能体 |
| [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | 134 | 语音控制真实浏览器；每个语音指令约 300ms 内决定意图+目标 |
| [savka777/jev-use](https://github.com/savka777/jev-use) | 39 | 通过 Accessibility API + 语音输入的 Mac 桌面操控 |
| [skeptrunedev/jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) | 33 | 浏览领英档案并保存候选人的招聘智能体 |
| [kevinbadi/jev-voice](https://github.com/kevinbadi/jev-voice) | 27 | whisper.cpp 本地语音转写 + 每条命令一次 Jev 调用的 macOS 自动化 |
| [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) | 29 | LLM 规划、Jev 决策；库 + CLI + MCP 服务器 |
| [razaanstha/ulka](https://github.com/razaanstha/ulka) | 18 | 经 Vercel AI Gateway 的实验性浏览器智能体 |

## 移动方向 —— Android / iOS 智能体与测试

| 项目 | ★ | 做什么 |
|---|---|---|
| [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) | 248 | 独立 Android 智能体（Mobilerun）：Uber 打车 SFO→金门大桥约 21 秒 / 9 步 |
| [SomeshSampat2/jev-android-super](https://github.com/SomeshSampat2/jev-android-super) | 0 | 端侧 Kotlin/Compose 智能体；"打开 YouTube 订阅 MrBeast"17 步约 32 秒，附 APK |
| [antiyro/jevdroid](https://github.com/antiyro/jevdroid) | 3 | 基于 ADB 的类型化 Python 安卓控制框架；Jev 读无障碍树，决策中位延迟 314ms |
| [gokulnair2001/Convoy](https://github.com/gokulnair2001/Convoy) | 2 | iOS/Android/Web 语义化端到端测试：YAML 自然语言步骤，Jev 匹配意图→控件 |
| [jaewgwon/jevis](https://github.com/jaewgwon/jevis) | 1 | 基于 Flutter `integration_test` 的 Dart 包：描述目标，Jev 选下一步动作 |
| [ufec/jev-block-android-ad](https://github.com/ufec/jev-block-android-ad) | 3 | "JevNoiseGate"：端侧通知/短信噪音过滤，fail-open 设计，验证码不出设备 |
| [Baran3575/jev-voice-android](https://github.com/Baran3575/jev-voice-android) | 0 | 土耳其语语音指令应用；一次并行 Jev 调用 → 拨号/短信/闹钟，置信度 0.60 门控 |
| [mkruglikov/droidjev](https://github.com/mkruglikov/droidjev) | 0 | 无截图模拟器点击器，把 jev-ultrafast 模式移植到 ADB |
| [Xopher00/jevdevice](https://github.com/Xopher00/jevdevice) | 0 | MCP 服务器控制真实安卓手机；Jev 从实时无障碍树中选目标 |
| [InfamousCube/JevPilot](https://github.com/InfamousCube/JevPilot) | 1 | 跨平台电脑操控应用（Windows + Android APK），有发布包 |
| [Clueless-Creations/jev-ios-ultrafast](https://github.com/Clueless-Creations/jev-ios-ultrafast) | 0 | iOS 模拟器运行器，带逐步验证与多模拟器套件 |
| [aldouus/jevium](https://github.com/aldouus/jevium) | 0 | 自然语言 UI 目标，经 Appium 或 Chrome 执行 |

## 游戏

| 项目 | ★ | 做什么 |
|---|---|---|
| [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) | 289 | 读模拟器 RAM 结构化状态玩超级马里奥 —— 无截图 |
| [standardagents/jevpilot](https://github.com/standardagents/jevpilot) | 102 | Three.js 驾驶模拟器 + Jev 自动驾驶，有在线 demo |
| [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) | 75 | Astra 规划、Jev 控制玩 Minecraft，带路线验证 |
| [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake) | 18 | 每 tick 一次 Choice 玩贪吃蛇 —— 作者是 UmiJS 创始人 sorrycc（云谦） |
| [ickas/battleship-vs-jev](https://github.com/ickas/battleship-vs-jev) | 0 | 60 局海战棋研究 + 实时概率热力图；混合策略 ≈ 密度基线 |
| [pokertools-arena](https://github.com/pokertools-arena/pokertools-arena.github.io) | 1 | 无限注德州扑克基准，Jev 对阵 OpenAI 兼容模型 |
| [atarikcaliskan/jevball](https://github.com/atarikcaliskan/jevball) | 3 | 3D 足球赛，22 名球员各是一次独立 Jev 调用 |
| [AbdelStark/heist-one](https://github.com/AbdelStark/heist-one) | 6 | 浏览器潜入游戏；Jev 做守卫判断，确定性代码掌管世界 |

更多：[typesafe-chess](https://github.com/Dimesio/typesafe-chess) · [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) · [tetris-jev](https://github.com/chahero/tetris-jev) · [jevs-kitchen-chaos](https://github.com/bebe0307mz/jevs-kitchen-chaos) · [tsai-civ2](https://github.com/phyous/tsai-civ2)

## 开发工具与智能体基础设施

| 项目 | ★ | 做什么 |
|---|---|---|
| [thruwire/foreman](https://github.com/thruwire/foreman) | 413 | "软件工厂工头"，用 Jev 编排开发工作流 |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | 376 | 分阶段代码评审工作流 + 本地仪表盘 |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | 229 | 把每个 Claude Code 任务路由到够用且最便宜的模型 |
| [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) | 175 | 本地优先的持续质量评审 MCP 插件 |
| [lakeday-org/perch](https://github.com/lakeday-org/perch) | 161 | 用 Jev 做语义化代码 lint |
| [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) | 119 | 在模型看到之前裁剪过长的 Bash 输出 |
| [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) | 103 | "按语义 grep"，支持 AND/OR 组合语义查询 |
| [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) | 98 | 路由模型、工具和子智能体 |
| [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) | 101 | Pi 智能体的决策层：工具调用门控 + `jev_ask` |
| [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent) | 95 | 量化 Jev（而非 LLM）选工具能省多少步 |
| [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | 76 | Codex 每轮模型/推理深度路由 |
| [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) | 76 | Rust CLI：基于实时会话上下文给 agent 技能排序 |
| [mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) | 68 | Jev 排序的 fish 风格 zsh 历史自动建议 |
| [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway) | 61 | 本地网关，由 Jev 为 Codex/Claude Code/OpenCode 做工具选择 |
| [w3cj/jev-chat](https://github.com/w3cj/jev-chat) | 49 | **不用 LLM** 的工具调用聊天机器人 —— 每轮由 Jev 选意图/工具/参数 |
| [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) | 39 | 为编码智能体按 prompt 选规则 |
| [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi) | 17 | 面向 agent 的 CLI：门控危险调用、筛查注入、分拣构建日志 |
| [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | 28 | 上下文筛：每条工具结果进入 Claude Code 上下文前先过 Jev |
| [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) | 1 | 可复用 GitHub Action：用 Jev 评审 PR/提交分类 |

更多：[jev-lint](https://github.com/mizchi/jev-lint) · [commit-miner](https://github.com/devanshbatham/commit-miner) diff 分类 · [jegrep](https://github.com/can1357/jegrep) · [blink](https://github.com/ellipsis-dev/blink) · [jev-cli](https://github.com/Nasrallah-AL/jev-cli) · [jeff](https://github.com/Alurith/jeff) · [yoshi](https://github.com/compozy/yoshi) · [ActionJev](https://github.com/AlexBabescu/ActionJev) · [typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)

## 护栏、内容审核与安全

| 项目 | ★ | 做什么 |
|---|---|---|
| [kitze/unclutter](https://github.com/kitze/unclutter) | 138 | 浏览器扩展：Jev 驱动的页面杂乱清除，规则可复用 |
| [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) | 99 | Pi 编码智能体护栏；Jev 判断不可逆性并引导而非打断 |
| [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) | 74 | 检测视频中的口播广告并自动跳过 |
| [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock) | 58 | Chrome 扩展：问 Jev "这个 DOM 元素是广告吗？" |
| [RafalWilinski/vibecheck](https://github.com/RafalWilinski/vibecheck) | 42 | 发推前先让 Jev 帮你"vibe check" |
| [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | 36 | Discord 机器人：实时垃圾信息/诈骗链接过滤与升级 |
| [jomatsu/pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) | 17 | bash 命令的语义化自动批准 |
| [leepokai/jev-guard](https://github.com/leepokai/jev-guard) | 11 | 结合会话上下文给每次工具调用做风险评分 |

更多：[pi-jev-sentinel](https://github.com/harshwasan/pi-jev-sentinel) 注入筛查 · [jev-prompt-sentry](https://github.com/ca7ai/jev-prompt-sentry) LLM 防火墙 · [jev-pii-guardrail](https://github.com/jms-dcksn/jev-pii-guardrail) UiPath PII · [Jeeves](https://github.com/Infrawrench/Jeeves) · [jev-comment-triage](https://github.com/soderlind/jev-comment-triage) · [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench)

## 搜索、RAG 与分类

| 项目 | ★ | 做什么 |
|---|---|---|
| [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) | 260 | 完整网络搜索管线：信源选择、查询理解、相关度排序 |
| [brainstormity/Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) | 80 | 50–1000 条加密货币推文 → 买/卖/持有终端 |
| [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift) | 46 | 批量分类 MCP —— "先分类，再选择性阅读" |
| [zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) | 4 | 中英重排评测 9,831 对：Jev 单独 ≈ bge-m3，**RRF 融合 +0.090 NDCG** |
| [samdotmak/jev-recall](https://github.com/samdotmak/jev-recall) | 15 | 基于相关度而非 embedding 的记忆过滤器 |

更多：[invalidate](https://github.com/chopratejas/invalidate) 记忆失效 · [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) 数据集筛选 · [jevmail](https://github.com/fazlerocks/jevmail) Gmail 分拣 · [jev-reranking](https://github.com/carlaiau/jev-reranking) · [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) · [reranker](https://github.com/hev/reranker)

## 金融与合规

| 项目 | ★ | 做什么 |
|---|---|---|
| [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | 1.4k | Monad 链上每个区块一次 AI 交易决策，作者是前 thirdweb 工程师 |
| [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) | 281 | IRS 税表页面分类器：261 种表单，100% 严格准确率，约 $0.001/页 |
| [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) | 30 | Hyperliquid 上的实盘 Jev 交易员 |
| [myc0576/SmartMoney-Cub](https://github.com/myc0576/SmartMoney-Cub) | 24 | 交易日志 + 类型化判断复盘工具 |

更多：[Jev-Trades](https://github.com/zadescoxp/Jev-Trades) · [jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader) · [jev-transaction-guard](https://github.com/finrod21/jev-transaction-guard) · [system1-fraud-interceptor](https://github.com/ordepas/system1-fraud-interceptor-demo)

## 机器人、IoT 与智能家居

| 项目 | ★ | 做什么 |
|---|---|---|
| [rokbenko/quackd](https://github.com/rokbenko/quackd) | 217 | 机器人舰队统一 CLI，每台机器人配决策模型 |
| [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | 81 | MuJoCo 纯视觉自主四旋翼；Jev 以 2.5Hz 判断"当前态势"，代码负责实时控制 |
| [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) | 27 | Home Assistant 集成，带 token 预算熔断 |
| [arielweinberger/jev-autopilot](https://github.com/arielweinberger/jev-autopilot) | 5 | Jev 在随机城市中点对点自主飞行无人机 |

## 数据库与数据工具

| 项目 | ★ | 做什么 |
|---|---|---|
| [realZachi/pg-jev](https://github.com/realZachi/pg-jev) | 228 | PostgreSQL 扩展：用自然语言向数据表提问 |
| [pithings/advocaat](https://github.com/pithings/advocaat) | 85 | 类型化客户端：向你的数据提 AI 问题 |
| [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) | 79 | PG 分类扩展 |
| [jexp/neo4jev](https://github.com/jexp/neo4jev) | 43 | Jev 通过分类相邻关系在 Neo4j 图中导航（作者：Neo4j 的 Michael Hunger） |

更多：[jevql](https://github.com/kylemclaren/jevql) Postgres 的 `jev()` 过滤 · [vgi-typesafe](https://github.com/Query-farm/vgi-typesafe) DuckDB · [sqlite-jev](https://github.com/mgaitan/sqlite-jev)

## SDK、MCP 与集成

- **官方**：Python/JS SDK（[文档](https://docs.typesafe.ai/introduction)）· [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)（LLM 后端对比适配器）
- **MCP 服务器**：[jkudish/jev-mcp](https://github.com/jkudish/jev-mcp)（129★）· [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)（123★，Go 单文件）· [tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge)（ACP+MCP 桥）· [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp)
- **社区 SDK**：[obie/ruby_decision_model](https://github.com/obie/ruby_decision_model)（Ruby，Obie Fernandez）· [dannote/jev](https://github.com/dannote/jev)（Elixir/OTP）· [Twister915/typesafe-ai](https://github.com/Twister915/typesafe-ai)（Rust）· [huncho](https://github.com/edgardcham/huncho)（决策即代码 + 迟滞阈值）· [JevSwiftSDK](https://github.com/NSStudent/JevSwiftSDK)（Swift）—— 另有 Go、Java/Kotlin、.NET、PHP/Laravel、Scala 客户端
- **框架与网关**：[yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router)（语义化 HTTP 路由，Hono 作者）· [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)（nDCG@5 0.340→0.396）· [typesafe_agent_gates](https://github.com/ThiagaoBR/typesafe_agent_gates)（LangChain 中间件）· [kushals256/jevcache](https://github.com/kushals256/jevcache)（意图相同则跳过 LLM）· [RyanKung/rotom](https://github.com/RyanKung/rotom) · [new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe) · n8n 节点（[vibe-with-me-tools](https://github.com/vibe-with-me-tools/n8n-nodes-jev)）
