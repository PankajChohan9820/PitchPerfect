from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import warnings
from bs4 import BeautifulSoup as bs
import time
import warnings
from typing import List
from helper.drivers import get_webdriver
from parsel import Selector

# Ignore warnings
warnings.filterwarnings("ignore")


def get_webdriver() -> webdriver.Chrome:
    """
    Initialize and configure a Chrome WebDriver instance.

    Returns:
    - webdriver.Chrome: The configured Chrome WebDriver instance.
    """

    try:
        ua = UserAgent()
        # ua.update()
        # ua.random
        user_agent = ua.random
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument('window-size=1200x600')
        options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver

    except Exception as e:
        print("Error in WebDriver", str(e))
        return None

driver = get_webdriver()
    # Get the list of all products
# url = 'https://www.linkedin.com/jobs/search/?currentJobId=3712601062'
url = 'https://www.linkedin.com/jobs/search/?currentJobId=3745590469'
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
desired_headings = ["Responsibilities", "Preferred Qualifications"]

data = {}

for heading in headings_and_lists:
    heading_text = heading.get_text().strip()
    
    # Check if the current heading is one of the desired headings
    # if heading_text in desired_headings:
        # Extract the content under the heading
    content = []
    next_element = heading.find_next()
    while next_element and next_element.name != 'strong':
        content.append(next_element.get_text().strip())
        next_element = next_element.find_next()
    # Store the content in the dictionary
    data[heading_text] = content

print(data)