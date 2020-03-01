import requests


key = '8lKPBXKVsRdsxFn9u0U0w'
secret = 'fkwQ0OK4E80EiOmiwWnGcsAv1S3F4ylOVn0MHjlM'

import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "8lKPBXKVsRdsxFn9u0U0w", "isbns": "9781632168146"})
print(res.json())
