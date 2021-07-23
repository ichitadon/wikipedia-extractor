import json

import pytest

from wikipedia_extractor.extract.general import General


class TestGeneral:
    def test_extract_from_json_line_success_index(self):
        testee = {"index": {"_type": "page", "_id": "506852"}}

        actual = General.extract_from_json_line(self, json.dumps(testee))
        assert actual[0] == "index"
        assert actual[1] == "506852"

    def test_extract_from_json_line_success_category(self):
        testee = {
            "template": [],
            "redirect": [
                {"namespace": 0, "title": "redirect1"},
                {"namespace": 0, "title": "redirect2"},
                {"namespace": 0, "title": "redirect3"},
            ],
            "wikibase_item": "Q8548191",
            "content_model": "wikitext",
            "heading": [],
            "source_text": "hoge",
            "version_type": "external",
            "opening_text": "hoge",
            "wiki": "jawiki",
            "coordinates": [],
            "auxiliary_text": ["hoge"],
            "language": "ja",
            "title": "title",
            "version": 54235107,
            "external_link": ["hoge"],
            "namespace_text": "Category",
            "namespace": 14,
            "text_bytes": 297,
            "incoming_links": 360,
            "text": "hoge",
            "category": ["category1", "category2", "category3"],
            "defaultsort": "hoge",
            "outgoing_link": ["outgoing_link1", "outgoing_link2"],
            "timestamp": "2015-01-26T07:29:35Z",
            "create_timestamp": "2006-04-14T00:37:47Z",
        }

        actual = General.extract_from_json_line(self, json.dumps(testee))
        assert actual[0] == "category"
        assert actual[1] == [
            "title",
            ["redirect1", "redirect2", "redirect3"],
            ["category1", "category2", "category3"],
        ]
