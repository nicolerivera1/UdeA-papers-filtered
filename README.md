# UdeA-papers-filtered
Implementing FastApi to show OpenAlex papers filtered by institution and concepts


## Fast API
See install options and usage at: https://fastapi.tiangolo.com/
```
$ uvicorn main:app --reload --host
```
and copy and paste the url in your browser, e.g:

http://127.0.0.1:8000/

You can now filter with the JSON keys into the url, e.g:

http://127.0.0.1:8000/?doi_id=https://doi.org/10.1371/journal.pcbi.1009704


## Frontend
```
$ python3 -m http.server 8001
```
