import unittest

from glp1_nlp import clean_text, normalize_record, summarize_records, tokenize


class Glp1NlpTests(unittest.TestCase):
    def test_clean_text_removes_urls_and_markdown(self):
        text = "> [Helpful link](https://example.com) about GLP-1 &amp; symptoms"
        self.assertEqual(clean_text(text), "Helpful link about GLP-1 & symptoms")

    def test_tokenize_normalizes_glp1(self):
        self.assertEqual(tokenize("GLP-1 medication and weekly progress"), ["glp1", "medication", "weekly", "progress"])

    def test_normalize_record_omits_author_fields(self):
        record = {
            "dataType": "post",
            "title": "Synthetic update",
            "body": "GLP-1 helped my weekly routine.",
            "parsedCommunityName": "ExampleSubreddit",
            "author": "should_not_be_returned",
            "url": "https://example.com/private",
            "upVotes": 3,
        }
        normalized = normalize_record(record)
        self.assertIsNotNone(normalized)
        self.assertNotIn("author", normalized)
        self.assertNotIn("url", normalized)
        self.assertEqual(normalized["subreddit"], "ExampleSubreddit")

    def test_summarize_records_returns_aggregate_counts(self):
        records = [
            normalize_record({"dataType": "post", "title": "A", "body": "GLP-1 progress", "subreddit": "A"}),
            normalize_record({"dataType": "comment", "body": "Medication support thread", "subreddit": "B"}),
        ]
        summary = summarize_records([record for record in records if record is not None])
        self.assertEqual(summary["total_rows"], 2)
        self.assertEqual(summary["type_counts"]["post"], 1)
        self.assertEqual(summary["unique_subreddits"], 2)


if __name__ == "__main__":
    unittest.main()
