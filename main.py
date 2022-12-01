"""
main program to execute FastApi and the data
"""

from typing import Optional

from fastapi import FastAPI

import requests

import json

app = FastAPI()

file = "https://raw.githubusercontent.com/nicolerivera1/UdeA-papers-filtered/main/data/papers_filtered.json"


@app.get("/")
def read_item(doi_id: str = ""):
    """
    This allows you to filter by author name or orcid
    Make sure orcid includes the complete https direction
    """
    # Real time JSON file
    r = requests.get(file)
    db = r.json()

    # choose between name and orcid

    new_db = [d for d in db if d.get("doi")==doi_id]
    f = open("data/filtered.json", "w")
    json.dump(new_db, f)
    f.close()
    # with open(file) as json_file:
    #   db=json.load(json_file)

    if not doi_id:
        return db
    else:
        return new_db
