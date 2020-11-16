from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_url_with_selenium(query):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options, service_log_path='NUL')
    query = query.replace(' ', '%20')
    query_url = 'https://www.formulacionquimica.com/buscador/?q=' + query
    browser.get(query_url)
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gs-title"))
        )
    except Exception as e:
        print(e)
        print('Element not found...')
        return

    final_url = browser.find_element_by_class_name("gs-title")\
                        .find_element_by_tag_name('a')\
                        .get_attribute('href')
    browser.close()
    return final_url