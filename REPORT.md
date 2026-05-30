# Report: GLP-1 Reddit NLP Pipeline

Project context: Yale course final project | BIS 550 | Public-safe report derivative

This report summarizes the group project in a public-safe format. It preserves the project framing, pipeline design, aggregate results, and contribution context while omitting raw Reddit text, usernames, URLs, labels, row-level records, model predictions, and private working files.

## Abstract

GLP-1 medications have become part of mainstream online conversation around diabetes care, weight loss, side effects, body image, and diet culture. This project studied Reddit discourse across medication-specific and anti-diet communities using a data pipeline that collected, cleaned, explored, labeled, and prepared text for downstream NLP modeling.

The public repo focuses on the data engineering and NLP preprocessing layer: record normalization, text cleaning, tokenization, aggregate exploratory analysis, and labeling handoff.

## Research Question

How are GLP-1 medications discussed across Reddit communities, and can NLP methods separate medical support from neutral discussion and toxic diet-culture framing?

## Data Pipeline

The pipeline processed Reddit-style post and comment records through the following stages:

1. collect recent posts and comments from GLP-1-related communities,
2. remove non-discussion records,
3. combine post titles, bodies, and comments into a unified text field,
4. clean HTML, Markdown, URLs, encoding artifacts, deleted markers, and unstable whitespace,
5. normalize text and tokenize domain-relevant terms,
6. produce aggregate EDA summaries,
7. hand off cleaned text for topic exploration, manual labeling, and supervised classification.

## Aggregate Results

The cleaned private project corpus contained:

| Metric | Value |
|---|---:|
| Total records | 32,377 |
| Posts | 4,136 |
| Comments | 28,241 |
| Unique subreddits | 6 |
| Average token count | 26.06 |
| Median token count | 16.0 |

The most frequent subreddit in the cleaned corpus was `Zepbound`. Common high-frequency terms included `weight`, `week`, `like`, `day`, and `month`.

## Labeling Strategy

Manual labeling used a two-stage design:

- 700 randomly sampled items for broad discourse coverage,
- 300 targeted items to improve coverage of the minority toxic-diet-culture class.

The final labeled set supported downstream topic modeling and supervised classification. The public repository does not include labeled rows or row-level text.

## Public Figures

The repository includes aggregate-only figures:

- posts versus comments,
- top subreddits,
- text-length distribution,
- top terms.

These figures are safe to publish because they do not expose usernames, post text, URLs, or individual records.

## Contribution

William Zhang contributed to project framing, data collection workflow, NLP preprocessing, exploratory data analysis, code implementation for preprocessing/EDA, and report/presentation sections related to the data pipeline.

Other group members contributed topic modeling, manual labeling, future-work framing, and classification modeling.

## Public-Safe Scope

This derivative excludes raw Reddit exports, cleaned datasets, labeled examples, post/comment text, usernames, URLs, model predictions, and private group working files.
