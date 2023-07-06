# effective-octo-broccoli (New York Times Article Crawler)
thoughtful automation challenge

This README provides an overview of the Python application for crawling the New York Times website and extracting article data. The application uses Selenium and a WebDriver to interact with the website and retrieve information such as the title, description, date, picture, and picture URL. The application also provides filters for data based on month, specific words, and NYT-sections.

## Prerequisites

Before running the application, ensure you have the following:

- Python installed on your system (version 3.6 or higher)
- WebDriver for browser Google Chrome (ChromeDriver)

## Install 

To install the required packages and set some default variables, run the following command:

> make start


## Usage

To run the application, follow these steps:

- Ensure that the filters are setted in .env file

- Open a terminal or command prompt.

> make run

Note if you delete the tmp folder, you need to restore them to run the aplication using

> make folders

The application will launch the New York Times website using Chrome and start crawling based.

## Getting the data

All the info are stored in xlsx file in tmp diretory with the name setted on .env