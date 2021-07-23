import json

import pytest

from wikipedia_extractor.extract.content import Content


class TestContent:
    def test_extract_from_json_line_success_index(self):
        testee = {"index": {"_type": "page", "_id": "37524"}}

        actual = Content.extract_from_json_line(self, json.dumps(testee))
        assert actual[0] == "index"
        assert actual[1] == "37524"

    def test_extract_from_json_line_success_content(self):
        testee = {
            "template": [],
            "content_model": "wikitext",
            "opening_text": "hoge",
            "wiki": "jawiki",
            "auxiliary_text": ["hoge"],
            "language": "ja",
            "title": "title",
            "text": "hoge",
            "defaultsort": "hoge",
            "timestamp": "2019-11-11T11:29:10Z",
            "redirect": [
                {"namespace": 0, "title": "redirect1"},
                {"namespace": 0, "title": "redirect2"},
                {"namespace": 0, "title": "redirect3"},
            ],
            "wikibase_item": "Q807853",
            "heading": ["heading1", "heading2"],
            "source_text": "hoge",
            "version_type": "external",
            "coordinates": [],
            "version": 74969344,
            "external_link": [],
            "namespace_text": "",
            "namespace": 0,
            "text_bytes": 2420,
            "incoming_links": 8,
            "category": ["category1", "category2", "category3"],
            "outgoing_link": ["outgoing_link1", "outgoing_link2"],
            "popularity_score": 8.098065362358829e-07,
            "create_timestamp": "2003-12-20T06:32:04Z",
        }

        actual = Content.extract_from_json_line(self, json.dumps(testee))
        assert actual[0] == "content"
        assert actual[1] == [
            "title",
            ["redirect1", "redirect2", "redirect3"],
            ["category1", "category2", "category3"],
        ]
