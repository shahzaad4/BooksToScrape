# Bookstoscrape

## Overview
Bookstoscrape is a Python-based web scraping project that extracts data from the [Books to Scrape](http://books.toscrape.com/) website and stores the information in a CSV file. This project uses BeautifulSoup and Selenium to navigate the website, scrape book details, and save them for analysis or further use.

## Features
- Scrapes book details including title, price, availability, rating, and more.
- Utilizes BeautifulSoup for parsing HTML content.
- Employs Selenium for handling dynamic content and browser automation.
- Saves scraped data into a structured CSV file.

## Requirements
- Python 3.x
- BeautifulSoup4
- Selenium
- pandas
- ChromeDriver (or another web driver compatible with Selenium)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bookstoscrape.git
    cd bookstoscrape
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download and set up [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (or another web driver):
    - Ensure the driver is in your system PATH or specify the path in the script.

## Usage
1. Run the scraper:
    ```sh
    python scrape_books.py
    ```

2. The script will navigate through the Books to Scrape website, scrape book details, and save them into a `books.csv` file in the project directory.

## File Structure
- `scrape_books.py`: Main script to run the web scraper.
- `requirements.txt`: List of required Python packages.
- `books.csv`: Output file containing the scraped data.

## Example
Example of a row in the `books.csv` file:
```csv
Title, Price, Availability, Rating
"A Light in the Attic", "£51.77", "In stock", "Three"
