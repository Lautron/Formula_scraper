# scrape_cse.py - Use google api to scrape google Custom Search Engine (CSE), and return first result
from api_alternative import get_url_with_selenium
from secrets import cse_api_key
import requests, json

search_eng_id = "partner-pub-3423573329131731:8004450472"

def get_page_text(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def get_link_from_json(json_str):
    json_dict = json.loads(json_str)
    first_item = json_dict.get('items', [None])[0]
    if first_item:
        return first_item['link']

def get_formula_link(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={cse_api_key}&cx={search_eng_id}&q={query}"
    try:
        json_response = get_page_text(url)
        link = get_link_from_json(json_response)
        if link:
            return link
        else:
            return f"N/A {query} couldn't be found"
    except:
        return get_url_with_selenium(query)

if __name__ == "__main__":
    print(get_formula_link('H2O'))


