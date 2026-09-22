---
name: inkbit-illustration
description: Create or edit retro monochrome ink illustrations with stippling, short hatching, bold silhouettes, and paper negative space. Use for illustrated hero art, editorial scenes, spot art, or asset series when the user requests Inkbit, 墨点插画, or this printlike ink style. Not for generic website redesigns, exact UI rendering, or small edits to existing vector icons.
license: CC-BY-4.0
metadata:
  author: MU LABS
  version: "0.1.3"
  language: en
---

# MU LABS Inkbit Illustration

Build illustrations from strong contours, black shapes, form-following stippling, and paper negative space. Preserve the user's subject and composition. Cats, ladders, mountains, and retro windows are examples, not required motifs.

[简体中文](SKILL.md) · [繁體中文](SKILL.zh-TW.md) · [English](SKILL.en.md) · [日本語](SKILL.ja.md) · [한국어](SKILL.ko.md)

Default to Simplified Chinese when no language is specified. Follow an explicit language choice, otherwise match the user: Simplified Chinese, Traditional Chinese, English, Japanese or Korean. Read only the relevant language entrypoint.

## Scope the request

Distinguish new artwork, a local edit, an asset series, prompt writing, and review only. Reuse the conversation and project context for subject, destination, dimensions, background, and references. Choose reasonable reversible defaults instead of imposing a questionnaire or an options round.

Label each input as a style reference, identity reference, composition reference, or edit target, and inspect it. The user's selected reference takes precedence over bundled examples.

## Style essentials

- Establish a readable thumbnail silhouette before texture. Black masses carry visual weight; dots and short hatching model form rather than coat the entire canvas.
- Use slightly dry, varied contours. Vary dot density with shadow, material, and depth. Avoid mechanical outlines and a uniform noise overlay.
- Use pure black ink on pure white; honor an explicit transparent background.
- No cream, yellowing, brown or colored accents. Model shading with black dots, short hatching and white space.
- Leave breathing room. Find playfulness in pose, scale, and relationships rather than accumulations of stickers and symbols.

Read the [style guide](references/style-guide.md) when composition or material needs detail. Inspect the [visual reference](assets/style-reference.png) when matching the mark-making; do not copy its scene by default.

## Execute

**New artwork:** Organize a prompt around subject, action, composition, ink treatment, background, and delivery. Add only details that serve the brief. Use [prompt recipes](references/prompts.md) when useful.

**Local edit:** Separate allowed changes from invariants. Lock the relevant proportions, markings/material, silhouette, camera, and surroundings. Use image editing rather than generating from a fresh verbal description. When identity drifts, return to the most recent acceptable source instead of repeatedly editing the drifted result.

**Series:** Fix line weight, dot scale, palette, subject occupancy, and camera in a shared prompt block, then vary subject and action. Deliver the requested count without expanding into an unsolicited brand kit.

Use an image generation/editing tool actually available in the host; prefer its built-in image tool when available and follow its reference, alpha, and output requirements. Do not invent model versions or unsupported parameters. This skill does not authorize purchases, plugin installation, or switching to a paid API. Without an image tool, provide a prompt labeled as not yet rendered. Do not generate when the request is only for prompts or review.

## Inspect and deliver

Inspect the image and its intended display size: subject/action clarity, reference identity, physical contacts and occlusion, texture legibility, and requested color/background. Use the relevant checks in [quality guidance](references/quality.md).

Fix observed defects with focused edits. If two attempts at the same defect make no progress, identify the remaining mismatch and retain the candidate; do not declare success or loop indefinitely.

Save versioned files and retain sources. If project integration is authorized, copy the asset into the project, update the real reference, and inspect the requested running page or app. Generation alone does not authorize project edits. Deliver the image, actual saved path, final prompt or its record, and any concrete unmet request. Distinguish generated, integrated, verified, and user accepted.

Use supplied originals or native typesetting for exact UI, real icons, and readable copy. Do not have a model guess brand marks, measurements, or interface geometry. Dark-mode adaptation must not blindly invert character markings or brand colors.

## Attribution

When sharing or adapting package content, follow [attribution and licensing](NOTICE.md): credit MU LABS / MU LABS Inkbit Illustration, retain source and CC BY 4.0 links, and describe changes. Do not automatically draw attribution into user artwork; use appropriate documentation or credits.

[Subject examples and prompts](references/gallery.md) cover product heroes, empty states, wildlife, buildings, people and landscapes. Read relevant examples as needed rather than loading the whole gallery.

## Language and color precedence

[简体中文](SKILL.md) · [繁體中文](SKILL.zh-TW.md) · [English](SKILL.en.md) · [日本語](SKILL.ja.md) · [한국어](SKILL.ko.md)

Default to Simplified Chinese; follow an explicit language choice or match the user’s supported language. Use pure black ink on pure white, with no cream, yellowing, brown or colored accents. Build shading through black stipple, short hatching and white space. Honor an explicit transparent background. This overrides warm-paper instructions in historical references and prompts.
