"""Record normalization for post/comment style exports."""

from __future__ import annotations

from typing import Any

from .text_cleaning import clean_text, tokenize


def _first_present(record: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = record.get(key)
        if value is not None:
            return str(value)
    return ""


def normalize_record(record: dict[str, Any]) -> dict[str, Any] | None:
    """Convert a raw post/comment record into a public-safe normalized shape.

    The returned object intentionally excludes author identifiers and URLs.
    """

    data_type = _first_present(record, "dataType", "data_type").lower()
    if data_type not in {"post", "comment"}:
        return None

    title = _first_present(record, "title").strip()
    body = _first_present(record, "body", "text").strip()
    raw_text = f"{title}\n{body}".strip() if data_type == "post" else body
    cleaned = clean_text(raw_text)
    tokens = tokenize(cleaned)
    if not tokens:
        return None

    subreddit = _first_present(record, "parsedCommunityName", "subreddit", "communityName")
    subreddit = subreddit.replace("r/", "").strip()

    return {
        "data_type": data_type,
        "subreddit": subreddit or "Unknown",
        "created_at": _first_present(record, "createdAt", "created_at"),
        "clean_text": cleaned,
        "tokens": tokens,
        "token_count": len(tokens),
        "upvotes": int(record.get("upVotes") or record.get("upvotes") or 0),
    }
