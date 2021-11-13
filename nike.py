import json
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service('road to chrome driver')

url = 'https://www.nike.com/ru/w/mens-soccer-shoes-1gdj0znik1zy7ok'
driver = webdriver.Chrome(service=service)

'''At first
1.We should create a function that capture HTML website.
2.We use Selenium to scroll down our site.
3.After scrolling to the end,we save it in HTML format.
4.Create a func pars.
5.We use wonderful library which name is BS4.
6.We read our HTML file that we saved before.
7.Then we find our products and information about them.
8.And last part we have to save them in JSON
9.READY!'''
def get_nike():
	try:
		driver.get(url=url)
		time.sleep(1)
		driver.find_element(By.CLASS_NAME,'hf-modal-btn-close').click()
		time.sleep(5)
		driver.execute_script('window.scrollTo(0,40000)')
		time.sleep(10)
		driver.execute_script('window.scrollTo(0,40000)')
		time.sleep(10)
		driver.execute_script('window.scrollTo(0,40000)')
		with open('nike.html','w',encoding='utf-8') as f:
			f.write(driver.page_source)
			time.sleep(5)
	except Exception as exception:
		print(exception)
	finally:
		driver.close()
		driver.quit()
def parse(path):
	with open(path,encoding='utf-8') as f:
		path = f.read()
	s = BeautifulSoup(path,'lxml')
	itemu = s.find_all('a',class_='product-card__link-overlay')
	Result = []
	for item in itemu:
		newurl = item.get('href')
		title = item.text.strip()
		Result.append(
			{
			"Name" : title,
			"Url" : newurl
			}
		)

	with open("nikeres.json", "w",newline='',encoding='utf-8') as f:
		json.dump(Result, f, indent=3, ensure_ascii=False)
def main():
	print(parse(path='ROAD TO HTML FILE THAT WE SAVED'))
if __name__ == '__main__':
	main()