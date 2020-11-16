from scrape_cse import get_formula_link
from scrape_page import get_page_data
from scrape_equation import get_equation
from scrape_cse import get_page_text
from queries import queries
import csv, time, os

def write_csv(data_dict, writer):
    res_dict = {k.encode().decode('latin1'): v for k, v in data_dict.items()}
    columns = ['formula', 'sist', 'stock', 'trad','equation']
    dict_keys = res_dict.keys()
    res = [res_dict[item] for item in columns if item in dict_keys]
    writer.writerow(res)

def main():
    writer = csv.writer(
        open('results.csv', 'a', encoding='latin1')
    )
    start_time = round(time.time())
    scrape_count = 0

    if os.path.getsize(f'results.csv') == 0:
        writer.writerow(['Formula', 'Stock', 'Sistemática', 'Tradicional', 'Ecuación'])

    for item in queries:
        query_list = item[1] if isinstance(item[1], list) else item[1].split(', ')
        mode = item[0]
        for query in query_list:
            print(f'Scraping {query}...')
            scrape_count += 1
            link = get_formula_link(query)
            if 'N/A' not in link:
                html = get_page_text(link)
                data = get_page_data(html, mode)
                if mode in {'e', 'all'}:
                    equation = get_equation(data['formula'])
                    data.update({'equation': equation})
            else:
                data = {'formula': f"N/A {query} couldn't be found"}
            write_csv(data, writer)
        writer.writerow([])

    seconds = round(time.time()) - start_time
    print(f"~~~ {seconds} seconds ~~~\n~~~ {seconds // scrape_count} seconds per search ~~~")


if __name__ == "__main__":
    main()

    