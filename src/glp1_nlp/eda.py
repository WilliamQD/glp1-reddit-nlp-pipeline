"""Aggregate-only EDA helpers."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping


def summarize_records(records: Iterable[Mapping[str, object]]) -> dict[str, object]:
    """Return aggregate counts without exposing row-level text."""

    rows = list(records)
    type_counts = Counter(str(row["data_type"]) for row in rows)
    subreddit_counts = Counter(str(row["subreddit"]) for row in rows)
    token_counts = [int(row["token_count"]) for row in rows]
    token_counter: Counter[str] = Counter()
    for row in rows:
        token_counter.update(row.get("tokens", []))

    average_token_count = sum(token_counts) / len(token_counts) if token_counts else 0.0
    return {
        "total_rows": len(rows),
        "type_counts": dict(type_counts),
        "unique_subreddits": len(subreddit_counts),
        "top_subreddits": subreddit_counts.most_common(10),
        "average_token_count": round(average_token_count, 2),
        "top_terms": token_counter.most_common(10),
    }
