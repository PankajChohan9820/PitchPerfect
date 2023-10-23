from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import warnings


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