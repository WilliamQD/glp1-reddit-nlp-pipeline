# Presentation: GLP-1 Reddit NLP Pipeline

Project context: Yale course final project | BIS 550 | Public-safe presentation derivative

This presentation summary highlights the data/NLP pipeline without publishing raw Reddit text, labels, usernames, URLs, or model outputs.

## Slide 1: Motivation

GLP-1 medications are discussed across clinical, weight-loss, side-effect, and anti-diet communities. Reddit offers a view into lived experience and public discourse, but the text is noisy, sensitive, and privacy-constrained.

## Slide 2: Project Question

Can a data pipeline and NLP workflow separate medical support, neutral discussion, and toxic diet-culture framing in GLP-1 conversations?

## Slide 3: Data Workflow

| Stage | Purpose |
|---|---|
| Collection | Gather Reddit-style post/comment records |
| Cleaning | Remove HTML, Markdown, URLs, deleted markers, and encoding artifacts |
| Tokenization | Normalize domain terms and produce countable tokens |
| EDA | Summarize communities, dates, text lengths, and common terms |
| Labeling handoff | Prepare text for manual labels and supervised modeling |

## Slide 4: Corpus Snapshot

| Metric | Value |
|---|---:|
| Total records | 32,377 |
| Posts | 4,136 |
| Comments | 28,241 |
| Unique subreddits | 6 |

## Slide 5: Aggregate Figures

The public repo includes aggregate plots for post/comment mix, top subreddits, text-length distribution, and top terms. These visuals show the project shape without exposing row-level text.

## Slide 6: Labeling Design

Manual annotation used 700 random items plus 300 targeted items to improve coverage of a minority toxic-diet-culture class.

## Slide 7: Takeaway

The reusable value is the privacy-conscious NLP pipeline: turn messy social text into clean, aggregate, analysis-ready inputs while keeping raw text and labels out of public artifacts.
