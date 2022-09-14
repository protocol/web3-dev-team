import requests
import json

# Dumps the JSON results of the provided ecosystem URL to disk
# by paging through until reaching the last page.
# The unpaginated_url is expecte to:
# 1. Be a .json url
# 2. End with a ? or a & so that the the paging queries can be appended.
# If you are getting timeouts, you can adust the page_size.
# If you want to do a transform on the data before writing it disk, you can apply a filter.
# A common filter is to to remove the "payload" field from the "/events" API result.
def dump_api(unpaginated_url, output_path, filter=lambda x: x, page_size=1000):
    page = 1
    last_page_json_array_filtered = []
    cumulative_json_array = []

    while True:
        url = f"{unpaginated_url}per_page={page_size}&page={page}"
        print(f"Fetching {url}")
        r = requests.get(url)
        page_json_array = r.json()
        fetched_page_size = len(page_json_array)
        print(f"Fetched {fetched_page_size} items")
        page_json_array_filtered = []
        for obj in page_json_array:
            page_json_array_filtered.append(filter(obj))
        if page_size != fetched_page_size:
            cumulative_json_array.extend(page_json_array_filtered)
            break
        if last_page_json_array_filtered == page_json_array_filtered: # the array comparison method hasn't always been reliable so it's our second level check
            break
        cumulative_json_array.extend(page_json_array_filtered)
        page = page + 1
        last_page_json_array_filtered = page_json_array_filtered

    with open(f"{output_path}", "w") as filecoin_repos_json_file:
        json.dump(cumulative_json_array, filecoin_repos_json_file, indent=2)