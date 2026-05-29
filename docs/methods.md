# Method Summary

## Research Question

How are GLP-1 medications discussed across Reddit communities, and can NLP methods separate medical support from neutral discussion and toxic diet-culture framing?

## Pipeline

1. Collect recent posts and comments from GLP-1-related subreddits.
2. Remove non-discussion/community records.
3. Build a unified text field from post titles, bodies, and comments.
4. Clean HTML, Markdown, URLs, encoding artifacts, deleted markers, and unstable whitespace.
5. Normalize text and tokenize into analysis-ready terms.
6. Run EDA over post/comment mix, subreddits, dates, lengths, and common terms.
7. Hand off cleaned text for topic exploration, manual labeling, and supervised classification.

## Public Version

This repository keeps the reusable structure and code patterns but excludes all row-level data. The tests use synthetic examples created only for code validation.
