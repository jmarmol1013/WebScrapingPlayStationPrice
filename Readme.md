# PlayStation Price Scraper

This Python application scrapes the price of the PlayStation from the Amazon website every day. If the price is lower than $700, it sends you an email notification. It also creates and edits a CSV file to store the price information.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `smtplib` library
- `time` library
- `datetime` library
- `csv` library
- `json` library

## Installation

1. Clone the repository
2. Change to the project directory
3. Install the required libraries

## Configuration

1. Create `config.json` file.

2. Create the following variable:
- `email`: The address where are you going to send and recieved the email information
- `password`: The password for the email to be sent


The application will scrape the price of the PlayStation from Amazon, send an email notification if it's lower than $700, and create/edit a CSV file to store the price information.

## CSV File

The application creates a CSV file to store the price information. The CSV file will be located at the same path of the file as `PlayStationPrices.csv`. Each row in the CSV file represents a recorded price and includes the following columns:

- Title: Title of the product.
- Date: The date when the price was recorded (format: YYYY-MM-DD).
- Price: The price of the PlayStation.

You can open and analyze the CSV file using spreadsheet software like Microsoft Excel or Google Sheets.

## Notes

- The application uses web scraping techniques to extract the price information from the Amazon website. Please ensure that you comply with Amazon's terms of service and do not overload their servers with excessive requests.
- Make sure to use valid email credentials in the configuration file to send email notifications successfully.
- The application must be running to save the information and send the email, it will do it every 24 hours.
