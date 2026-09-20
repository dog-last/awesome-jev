# Use Cases

What the community is building with Jev, five days in. Stars are point-in-time (2026-09-20) and moving fast. Every entry was checked to exist and to genuinely use TypeSafe's Jev.

## Flagship demos

| Project | ★ | What it does |
|---|---|---|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 10.1k | Browser agent: **one Jev call picks both action and target element**; an LLM is only called to type text. Zürich→London flight booked in **7.1 s** end-to-end |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | 11.8k | Open-source AI trading OS with a documented Jev pre-trade decision module |
| [vercel/eve](https://github.com/vercel/eve) | 5.3k | Vercel's agent framework ships Jev as the **default model** in its `evaluate` path |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 4.5k | Claude Code plugin replacing summary-based compaction with per-item Jev keep/drop decisions — context stays verbatim (156k→62k tokens demo) |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 853 | Official agent-skills package for building with the System One API |

## Browser & desktop agents

| Project | ★ | What it does |
|---|---|---|
| [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) | 391 | Jev picks element/action/risk inside Codex Computer Use — text-only, no screenshots |
| [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) | 217 | "Jev clicks, Codex thinks and verifies" — 5–10× faster browser ops |
| [jkudish/jev-browser](https://github.com/jkudish/jev-browser) | 164 | Browser-use driven by Jev decisions |
| [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | 134 | Voice-controlled real browser; intent+target in ~300 ms per spoken word |
| [savka777/jev-use](https://github.com/savka777/jev-use) | 39 | Mac computer-use via Accessibility API + voice input |
| [skeptrunedev/jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) | 33 | LinkedIn recruiting agent that browses profiles and saves candidates |
| [kevinbadi/jev-voice](https://github.com/kevinbadi/jev-voice) | 27 | whisper.cpp local STT + one Jev call per macOS command |
| [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) | 29 | LLM plans, Jev decides; library + CLI + MCP server |
| [razaanstha/ulka](https://github.com/razaanstha/ulka) | 18 | Experimental browser agent via Vercel AI Gateway |

## Mobile use — Android / iOS agents & testing

| Project | ★ | What it does |
|---|---|---|
| [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) | 248 | Standalone Android agent (Mobilerun): Uber ride SFO→Golden Gate in ~21 s / 9 actions |
| [SomeshSampat2/jev-android-super](https://github.com/SomeshSampat2/jev-android-super) | 0 | On-device Kotlin/Compose agent; "open YouTube and subscribe to MrBeast" in 17 steps / ~32 s, ships an APK |
| [antiyro/jevdroid](https://github.com/antiyro/jevdroid) | 3 | Typed Python framework for Android over ADB; Jev reads the accessibility tree, 314 ms median decision latency |
| [gokulnair2001/Convoy](https://github.com/gokulnair2001/Convoy) | 2 | Semantic E2E testing for iOS/Android/web: YAML natural-language steps, Jev matches intent → control |
| [jaewgwon/jevis](https://github.com/jaewgwon/jevis) | 1 | Dart package on Flutter `integration_test`: describe a goal, Jev picks the next action |
| [ufec/jev-block-android-ad](https://github.com/ufec/jev-block-android-ad) | 3 | "JevNoiseGate": on-device notification/SMS noise filter, fail-open, codes never uploaded |
| [Baran3575/jev-voice-android](https://github.com/Baran3575/jev-voice-android) | 0 | Turkish voice-command app; one parallel Jev call → dial/SMS/alarms, confidence-gated at 0.60 |
| [mkruglikov/droidjev](https://github.com/mkruglikov/droidjev) | 0 | Screenshot-free emulator clicker porting the jev-ultrafast pattern to ADB |
| [Xopher00/jevdevice](https://github.com/Xopher00/jevdevice) | 0 | MCP server controlling a real Android phone; Jev picks targets from the live accessibility tree |
| [InfamousCube/JevPilot](https://github.com/InfamousCube/JevPilot) | 1 | Cross-platform computer-use app (Windows + Android APK), released binaries |
| [Clueless-Creations/jev-ios-ultrafast](https://github.com/Clueless-Creations/jev-ios-ultrafast) | 0 | iOS Simulator runner with step verification and multi-simulator suites |
| [aldouus/jevium](https://github.com/aldouus/jevium) | 0 | Natural-language UI goals executed via Appium or Chrome |

## Games

| Project | ★ | What it does |
|---|---|---|
| [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) | 289 | Plays Super Mario Bros from structured emulator RAM — no screenshots |
| [standardagents/jevpilot](https://github.com/standardagents/jevpilot) | 102 | Three.js driving simulator with Jev autopilot, hosted demo |
| [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) | 75 | Astra plans, Jev controls, with route verification |
| [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake) | 18 | Snake, one Choice per tick — by UmiJS creator sorrycc |
| [ickas/battleship-vs-jev](https://github.com/ickas/battleship-vs-jev) | 0 | 60-game study with live probability heatmaps; hybrid Jev ≈ density baseline |
| [pokertools-arena](https://github.com/pokertools-arena/pokertools-arena.github.io) | 1 | No-limit Hold'em bench seating Jev vs OpenAI-compatible models |
| [atarikcaliskan/jevball](https://github.com/atarikcaliskan/jevball) | 3 | 3D football where all 22 players are separate Jev calls |
| [AbdelStark/heist-one](https://github.com/AbdelStark/heist-one) | 6 | Browser stealth game; Jev makes guard judgments while deterministic code owns the world |

More: [typesafe-chess](https://github.com/Dimesio/typesafe-chess) · [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) · [tetris-jev](https://github.com/chahero/tetris-jev) · [jevs-kitchen-chaos](https://github.com/bebe0307mz/jevs-kitchen-chaos) · [tsai-civ2](https://github.com/phyous/tsai-civ2)

## Dev tools & agent infrastructure

| Project | ★ | What it does |
|---|---|---|
| [thruwire/foreman](https://github.com/thruwire/foreman) | 413 | "Software factory foreman" orchestrating dev work via Jev |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | 376 | Staged code-review workflow + local dashboard driven by Jev judgments |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | 229 | Routes each Claude Code task to the cheapest adequate model |
| [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) | 175 | Local-first MCP plugin for continuous quality review |
| [lakeday-org/perch](https://github.com/lakeday-org/perch) | 161 | Semantic code linting with Jev |
| [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) | 119 | Trims long Bash output before the model sees it |
| [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) | 103 | "grep by meaning" with composable AND/OR meaning queries |
| [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) | 98 | Routes models, tools, and subagents |
| [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) | 101 | Decision layer for the Pi agent: tool-call gate + `jev_ask` |
| [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent) | 95 | Measures steps saved when Jev (not the LLM) picks tools |
| [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | 76 | Per-turn model / reasoning-depth routing for Codex |
| [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) | 76 | Rust CLI ranking agent skills from live session context |
| [mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) | 68 | Fish-style zsh autosuggestions ranked by Jev |
| [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway) | 61 | Local gateway where Jev makes tool-choice for Codex/Claude Code/OpenCode |
| [w3cj/jev-chat](https://github.com/w3cj/jev-chat) | 49 | Tool-calling chatbot with **no LLM** — Jev picks intent/tool/args each turn |
| [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) | 39 | Per-prompt rule selection for coding agents |
| [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi) | 17 | Agent-ergonomic CLI: gates risky calls, screens injection, triages build logs |
| [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | 28 | Context sieve judging every tool result before it enters Claude Code's context |
| [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) | 1 | Reusable GitHub Action: Jev reviews PR/submission classifications |

More: [jev-lint](https://github.com/mizchi/jev-lint) · [commit-miner](https://github.com/devanshbatham/commit-miner) · [jegrep](https://github.com/can1357/jegrep) · [blink](https://github.com/ellipsis-dev/blink) · [jev-cli](https://github.com/Nasrallah-AL/jev-cli) · [jeff](https://github.com/Alurith/jeff) · [yoshi](https://github.com/compozy/yoshi) · [ActionJev](https://github.com/AlexBabescu/ActionJev) · [typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)

## Guardrails, moderation & security

| Project | ★ | What it does |
|---|---|---|
| [kitze/unclutter](https://github.com/kitze/unclutter) | 138 | Browser extension for Jev-powered page-clutter removal with reusable rules |
| [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) | 99 | Guardrails for the Pi coding agent; Jev judges irreversibility and steers |
| [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) | 74 | Finds sponsor reads in videos and skips them |
| [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock) | 58 | Chrome extension asking Jev "is this DOM element an ad?" |
| [RafalWilinski/vibecheck](https://github.com/RafalWilinski/vibecheck) | 42 | Vibe-checks your X posts before you send them |
| [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | 36 | Discord bot: real-time spam/scam filtering and escalation |
| [jomatsu/pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) | 17 | Semantic auto-approval of bash commands |
| [leepokai/jev-guard](https://github.com/leepokai/jev-guard) | 11 | Risk-scores every tool call with session context |

More: [pi-jev-sentinel](https://github.com/harshwasan/pi-jev-sentinel) · [jev-prompt-sentry](https://github.com/ca7ai/jev-prompt-sentry) · [jev-pii-guardrail](https://github.com/jms-dcksn/jev-pii-guardrail) · [Jeeves](https://github.com/Infrawrench/Jeeves) · [jev-comment-triage](https://github.com/soderlind/jev-comment-triage) · [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench)

## Search, RAG & classification

| Project | ★ | What it does |
|---|---|---|
| [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) | 260 | Full web-search pipeline: source selection, query understanding, ranking |
| [brainstormity/Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) | 80 | 50–1000 crypto tweets → Buy/Sell/Hold terminal |
| [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift) | 46 | Batch classification MCP — "classify first, read selectively" |
| [zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) | 4 | zh/en rerank eval, 9,831 pairs: Jev ≈ bge-m3 alone, **RRF fusion +0.090 NDCG** |
| [samdotmak/jev-recall](https://github.com/samdotmak/jev-recall) | 15 | Relevance-not-embedding memory filter |

More: [invalidate](https://github.com/chopratejas/invalidate) · [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) · [jevmail](https://github.com/fazlerocks/jevmail) · [jev-reranking](https://github.com/carlaiau/jev-reranking) · [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) · [reranker](https://github.com/hev/reranker)

## Finance & compliance

| Project | ★ | What it does |
|---|---|---|
| [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | 1.4k | One AI trade decision every block on Monad, by an ex-thirdweb engineer |
| [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) | 281 | IRS tax-form page classifier: 261 form types, 100% strict accuracy at ~$0.001/page |
| [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) | 30 | Live Jev trader on Hyperliquid |
| [myc0576/SmartMoney-Cub](https://github.com/myc0576/SmartMoney-Cub) | 24 | Trading journal + typed-judgment review harness |

More: [Jev-Trades](https://github.com/zadescoxp/Jev-Trades) · [jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader) · [jev-transaction-guard](https://github.com/finrod21/jev-transaction-guard) · [system1-fraud-interceptor](https://github.com/ordepas/system1-fraud-interceptor-demo)

## Robotics, IoT & smart home

| Project | ★ | What it does |
|---|---|---|
| [rokbenko/quackd](https://github.com/rokbenko/quackd) | 217 | One CLI for robot fleets with per-robot decision models |
| [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | 81 | Camera-only autonomous quadrotor in MuJoCo; Jev at 2.5 Hz decides "what the situation means" while code owns control |
| [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) | 27 | Home Assistant integration with token-budget kill switch |
| [arielweinberger/jev-autopilot](https://github.com/arielweinberger/jev-autopilot) | 5 | Jev flies a drone point-to-point in a random city |

## Databases & data tooling

| Project | ★ | What it does |
|---|---|---|
| [realZachi/pg-jev](https://github.com/realZachi/pg-jev) | 228 | PostgreSQL extension: ask tables questions in plain language |
| [pithings/advocaat](https://github.com/pithings/advocaat) | 85 | Typed client for asking AI questions about your data |
| [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) | 79 | PG extension for categorical classification |
| [jexp/neo4jev](https://github.com/jexp/neo4jev) | 43 | Jev navigates a Neo4j graph by classifying neighbouring relations (by Neo4j's Michael Hunger) |

More: [jevql](https://github.com/kylemclaren/jevql) · [vgi-typesafe](https://github.com/Query-farm/vgi-typesafe) (DuckDB) · [sqlite-jev](https://github.com/mgaitan/sqlite-jev)

## SDKs, MCP & integrations

- **Official**: Python/JS SDKs ([docs](https://docs.typesafe.ai/introduction)) · [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) (LLM-backed comparison adapter)
- **MCP servers**: [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) (129★) · [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) (123★, Go single binary) · [tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge) (ACP+MCP bridge) · [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp)
- **Community SDKs**: [obie/ruby_decision_model](https://github.com/obie/ruby_decision_model) (Ruby, by Obie Fernandez) · [dannote/jev](https://github.com/dannote/jev) (Elixir/OTP) · [Twister915/typesafe-ai](https://github.com/Twister915/typesafe-ai) (Rust) · [huncho](https://github.com/edgardcham/huncho) (decisions-as-code with hysteresis) · [JevSwiftSDK](https://github.com/NSStudent/JevSwiftSDK) (Swift) — plus Go, Java/Kotlin, .NET, PHP/Laravel, Scala clients
- **Frameworks & gateways**: [yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router) (semantic HTTP routing, by Hono's creator) · [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) (nDCG@5 0.340→0.396) · [typesafe_agent_gates](https://github.com/ThiagaoBR/typesafe_agent_gates) (LangChain middleware) · [kushals256/jevcache](https://github.com/kushals256/jevcache) (skip the LLM when intent matches) · [RyanKung/rotom](https://github.com/RyanKung/rotom) · [new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe) · n8n nodes ([vibe-with-me-tools](https://github.com/vibe-with-me-tools/n8n-nodes-jev))
