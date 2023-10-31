from bs4 import BeautifulSoup as bs
import time
import warnings
from typing import List
from helper.drivers import get_webdriver


def scrap_data(url) -> List[str]:
    """
    Scrapes product links from the Vestiaire Collective website.

    Returns:
    - List[str]: List of product URLs.
    """
    driver = get_webdriver()
    # Get the list of all products
    
    driver.get(url)
    SCROLL_PAUSE_TIME = 2  # Pause time between scrolls
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = bs(driver.page_source, "html.parser")

    headings_and_lists = soup.find_all('strong')
    data = {}

    for heading in headings_and_lists:
        heading_text = heading.get_text().strip()
        # Extract the content under the heading
        content = []
        next_element = heading.find_next()
        while next_element and next_element.name != 'strong':
            content.append(next_element.get_text().strip())
            next_element = next_element.find_next()
        # Store the content in the dictionary
        data[heading_text] = content

    print(data)
    return data["Responsibilities"]
