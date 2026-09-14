# Design and release plan / 设计与发布规划

Version: 0.1.1. The maintainer explicitly authorized publication. / 维护者已明确授权发布。

## Contract / 产品定位

| Decision / 决策 | Implementation / 实现 |
| --- | --- |
| Reusable style, not one mascot / 复用画法而非固定吉祥物 | Silhouette, ink, stipple, negative space form the shared vocabulary. Subject and palette accents remain brief-specific. / 轮廓、墨线、点阵与留白构成通用语言，主体和强调色由需求决定。 |
| One skill, two complete languages / 一个技能、完整双语 | English discovery entry plus full Chinese counterpart; paired references. Avoid duplicate skill IDs. / 英文发现入口、完整中文对应及配对参考文档，避免双 ID。 |
| Progressive disclosure / 按需读取 | Short entrypoint; detailed style, prompt, and quality references loaded only when useful. / 精简入口，按需要读取风格、模板与验收。 |
| Tool portability / 工具可移植 | Host-provided image tool; no embedded API, secret, model claim, or network script. / 由宿主提供图像工具，不内置 API、密钥、模型声明或联网脚本。 |
| Maintainability / 可维护 | Local-link and metadata checks, reference hashes, bilingual parity checks, behavioral cases. / 本地链接、元数据、素材哈希、语言配对及行为案例。 |
| Honest delivery / 如实交付 | Generated, integrated, visually inspected, accepted, and published are distinct. / 生成、集成、目视检查、接受与发布分别记录。 |

## Format sources / 格式依据

Reviewed 2026-09-14:

- [Agent Skills specification](https://agentskills.io/specification): adopted the required name/description frontmatter, matching directory name, relative resources, and portable directory. Optional experimental tool permissions were omitted. / 采用必需元数据、同名目录、相对资源路径与可移植目录，不加入实验性工具授权。
- [Creation best practices](https://agentskills.io/skill-creation/best-practices): adopted task-derived rules, conditional references, and realistic evaluations. Rejected generic design advice and mandatory multi-round approval. / 采用实际任务规则、条件式参考与真实案例评估，不堆积通用设计建议或强制多轮审批。
- [MIT license](https://opensource.org/license/mit): selected for this local open-source candidate; bundled reference provenance is separately disclosed. / 本地开源候选采用 MIT，示例图另有来源说明。

The format is an interoperability specification, not a quality certification. There is no claim that all “open-source skills” share one publishing standard. / 格式规范不是质量认证，也不声称所有开源 skill 共用一个发布标准。

## Evaluation boundary / 验证边界

Structural checks cover discoverability fields, matching name, bounded descriptions, paired locale files, all local Markdown links, licenses, and asset hashes. Behavioral checks cover trigger scope, prompt-only requests, editing invariants, transparent assets, and absent image tools. Rendering quality must be assessed from actual outputs at intended size; text checks cannot establish it.

结构检查覆盖发现字段、目录名、描述长度、双语配对、本地 Markdown 链接、许可证和素材哈希。行为检查覆盖触发范围、仅提示词、编辑保留项、透明素材与工具缺失。图片质量必须检查实际展示结果，不能靠文本校验确定。

## Release path / 发布步骤

1. Review the source package and attribution license choice; confirm the included reference is appropriate to publish. / 审查源码、署名许可选择与参考图的公开范围。
2. Run structural checks and the relevant behavioral cases; document unrun render/host combinations. / 执行结构与相关行为检查，记录未测试的渲染或宿主组合。
3. Create a public repository only when requested, then add its actual URL to the README. / 明确要求后才创建公开仓库，并填入真实 URL。
4. Publish a versioned source archive with checksums; describe tested hosts without general certification claims. / 发布带校验值的版本源码包，如实说明测试宿主。
5. Grow examples through observed use: spot illustration, editorial scene, reference edit, and a coherent series. Add references only when redistribution rights and a concrete teaching purpose are clear. / 根据实际使用逐步增加点缀图、编辑场景、参考修改和系列示例，增加素材前确认分发权与用途。

No registry listing, remote repository, release tag, or generated-image benchmark is implied by this local package. / 本地包不代表已上架、已建远端仓库、已发标签或已完成图片基准测试。

## 0.1.1 attribution update / 署名更新

The initial MIT choice above records the historical draft. For 0.1.1 the maintainer requested attribution: skill content and reference artwork now use CC BY 4.0; maintenance code retains MIT. See [NOTICE](../NOTICE.md). / 上文 MIT 为早期草案记录，0.1.1 按维护者要求将技能内容及参考图改为 CC BY 4.0，维护代码保留 MIT。
