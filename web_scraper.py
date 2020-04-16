import sys
import time
import os
import re
import json # pip install json
from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Scraper:

    def __init__(self,webpage, username, password):
  
        chrome_options = webdriver.ChromeOptions()
        self.webpage = webpage
        self.username = username
        self.password = password
        
        settings = {
            "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
        prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--kiosk-printing')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.minimize_window()
        self.driver.implicitly_wait(10)
 
    def scrape_page(self):

        print("Loging in....")
        
        login_page = self.webpage.split("/#/")[0]
          
        self.driver.get(login_page)
        
        self.driver.find_element_by_id("email-field").send_keys("%s" % self.username)
        password_field = self.driver.find_element_by_id("password-field").send_keys("%s" % self.password)
        self.driver.execute_script('document.getElementById("signin-form").submit()')
        
        time.sleep(5)
        if "signin" in self.driver.current_url:
            print("Login Failed!")
            print("Check Credentials")
            self.driver.quit()
            sys.exit(1)
            
        print("Scraping Webpage...")
        self.driver.get(self.webpage)
        time.sleep(10)
        seq = self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(seq[1])
        html_page = self.driver.page_source
        book_content = self.driver.find_element_by_id('epub-content')
        self.driver.switch_to.frame(book_content)
        book_source = self.driver.page_source
       
        self.source_to_web(book_source)
        
        self.driver.quit()

    def source_to_web(self, book_source):
        
        print("Converting data into usable form...")
        true_source = "https://jigsaw.vitalsource.com/books/%s/epub/OPS" % self.driver.current_url.split('/')[5]
        pattern_no_body = re.compile(r'<style type="text\/css" media="print">.*<\/style>')
        result = pattern_no_body.sub("", book_source)
        pattern_sub_images = re.compile(r'src="images\/')
        result = pattern_sub_images.sub('src="%s/images/' % true_source, result)
        pattern_sub_style = re.compile(r'<link rel="stylesheet" href="')
        result = pattern_sub_style.sub(r'<link rel="stylesheet" href="%s' % true_source, result)
        result = result.encode(encoding="ascii",errors="xmlcharrefreplace")
        f = open('.\web.html', 'wb')
        f.write(result)
        f.close()

        self.web_to_pdf()

    def web_to_pdf(self):

        print("Printing content to PDF...")
        current_dir = os.getcwd()
        self.driver.get("%s/web.html" % current_dir)
        self.driver.execute_script('window.print();')
        
        
if __name__ == "__main__":

    print("VitalSource Webscraper...")
    webpage = input("Please enter your desired webpage: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    run = Scraper(webpage, username, password)

    run.scrape_page()

    print("Success!")
    print("Your PDF should be located in your downloads folder.")
