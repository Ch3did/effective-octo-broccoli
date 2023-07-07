# effective-octo-broccoli (New York Times Article Crawler)
thoughtful automation challenge

This README provides an overview of the Python application for crawling the New York Times website and extracting article data. The application uses Selenium and a WebDriver to interact with the website and retrieve information such as the title, description, date, picture, and picture URL. The application also provides filters for data based on month, specific words, and NYT-sections.

## Prerequisites

Before running the application, ensure you have the following:

- Python installed on your system (version 3.6 or higher)
- WebDriver for browser Google Chrome (ChromeDriver)
- Virtual environment installed and activated (To avoid polluting your environment).

## Install 

After the ponits above, run the following commands to configure the folders, aplication variables and install all python packages neede to run the aplication:

> make start


## Usage

The application offers various filters to guide the scraping process. The main filter is the "phrase," which serves as the basis for data extraction. Additionally, you can adjust the number of months to search, determining how far back the application retrieves data. Finally, the section filter defines the type of news within the New York Times

To make it easier to use the application, default values are set for these variables in the initial configuration:

- Phrase: Brazil
- Section: World
- Months: 1

If you want to configure any of these variables, Effective-Octo-Broccoli provides a command-line interface (CLI) to adjust them. Simply use the command "make" followed by the name of the target variable.

> make phrase
> make months
> make section


finally, to run the application open a terminal or command prompt and hit:

> make run

The application will launch the New York Times website with Chrome and uses the phrase to search news. After that, to set filter on the page, start scraping by the newest on the selected section.


Note if in some point you delete the tmp folder, you need to restore them to run the aplication using

> make folders

## Stored data

All the info are stored in the tmp folder where you can find an .xlsx file with the name setted on env and a pictures folder, where are saved the image of the headline