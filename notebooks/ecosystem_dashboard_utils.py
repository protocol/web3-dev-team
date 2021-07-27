import requests
import json

# Dumps the JSON results of the provided ecosystem URL to disk
# by paging through until reaching the last page.
# The unpaginated_url is expecte to:
# 1. Be a .json url
# 2. End with a ? or a & so that the the paging queries can be appended.
def dump_api(unpaginated_url, output_path):
    page_size = 1000
    page = 1
    last_page_json_array = []
    cumulative_json_array = []

    while True:
        url = f"{unpaginated_url}per_page={page_size}&page={page}"
        print(f"Fetching {url}")
        r = requests.get(url)
        page_json_array = r.json()
        print(f"Fetched {len(page_json_array)} items")
        if last_page_json_array == page_json_array:
            break
        cumulative_json_array.extend(page_json_array)
        page = page + 1
        last_page_json_array = page_json_array

    with open(f"{output_path}", "w") as filecoin_repos_json_file:
        json.dump(cumulative_json_array, filecoin_repos_json_file, indent=2)