# SeleniumHotelPriceChecker

## Overview
This repository contains a Selenium-based bot for checking hotel prices on Booking.com.

## Table of Contents
- [Files and Their Roles](#files-and-their-roles)
- [Usage](#usage)

## Files and Their Roles

### `booking` Package
- [`__init__.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/booking/__init__.py): Initializes the `booking` package.
- [`booking.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/booking/booking.py): Contains the main `Booking` class for interacting with Booking.com.
- [`booking_filtration.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/booking/booking_filtration.py): Provides the `BookingFiltration` class for applying filters on search results.
- [`booking_report.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/booking/booking_report.py): Includes the `BookingReport` class for parsing and reporting hotel deals.
- [`constants.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/booking/constants.py): Stores constant values like the base URL for Booking.com.

### Main Script
- [`run.py`](https://github.com/mahir24/SeleniumHotelPriceChecker/blob/master/run.py): The main script that runs the bot.

## Usage
Run the `run.py` script to start the bot. Follow the prompts to enter your search criteria and view the hotel deals.

