# Validation / 验证记录

Date: 2026-09-14. Candidate: 0.1.0. Environment: local macOS, Python 3, Codex.

| Check / 检查 | Result / 结果 | Boundary / 边界 |
| --- | --- | --- |
| Skill-creator quick validator, English and Chinese entrypoints | Passed / 通过 | Frontmatter and scaffold checks only / 仅元数据及占位检查 |
| Repository validator | Passed / 通过 | Links, locale file pairs, licenses, UI metadata, image hash, case structure / 链接、双语配对、许可、界面元数据、素材哈希和案例结构 |
| Validator negative fixtures | Wrong name, broken reference, and changed image rejected / 正确拒绝错名、断链及被修改素材 | Temporary isolated copies / 隔离临时副本 |
| Independent prompt-only exercise, gpt-5.6-luna | zh-prompt-only, en-edit-tool-unavailable, negative-dashboard behaved as expected / 三个文本案例符合预期 | No image generation, project edits, or visual scoring / 未生成图片、修改项目或给图片评分 |
| Bilingual semantic review | Shared scope and workflow aligned / 两版范围与流程一致 | Human-readable comparison, not automatic translation equivalence / 文本比较，不是自动翻译等价证明 |

The remaining rendering, transparency, identity, theme, and review fixtures in `evals/cases.json` have not been executed as skill-driven visual benchmarks. Prior illustration work informed the style but does not constitute an independent pass for this package. Other agent hosts and remote GitHub CI have not been run. No publication or certification is claimed.

`evals/cases.json` 中其余生成、透明、角色、主题及图片评审案例，尚未作为本 skill 驱动的视觉基准执行。此前插画工作提供风格来源，不等于本包独立评估通过。其他宿主与远端 GitHub CI 尚未执行，不声称已发布或获认证。

## 0.1.1 release checks / 发布检查

The attribution update was structurally revalidated locally. Earlier prompt exercises remain historical 0.1.0 evidence; visual benchmark limitations are unchanged. / 署名更新已重新通过本地结构检查；早先提示词演练属于 0.1.0 历史证据，视觉基准验证范围未扩大。

## 0.1.2 gallery / 示例画廊

2026-09-14: Six AI-generated subject examples were visually inspected, including a revised cyclist after maintainer feedback. Local metadata, bilingual links and all seven asset hashes passed validation. Actual English generation and edit prompts plus Chinese reusable translations are recorded. These are illustrative examples, not anatomy or engineering benchmarks; Chinese translations were not separately rendered. User acceptance is not claimed. / 六张题材示例已逐张检查，骑行人物按反馈修订。元数据、双语链接与七张素材哈希通过本地验证；记录实际英文生成和修改提示词及中文译写。不声称用户已验收或通过专业结构基准。
