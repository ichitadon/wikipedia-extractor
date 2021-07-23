import gzip
import json
import sys
from typing import Any, List, Type

import pandas as pd

from wikipedia_extractor.util.color import Color


class Content:
    RESULT_COLUMNS = ["doc_id", "title", "redirects", "categories"]
    extract_result = Type[List[Any]]

    def __init__(self):
        pass

    def extract_from_json_line(self, line: bytes) -> tuple:
        json_line = json.loads(line)
        if "index" in json_line:
            return ("index", json_line["index"]["_id"])
        else:
            title = json_line["title"]
            redirect = [row["title"] for row in json_line["redirect"]]
            category = json_line["category"]
            return ("content", [title, redirect, category])

    def extract(self, path: str):
        i = 0
        result = []
        tmp_doc_id = 0
        with gzip.open(path) as f:
            for i, line in enumerate(f):
                extracted = self.extract_from_json_line(line)
                if extracted[0] == "index":
                    tmp_doc_id = extracted[1]
                else:
                    extracted[1].insert(0, tmp_doc_id)
                    result.append(extracted[1])
                if i % 200000 == 0:
                    print(int(i / 2))
        self.extract_result = result

    def to_csv(self, path: str):
        df_result = pd.DataFrame(self.extract_result, columns=self.RESULT_COLUMNS)
        df_result.to_csv(path, index=False)


if __name__ == "__main__":
    args = sys.argv
    content = Content()
    print(f"{Color.GREEN}start : content extraction{Color.RESET}")
    content.extract(args[1])
    print(f"{Color.GREEN}end   : content extraction{Color.RESET}")
    print(f"{Color.GREEN}start : content save{Color.RESET}")
    content.to_csv(args[2])
    print(f"{Color.GREEN}end   : content save{Color.RESET}")
