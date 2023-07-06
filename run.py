from booking.booking import Booking  #import Booking class

# context managers
with Booking() as bot:
    bot.land_first_page()
    bot.close_popup()
    bot.select_place_to_go(input("Where do you want to go?"))
    bot.select_dates(check_in_date='2023-07-16',
                    check_out_date='2023-07-23')  #dynamic vairables not working??
    bot.select_adults(int(input("How many people will go?")))
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() # refresh to let bot grab data properly
    bot.report_result()

