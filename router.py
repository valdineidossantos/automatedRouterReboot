from selenium 								 import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by 			 import By
from selenium.webdriver.common.keys 		 import Keys
from selenium.webdriver.support 			 import expected_conditions as EC
from selenium.webdriver.support.ui 			 import WebDriverWait


class RouterBase(object):
	def __init__(self):
		self.__chromedriverPath="/mnt/c/WebDriver/chromedriver.exe"		
		self.browser =  webdriver.Chrome(self.__chromedriverPath)
		self.browser.maximize_window()
	
	def go(self):
		raise "Not implemented method"
		pass

	def getByClass(self, _class, timeout):
		wait = WebDriverWait(self.browser, timeout)
		element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, _class)))
		return element
	 
	def getByXPath(self,  xpath, timeout=3, parentElement=None):	
		if(parentElement != None):
			wait = WebDriverWait(parentElement, timeout)
		else:			
			wait = WebDriverWait(self.browser, timeout)
			try:
				element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
			except Exception as e:
				print ("Error["+ str(e) +"] xpath:")  
				print xpath
				raise "Stop service"
		return element

	def clearInput(self, element):	
		element.click();
		actions =  ActionChains(self.browser)
		actions.key_down(Keys.CONTROL) 
		actions.send_keys('a') 
		actions.key_up(Keys.CONTROL)	
		actions.perform()
		actions.send_keys(Keys.DELETE)
		actions.send_keys(Keys.BACK_SPACE)
		actions.perform()

	def closeBrowser(self):
		self.browser.quit()

