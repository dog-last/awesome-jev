# Contributing

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md)

Thanks for helping make this the most *useful* Jev list, not the longest one.

## What we accept

- **Runnable cookbook patterns** — ≤200 lines, one pattern per file, and you must have actually run it against the API (paste the real output in your PR).
- **Independent evaluation results** — with dataset, protocol, and numbers. Negative results are especially welcome.
- **Non-English-scenario benchmarks** — the ecosystem's biggest known gap.
- **Curated links** — only if you add one line on *why it's worth reading*. No bare links, no same-day scaffold projects.
- **Updates to existing entries** — fresh star counts, corrected descriptions, renamed/dead repos, or better one-liners. Small maintenance PRs are welcome and merge fast.

## Rules

1. No vendor marketing copy. Numbers must be sourced and dated.
2. Never commit API keys. `.env` is gitignored; CI will fail the PR if one slips in.
3. Keep languages in sync: every content page has an English version (`*.md`) and a Chinese version (`*.zh-CN.md`) — update both, or mark the PR as one-language and let maintainers follow up.
4. Cookbook scripts must declare dependencies inline (PEP 723) and run with `uv run`.
