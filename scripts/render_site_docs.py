from __future__ import annotations

from html import escape
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
import subprocess
import sys
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
DIST_ROOT = ROOT / "dist"
VERSION = "1.1.0"
PACKAGE_ROOT = DIST_ROOT / f"dama-data-project-skills-v{VERSION}"
DOCS_REL = PurePosixPath("site-docs") / f"v{VERSION}"
DOCS_ROOT = DIST_ROOT / DOCS_REL


def split_front_matter(markdown: str) -> tuple[dict[str, str], str]:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, markdown

    end = next((index for index in range(1, len(lines)) if lines[index].strip() in {"---", "..."}), None)
    if end is None:
        return {}, markdown

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            value = match.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            metadata[match.group(1)] = value
    return metadata, "\n".join(lines[end + 1 :]).lstrip("\n")


def document_title(markdown: str, relative_source: PurePosixPath) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*#*\s*$", markdown)
    if match:
        return re.sub(r"[`*_]", "", match.group(1)).strip()
    return relative_source.stem.replace("-", " ").replace("_", " ").title()


def checked_source_target(relative_path: str) -> str:
    normalized = posixpath.normpath(relative_path)
    if normalized in {"", ".", ".."} or normalized.startswith(("../", "/")):
        raise ValueError(f"Markdown link escapes the release package: {relative_path}")
    target = PACKAGE_ROOT / PurePosixPath(normalized)
    if not target.is_file():
        raise ValueError(f"Broken package link: {relative_path}")
    return normalized


def rewrite_local_href(
    href: str,
    relative_source: PurePosixPath,
    relative_output: PurePosixPath,
) -> str:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return href

    decoded_path = unquote(parsed.path)
    if decoded_path.startswith("/"):
        raise ValueError(f"Root-relative package link is unsupported: {href}")
    source_target = checked_source_target(
        posixpath.join(relative_source.parent.as_posix(), decoded_path)
    )

    if source_target.lower().endswith(".md"):
        output_target = DOCS_REL / PurePosixPath(source_target).with_suffix(".html")
    else:
        output_target = PurePosixPath(PACKAGE_ROOT.name) / source_target

    encoded_target = relative_url(output_target, relative_output)
    return urlunsplit(("", "", encoded_target, parsed.query, parsed.fragment))


class HrefRewriter(HTMLParser):
    def __init__(self, transform) -> None:
        super().__init__(convert_charrefs=False)
        self.transform = transform
        self.parts: list[str] = []

    @staticmethod
    def _render_attrs(attrs: list[tuple[str, str | None]]) -> str:
        rendered = []
        for name, value in attrs:
            if value is None:
                rendered.append(f" {name}")
            else:
                rendered.append(f' {name}="{escape(value, quote=True)}"')
        return "".join(rendered)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        rewritten = [
            (name, self.transform(value) if name == "href" and value else value)
            for name, value in attrs
        ]
        self.parts.append(f"<{tag}{self._render_attrs(rewritten)}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        rewritten = [
            (name, self.transform(value) if name == "href" and value else value)
            for name, value in attrs
        ]
        self.parts.append(f"<{tag}{self._render_attrs(rewritten)} />")

    def handle_endtag(self, tag: str) -> None:
        self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.parts.append(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl: str) -> None:
        self.parts.append(f"<!{decl}>")

    def handle_pi(self, data: str) -> None:
        self.parts.append(f"<?{data}>")


def rewrite_markdown_links(
    fragment: str,
    relative_source: PurePosixPath,
    relative_output: PurePosixPath,
) -> str:
    parser = HrefRewriter(
        lambda href: rewrite_local_href(href, relative_source, relative_output)
    )
    parser.feed(fragment)
    parser.close()
    return "".join(parser.parts)


def relative_url(target: PurePosixPath, current_output: PurePosixPath) -> str:
    current_in_dist = DOCS_REL / current_output
    relative = posixpath.relpath(target.as_posix(), start=current_in_dist.parent.as_posix())
    return quote(relative, safe="/-._~")


def skill_metadata(metadata: dict[str, str]) -> str:
    name = metadata.get("name")
    description = metadata.get("description")
    if not name and not description:
        return ""
    name_html = f'<code>{escape(name)}</code>' if name else ""
    description_html = f'<p>{escape(description)}</p>' if description else ""
    return (
        '<aside class="docs-skill-summary" aria-label="技能元数据 Skill metadata">'
        f'<div><span class="docs-meta-label">SKILL ID</span>{name_html}</div>'
        f"{description_html}</aside>"
    )


