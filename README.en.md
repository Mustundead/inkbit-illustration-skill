# MU LABS Inkbit Illustration

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A reusable Agent Skill for monochrome ink illustrations: strong silhouettes, dry contours, stippling, short hatching, and generous paper negative space. By MU LABS.



## Selected examples

![Creative workspace](skills/inkbit-illustration/assets/examples/07-workspace.png)

![City cycling](skills/inkbit-illustration/assets/examples/08-city-cycling.png)

![Listening to music](skills/inkbit-illustration/assets/examples/09-music.png)

![Baking kitchen](skills/inkbit-illustration/assets/examples/10-baking.png)

![Lakeside camping](skills/inkbit-illustration/assets/examples/11-camping.png)

![Sailing harbor](skills/inkbit-illustration/assets/examples/12-harbor.png)

![Reading corner](skills/inkbit-illustration/assets/examples/13-reading-corner.png)

[Image prompts](skills/inkbit-illustration/references/selected-gallery.md) · MU LABS / MU LABS Inkbit Illustration · CC BY 4.0


## Use it

```text
Use $inkbit-illustration to create a quiet ink illustration of a sailboat
for a reading app. Leave space on the right for a heading. No lettering.
```

```text
Use $inkbit-illustration to edit the attached illustration.
Change only the cup handle angle; preserve its shape, pattern, and background.
```

```text
使用 $inkbit-illustration，创作一组黑白墨点风格的阅读主题插画。
三个独立透明素材：书、台灯、茶杯。不要加文字或场景背景。
```

Supports new illustrations, reference-based edits, asset series, prompt writing, and visual review. Chinese and English instructions and references are complete counterparts. Exact product UI and official logos should use supplied originals rather than generated guesses.

## Install

The portable skill is `skills/inkbit-illustration/`. Download this source package, then copy that complete directory into your agent's skill location. It includes its own license, attribution, references, and image. The repository root is not the skill entrypoint.

For a local Codex installation, run from this repository root:

```sh
skill_dest="${CODEX_HOME:-$HOME/.codex}/skills/inkbit-illustration"
if test -e "$skill_dest"; then
  echo "A skill already exists there. Compare versions before replacing it."
else
  mkdir -p "$(dirname "$skill_dest")"
  cp -R skills/inkbit-illustration "$skill_dest"
fi
```

Use a fresh session or the host's skill refresh mechanism if it does not appear immediately. The package uses the [Agent Skills format](https://agentskills.io/specification). Other compatible hosts can read `SKILL.md`; host support and image-tool availability vary and are not certified here.

`SKILL.md` is the default Simplified Chinese entrypoint; five language entrypoints share one skill ID. Do not install two competing skill IDs. `agents/openai.yaml` adds optional Codex UI metadata; it is not required for other hosts.

## Requirements and limits

Reading the skill and preparing prompts needs no executable dependency. Rendering requires an image generation/editing tool supplied by the host. The skill includes no API client, credentials, hidden downloads, model pin, or bundled commercial service. It cannot guarantee identical images across models or runs. Transparency and visual identity require inspection of the actual output.

## Development

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

The validator checks package structure, metadata, local links, locale pairs, and reference hashes. It does not judge illustration quality. See [evaluation cases](evals/cases.json), [contribution guidance](CONTRIBUTING.md), and [design and release plan](docs/DESIGN.md). CI runs the same structural checks.

## License and attribution

Skill content and artwork use [CC BY 4.0](LICENSE); maintenance code uses [MIT](scripts/LICENSE). When sharing or adapting licensed material, credit **MU LABS / MU LABS Inkbit Illustration**, include the [source](https://github.com/mustundead/inkbit-illustration-skill) and license links, and describe modifications. See [NOTICE](NOTICE.md) for scope and a credit template. Version: 0.1.1. See the [validation record](docs/VALIDATION.md) for tested boundaries.

Simplified Chinese is the default, with Traditional Chinese, English, Japanese and Korean entrypoints. Detailed reference documents remain available in Simplified Chinese and English. New images use black ink on pure white; existing gallery images have not been recolored.
