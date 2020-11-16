from bs4 import BeautifulSoup
import requests

def get_page_data(html, mode):
    soup = BeautifulSoup(html, 'lxml')
    formula = soup.find('h1').text.split(' / ')[0]
    result = {'formula': formula}
    if mode in {'e', 'all'}:
        p_list = soup.select('div[id=cf] > p')
        nomenclature = {
            'sist' : p_list[1].text if p_list else 'N/A',
            'stock' : p_list[2].text if p_list else 'N/A',
            'trad' : p_list[3].text if p_list else 'N/A'
        }
        result.update(nomenclature)
    
    return result


if __name__ == "__main__":
    get_page_data(requests.get('https://www.formulacionquimica.com/H2O/').text, '')