def page_shell(
    title: str,
    language: str,
    fragment: str,
    metadata: dict[str, str],
    relative_source: PurePosixPath,
    relative_output: PurePosixPath,
) -> str:
    stylesheet = relative_url(PurePosixPath("assets/site.css"), relative_output)
    language_script = relative_url(PurePosixPath("assets/docs-language.js"), relative_output)
    home = relative_url(PurePosixPath("index.html"), relative_output)
    source = relative_url(PurePosixPath(PACKAGE_ROOT.name) / relative_source, relative_output)
    chinese_guide = relative_url(DOCS_REL / "README.html", relative_output)
    english_guide = relative_url(DOCS_REL / "README.en.html", relative_output)
    heading = escape(title)
    summary_html = skill_metadata(metadata)
    summary = f"      {summary_html}\n" if summary_html else ""
    return f'''<!doctype html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{heading} — DAMA Data Project Skills documentation">
  <title>{heading} · DAMA Data Project Skills</title>
  <link rel="stylesheet" href="{stylesheet}">
  <script src="{language_script}" defer></script>
</head>
<body class="docs-page">
  <a class="skip-link" href="#document-content">跳转到正文 / Skip to content</a>
  <header class="docs-header content-wrap">
    <a class="docs-brand" href="{home}">
      <span class="docs-brand-mark" aria-hidden="true">D</span>
      <span><strong>DAMA DATA PROJECT SKILLS</strong><small>DOCUMENTATION · RELEASE {VERSION}</small></span>
    </a>
    <nav class="docs-nav" aria-label="文档导航 / Document navigation">
      <a class="docs-home" href="{home}">← 技能首页 / Skill index</a>
      <a href="{chinese_guide}">中文指南</a>
      <a href="{english_guide}">English guide</a>
      <a class="source-markdown" href="{source}" download rel="alternate">原始 Markdown ↓</a>
    </nav>
  </header>
  <main class="docs-main" id="document-content">
    <p class="docs-kicker">KNOWLEDGE LIBRARY <span>／</span> V{VERSION}</p>
    <article class="docs-content">
{summary}      <div class="markdown-body">
{fragment}
      </div>
    </article>
  </main>
  <footer class="docs-footer content-wrap">
    <span>DAMA DATA PROJECT SKILLS · V{VERSION}</span>
    <a href="{home}">返回入口页 / Back to index ↑</a>
  </footer>
</body>
</html>
'''


def render_source(pandoc: str, source_path: Path, relative_source: PurePosixPath) -> str:
    original = source_path.read_text(encoding="utf-8")
    metadata, markdown = split_front_matter(original)
    title = document_title(markdown, relative_source)
    completed = subprocess.run(
        [pandoc, "--from=gfm", "--to=html5", "--wrap=none"],
        input=markdown,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"Pandoc failed for {relative_source}: {completed.stderr.strip()}")

    relative_output = relative_source.with_suffix(".html")
    fragment = rewrite_markdown_links(completed.stdout, relative_source, relative_output)
    language = "en" if relative_source.name.endswith(".en.md") else "zh-CN"
    return page_shell(title, language, fragment, metadata, relative_source, relative_output)


def render_all() -> int:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("Pandoc is required to generate the HTML mirror (pandoc was not found).")
    if not PACKAGE_ROOT.is_dir():
        raise RuntimeError(f"Release source directory not found: {PACKAGE_ROOT}")

    sources = sorted(PACKAGE_ROOT.rglob("*.md"))
    if not sources:
        raise RuntimeError(f"No Markdown source files found under {PACKAGE_ROOT}")

    for source_path in sources:
        relative_source = PurePosixPath(source_path.relative_to(PACKAGE_ROOT).as_posix())
        relative_output = relative_source.with_suffix(".html")
        output_path = DOCS_ROOT / Path(relative_output.as_posix())
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            render_source(pandoc, source_path, relative_source), encoding="utf-8", newline="\n"
        )
    print(f"Rendered {len(sources)} Markdown documents to {DOCS_ROOT.relative_to(ROOT)}.")
    return len(sources)


def main() -> int:
    try:
        render_all()
    except (OSError, ValueError, RuntimeError) as error:
        print(f"render_site_docs: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
