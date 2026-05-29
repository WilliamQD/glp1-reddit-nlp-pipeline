"""Text cleaning helpers used by the public no-data pipeline."""

from __future__ import annotations

import html
import re
import unicodedata

URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_PREFIX_RE = re.compile(r"^\s{0,3}(?:>+|[*+-]|\d+\.)\s*")
TOKEN_CLEAN_RE = re.compile(r"[^a-z0-9]+")
WHITESPACE_RE = re.compile(r"\s+")
EMPTY_MARKERS = {"", "[deleted]", "[removed]", "deleted", "removed"}
DEFAULT_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "for",
    "from",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "with",
}


def strip_markdown(text: str) -> str:
    """Remove common Markdown link and quote/list markup."""

    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    lines = [MARKDOWN_PREFIX_RE.sub("", line.strip()) for line in text.splitlines()]
    return "\n".join(lines)


def clean_text(text: str) -> str:
    """Normalize raw Reddit text while preserving readable content."""

    if not text:
        return ""

    text = html.unescape(text)
    text = strip_markdown(text)
    text = URL_RE.sub(" ", text)
    text = unicodedata.normalize("NFKC", text)
    text = WHITESPACE_RE.sub(" ", text).strip()
    return "" if text.lower() in EMPTY_MARKERS else text


def tokenize(text: str, stopwords: set[str] | None = None) -> list[str]:
    """Tokenize cleaned text for lightweight public tests and EDA examples."""

    stopwords = DEFAULT_STOPWORDS if stopwords is None else stopwords
    normalized = text.lower().replace("glp-1", "glp1")
    tokens: list[str] = []
    for raw_token in normalized.split():
        token = TOKEN_CLEAN_RE.sub("", raw_token)
        if not token or token in stopwords or token in EMPTY_MARKERS or token.isdigit():
            continue
        tokens.append(token)
    return tokens
