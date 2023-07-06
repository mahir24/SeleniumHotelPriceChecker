# This file will include a class with instance methods that will be responsible to interact
# with the website after results
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver # will receive original driver from Booking class

    # *star_values is an arbitrary argument where you can add multiple arguments
    # in this case this will check multiple filters
    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.ID, "filter_group_class_:R14q:")
        # This gets all the child elements of the entire star filtration box
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        # Iterate over all the arguments(filters)
        for star_value in star_values:
            # Iterate over all the star filtration elements to find the star values
            for star_element in star_child_elements:
                # inner HTML --> <h1>5 Stars<h1> --> will receive 5 Stars
                # strip() cleans all white spaces
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price(self):
        open_sort = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        open_sort.click()

        element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        element.click()

