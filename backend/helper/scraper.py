from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helper.drivers import get_webdriver
import json



def scrap_data(url):

    driver = get_webdriver()
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    # Extract data directly using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    headings_and_lists = soup.find_all('strong')
    text = ''
    for heading in headings_and_lists:
        # Use BeautifulSoup to find the next siblings
        next_elements = heading.find_all_next()

        for element in next_elements:
            if element.name == 'strong':
                break
            text += element.get_text().strip()

    driver.quit()
    return text
