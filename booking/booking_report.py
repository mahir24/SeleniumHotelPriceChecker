# File will include methods that will parse the specific data from each deal box
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes() # gives control over all boxes

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_deal_info(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pull Each Hotel Name
            hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
                                                ).get_attribute('innerHTML').strip()
            collection.append(
                [hotel_name, hotel_price]
            )

        return collection
