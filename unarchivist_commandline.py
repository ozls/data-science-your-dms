#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# FUNCTION
# =============================================================================

def ziptocsv(zip_path, csv_path):

    from zipfile import ZipFile
    import pandas as pd
    import json

    d = pd.DataFrame([])

    with ZipFile(zip_path) as tzip:

        fileNames = tzip.namelist()
        fileNames = [fn for fn in fileNames if fn.endswith('json')]

        for fileName in fileNames:

            with tzip.open(fileName) as f:
                dic = json.load(f)
                df = pd.DataFrame(dic["messages"])
                df["title"] = dic["title"]
                df["type"] = dic["thread_type"]
                d = pd.concat([d, df])

    d = d.loc[:,("title", "type", "sender_name", "content", "timestamp_ms")].dropna(0)
    for c in ["sender_name", "content", "title"]:
        d[c] = [str(i).encode("latin1").decode("utf8") for i in d[c]]

    d.to_csv(csv_path, sep = ";", index = False)

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    import sys

    zip_path = sys.argv[1]
    csv_path = sys.argv[2]

    ziptocsv(zip_path, csv_path)