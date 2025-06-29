from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def extract_chapter_titles(url):
    """
    Extracts chapter titles from a novel's webpage using Selenium for dynamic content.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of chapter titles, or an empty list if an error occurs.
    """
    driver = None  # Initialize driver to None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage') # Overcome limited resource problems

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Wait for the "Chapter List" tab link to be clickable and click it
        chapter_tab_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'tab-chapters-title'))
        )
        chapter_tab_link.click()

        # Wait for the chapter list container to be present
        chapter_list_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'tab-chapters'))
        )

        # Implement mechanism to handle pagination/load more if they exist.
        # For now, assuming all chapters are loaded after clicking the tab.
        # If there were "load more" buttons, we would click them here until no more are available.
        # Example (conceptual):
        # while True:
        #     try:
        #         load_more_button = WebDriverWait(driver, 5).until(
        #             EC.element_to_be_clickable((By.ID, 'load-more-chapters-button'))
        #         )
        #         load_more_button.click()
        #         time.sleep(2) # Give some time for content to load
        #     except TimeoutException:
        #         break # No more load more button

        # Find all chapter links within the container
        chapter_links = chapter_list_container.find_elements(By.TAG_NAME, 'a')
        
        titles = [link.text.strip() for link in chapter_links if link.text.strip()]
        return titles

    except TimeoutException as e:
        print(f"Error: Timeout while waiting for element: {e}")
        return []
    except WebDriverException as e:
        print(f"Error: WebDriver encountered an issue: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    finally:
        if driver:
            driver.quit()