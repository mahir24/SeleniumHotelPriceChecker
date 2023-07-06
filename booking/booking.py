import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable
# constructor method
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Program Files (x86)\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()  # using super to instantiate an instance of the webdriver.Chrome class
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        input("Press any key to exit...")

        self.quit()
        # # if teardown is true then quit the browser
        # if self.teardown:
        #     self.quit()  # shuts down chrome when done

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        try:
            close = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
            close.click()
        except:
            print("No popup... Skipping")

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()  # clean existing text
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, "li.a80e7dc237:first-child")
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[role="gridcell"] span[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[role="gridcell"] span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()

        while True:
            decrease_adult_element = self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')
            decrease_adult_element.click()

            # if value of adults reaches 1 exit loop
            adult_value_element = self.find_element(By.ID, "group_adults")
            adult_value = adult_value_element.get_attribute('value') # receives key name and returns value of that attribute

            if int(adult_value) == 1:
                break

        increase_button_element = self.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')

        for i in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(self) # instantiate booking filtration class
        filtration.apply_star_rating(3)

        filtration.sort_price()

    def report_result(self):
        hotel_boxes = self.find_element(By.ID, "search_results_table")
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            ["Hotel Name", "Hotel Price"] # names of columns
        )
        table.add_rows(report.pull_deal_info())
        print(table)
