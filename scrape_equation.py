from scrape_cse import get_page_text
import requests, re

def get_equation(formula):
    url = 'http://www.endmemo.com/chem/ajax/balancer_ajax.php?q=' + formula
    results = get_page_text(url)
    regex = re.compile(r'(.* = (\d)?' + formula + r')\n')
    try:
        res = regex.search(results).group(1)
        print(res)
    except:
        res = 'N/A'
    return res