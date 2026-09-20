import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

const navEn = [
  { text: 'Guide', link: '/' },
  { text: 'Use Cases', link: '/use-cases' },
  { text: 'Research', link: '/research' },
  { text: 'Cookbooks', link: '/cookbooks' },
]

const navZh = [
  { text: '指南', link: '/zh/' },
  { text: '用例', link: '/zh/use-cases' },
  { text: '研究', link: '/zh/research' },
  { text: '实战', link: '/zh/cookbooks' },
]

export default withMermaid(
  defineConfig({
    base: '/awesome-jev/',
    title: 'Awesome Jev Guide',
    description: 'A curated guide to Jev, the System One decision model from TypeSafe AI.',
    head: [
      ['link', { rel: 'icon', href: 'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>' }],
    ],
    mermaid: {
      theme: 'base',
      themeVariables: {
        background: '#ffffff',
        primaryColor: '#ffffff',
        primaryTextColor: '#1c1917',
        primaryBorderColor: '#c2410c',
        lineColor: '#a8a29e',
        fontSize: '15px',
      },
    },
    mermaidPlugin: { class: 'mermaid' },
    markdown: {
      // Code blocks always have a dark background (custom.css), so pin a
      // single dark syntax theme instead of VitePress's light/dark pair —
      // otherwise the light-theme colors land on the dark block and are unreadable.
      theme: 'github-dark',
    },
    locales: {
      root: {
        label: 'English',
        lang: 'en',
        themeConfig: {
          nav: navEn,
          outline: { level: [2, 3], label: 'On this page' },
          docFooter: { prev: 'Previous', next: 'Next' },
          editLink: {
            pattern: 'https://github.com/dog-last/awesome-jev/edit/main/docs/:path',
            text: 'Edit this page on GitHub',
          },
        },
      },
      zh: {
        label: '简体中文',
        lang: 'zh-CN',
        link: '/zh/',
        themeConfig: {
          nav: navZh,
          outline: { level: [2, 3], label: '本页目录' },
          docFooter: { prev: '上一页', next: '下一页' },
          editLink: {
            pattern: 'https://github.com/dog-last/awesome-jev/edit/main/docs/:path',
            text: '在 GitHub 上编辑此页',
          },
        },
      },
    },
    themeConfig: {
      logo: '⚡',
      sidebar: false,
      aside: true,
      socialLinks: [{ icon: 'github', link: 'https://github.com/dog-last/awesome-jev' }],
      search: { provider: 'local' },
    },
  })
)
