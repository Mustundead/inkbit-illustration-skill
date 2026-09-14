# Inkbit Illustration · 墨点插画

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

可反复调用的黑白墨线插画 Agent Skill：明确轮廓、干涩笔触、疏密点阵、短排线与纸面留白。由 MU Labs 制作。



## 精选示例

![创作者的工作台](skills/inkbit-illustration/assets/examples/07-workspace.png)

![城市骑行](skills/inkbit-illustration/assets/examples/08-city-cycling.png)

![音乐聆听](skills/inkbit-illustration/assets/examples/09-music.png)

![烘焙厨房](skills/inkbit-illustration/assets/examples/10-baking.png)

![湖畔露营](skills/inkbit-illustration/assets/examples/11-camping.png)

![航海港口](skills/inkbit-illustration/assets/examples/12-harbor.png)

![阅读空间](skills/inkbit-illustration/assets/examples/13-reading-corner.png)

[查看每张图片的提示词](skills/inkbit-illustration/references/selected-gallery.zh-CN.md) · MU Labs / Inkbit Illustration · CC BY 4.0


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

默认简体中文入口是 `SKILL.md`，其他语言使用对应的 `SKILL.<语言>.md`。不要安装两个互相竞争的技能 ID。`agents/openai.yaml` 提供可选 Codex 界面信息，其他宿主不依赖此文件。

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

默认简体中文，支持繁体中文、英文、日文和韩文。各语言有独立使用入口；详细参考资料目前提供简体中文与英文。新生成图片统一纯黑墨色与纯白背景，旧画廊图片不代表已完成颜色修订。
