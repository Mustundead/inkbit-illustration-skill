# Contributing / 贡献

Keep changes specific to this ink illustration workflow. Submit the brief, affected locale, tool/host, expected behavior, actual behavior, and a minimal permitted reference or result. Remove private screenshots, credentials, local user paths, and material you cannot redistribute.

Update English and Chinese counterparts together, including prompt recipes and meaningful constraints. Version changes to the shared contract in both skill headers and the asset manifest. Add a regression case when a correction represents a reusable failure; do not turn a single scene preference into a universal rule.

Run `python3 scripts/validate.py`. For behavior changes, run relevant cases from `evals/cases.json`; record the host/model actually used, steps taken, and concrete mismatches. A prompt-only exercise is not a rendered-image test. Do not mark unrun cases as passing. Keep visual evidence and original references separate from edited candidates.

Only contribute assets you can share. Add provenance and hashes. Review the license and public diff before publication. Do not add dependency-heavy generation clients or new approval stages without a demonstrated need.

保持修改与墨线插画工作相关。提供需求、受影响语言、工具或宿主、预期与实际行为，以及可分发的最小参考图或结果。移除私人截图、密钥、本机用户路径及无权传播的素材。

同步修改中英文入口、模板及实际约束；通用规则变更时更新两个入口与素材清单的版本。对可复用错误增加回归案例，不把某个场景的偏好变成通用要求。

运行 `python3 scripts/validate.py`。行为变化应执行 `evals/cases.json` 中相关案例，记录实际宿主或模型、执行过程与具体偏差。仅提示词演练不等于图片测试，未执行案例不得记为通过。视觉证据、原参考与编辑候选分别保存。

只贡献有权分享的素材，记录来源及哈希；发布前检查许可与公开差异。没有明确需要时，不添加重型生成客户端或额外审批阶段。
