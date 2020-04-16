# Vitalsource PDF Converter

### Introduction
This python script converts Online Vitalsource Ebooks into PDF format. This is achieved by scraping the desired webpage for the content HTML and creating an offline replica while removing the specific tags that prevent the user from normally printing the page. With these tags removed the page is printed to a PDF format for universal use. Due to the fact that only one chapter is displayed per webpage this proccess will need to be repeated for each chapter you wish to download.

### Prerequisites 
I have inclueded a compilied version of my python code in this repository. If you do not wish to make changes to this code or do not want to worry about dependencies please use the executable. NOTE: You will still need a Chrome version 81.x installed. If you decide to run the python code you will need to install a few selective python packages. This script utilizes selenium with chromedriver. The current tested chromedriver is for Chrome version 81. If you are using an older version you can download and attempt to replace chromedriver.exe with the older chromedriver. NOTE: This has not been tested. This tool was specifically designed for a Windows environment so some changes will need to be made if you are using an alternative environment. Python dependencies can be installed  via:
```
pip install json
pip install selenium
```
### Usage
Navigate to the desired chapter of the book in your vitalsource account and copy the webpage associated with it.
There are two way to use this program. If you wish to avoid hassle I reccomend using the executable (web_scraper.exe). For this method just double click the executable to run it and the prompts will continue as shown below.

If you are using the python source code it can be ran by the following: `python web_scraper.py` The prompts will start as shown below. 

```
VitalSource Webscraper...
Please enter your desired webpage: <Vitalsource Webpage>
Please enter your username: <Vitalsource username>
Please enter your password: <Vitalsource password>
Loging in....
Scraping Webpage...
Converting data into usable form...
Printing content to PDF...
Success!
Your PDF should be located in your downloads folder.
```

