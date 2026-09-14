# Inkbit Illustration · 墨点插画

简体中文 · [English](README.md)

可反复调用的黑白墨线插画 Agent Skill：明确轮廓、干涩笔触、疏密点阵、短排线与纸面留白。由 MU Labs 制作。

![墨线与点阵风格参考](skills/inkbit-illustration/assets/style-reference.png)

图片仅示范画法，其中的猫、梯子、风景和动作不是固定元素，也不是视觉验收基准。

## 题材画廊

| 静物、植物与动物 | 建筑、人物与风景 |
| --- | --- |
| **桌上的早餐**<br>![桌上的早餐](skills/inkbit-illustration/assets/examples/01-still-life.png)<br>用不同点阵密度区分陶瓷、酥皮和纸张。 | **街角书店**<br>![街角书店](skills/inkbit-illustration/assets/examples/04-architecture.png)<br>用墨色层次区分墙面、木框与石板路。 |
| **蕨叶与蘑菇**<br>![蕨叶与蘑菇](skills/inkbit-illustration/assets/examples/02-botanical.png)<br>以细排线描叶脉，用疏密点阵表现苔藓。 | **骑行的午后**<br>![骑行的午后](skills/inkbit-illustration/assets/examples/05-human-motion.png)<br>通过姿态和衣摆表现动感，纹理不盖过人物轮廓。 |
| **林间的狐狸**<br>![林间的狐狸](skills/inkbit-illustration/assets/examples/03-wildlife.png)<br>靠轮廓和顺向笔触表现毛发、重心与步态。 | **海岬灯塔**<br>![海岬灯塔](skills/inkbit-illustration/assets/examples/06-coastal-landscape.png)<br>前景深、远景浅，以留白表现海面与空间。 |

[查看完整图集与中文提示词](skills/inkbit-illustration/references/gallery.zh-CN.md)。AI 生成示例；引用或改编请署名 **MU Labs / Inkbit Illustration**，保留来源与 CC BY 4.0 许可，并说明修改。

## 使用

```text
使用 $inkbit-illustration，为阅读应用画一艘安静的小帆船。
黑白墨点风格，右侧留标题空间，不在图里生成文字。
```

```text
使用 $inkbit-illustration 修改附件，只调整杯子把手角度，
保持杯形、花纹与背景不变。
```

```text
Use $inkbit-illustration to create three separate transparent reading-themed
spot illustrations: a book, a lamp, and a teacup. No lettering or scenery.
```

支持新插画、参考图局部修改、系列素材、提示词编写和视觉评审。入口与参考文档均有完整中英文对应版本。精确产品 UI 与官方图标应使用提供的原件，避免生成模型猜测。

## 安装

可安装的完整目录是 `skills/inkbit-illustration/`。下载源码包后，把此目录复制到使用中的 agent 的技能目录，许可证、来源说明、参考文档和示例图均随包携带。仓库根目录不是 skill 入口。

在本仓库根目录运行以下命令，可安装到本地 Codex：

```sh
skill_dest="${CODEX_HOME:-$HOME/.codex}/skills/inkbit-illustration"
if test -e "$skill_dest"; then
  echo "该位置已有 skill，请先比较版本，再决定是否替换。"
else
  mkdir -p "$(dirname "$skill_dest")"
  cp -R skills/inkbit-illustration "$skill_dest"
fi
```

未立即显示时，使用新会话或宿主的技能刷新机制。本包采用 [Agent Skills 格式](https://agentskills.io/specification)，其他兼容宿主可读取 `SKILL.md`；宿主支持情况及图像工具可用性不同，本包不声称已完成跨宿主认证。

默认英文入口是 `SKILL.md`，中文请求路由到 `SKILL.zh-CN.md`。不要安装两个互相竞争的技能 ID。`agents/openai.yaml` 提供可选 Codex 界面信息，其他宿主不依赖此文件。

## 依赖与限制

读取 skill、编写提示词无需可执行依赖；生成图片需要宿主提供图像生成或编辑工具。本包不内置 API 客户端、密钥、隐藏下载、指定模型或商业服务。不同模型和不同轮次不能保证像素一致。透明通道与角色保持必须检查实际结果。

## 开发

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

校验器检查包结构、元数据、本地链接、语言配对和参考图哈希，不判断插画质量。参阅 [评估案例](evals/cases.json)、[贡献说明](CONTRIBUTING.md) 和 [设计与发布规划](docs/DESIGN.md)。CI 执行相同结构检查。

## 许可与署名

技能内容与参考图采用 [CC BY 4.0](LICENSE)，维护脚本采用 [MIT](scripts/LICENSE)。引用、分享或改编受许可内容时，需署名 **MU Labs / Inkbit Illustration**，附[项目来源](https://github.com/mustundead/inkbit-illustration-skill)与许可链接，并说明修改。完整范围和署名模板见 [NOTICE](NOTICE.md)。当前版本 0.1.1，验证范围见 [验证记录](docs/VALIDATION.md)。
