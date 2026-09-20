# 贡献指南

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md)

感谢你把这份清单变得更有用，而不是更长。

## 我们接受什么

- **可运行的 cookbook 模式** —— 每个文件 ≤200 行、只讲一个模式，且必须真实调过 API（PR 里贴上真实输出）。
- **独立评测结果** —— 附数据集、协议和数字。反面结果尤其欢迎。
- **非英语场景基准** —— 生态目前最大的空白。
- **精选链接** —— 必须附一句"为什么值得读"。不收裸链接，不收同日批量脚手架项目。
- **对已有条目的更新** —— 刷新 star 数、修正描述、处理改名/失效仓库、改写更准确的推荐语。这类维护性小 PR 非常欢迎，合入很快。

## 规则

1. 不收厂商营销文案。数字必须注明来源和日期。
2. 永远不要提交 API key。`.env` 已被 gitignore，CI 会拦截误提交。
3. 保持双语同步：每个内容页都有英文版（`*.md`）和中文版（`*.zh-CN.md`）—— 两个都改，或在 PR 中注明只改了一种语言，由维护者补齐。
4. Cookbook 脚本必须内联声明依赖（PEP 723），并可用 `uv run` 直接运行。

## 本地预览网站

网站是 `docs/` 目录下的 [VitePress](https://vitepress.dev) 应用（需要 Node 20+）：

```bash
npm ci              # 安装依赖（仅首次）
npm run docs:dev    # 开发服务器，热更新 → http://localhost:5173/awesome-jev/
```

其他命令：`npm run docs:build`（生产构建到 `docs/.vitepress/dist`，与 CI 一致）、`npm run docs:preview`（预览构建产物）。

网站内容在 `docs/*.md`（英文）和 `docs/zh/*.md`（中文）—— 每个页面都必须双语存在。样式微调在 `docs/.vitepress/theme/custom.css`，导航与多语言配置在 `docs/.vitepress/config.mts`。向 `main` 推送 `docs/**` 下的改动会自动重新构建并部署 GitHub Pages。
