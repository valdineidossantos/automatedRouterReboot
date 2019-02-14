
from router import RouterBase
from time import sleep
from selenium.webdriver.common.alert import Alert

class RouterNokia(RouterBase):
	"""
	RouterNokia Device G-240W-A 
	Software Version 3FE56557AFIA53
	Boot Version U-Boot Apr-03-2018--14:05:27
	"""
	def __init__(self):
		super(RouterNokia, self).__init__()		
		self.__username="userAdmin"
		self.__password="4791330357"
		

	def reboot(self):
		self.__go()
		self.__fillUsername()
		self.__fillPassword()
		self.__clickSubmitLogin()
		self.__clickMaintenanceLink()
		self.__clickRebootLink()
		self.__switchToMainFrame()
		self.__clickRebootButton()
		self.__confirmAlertMessage()

		
	
	def __fillUsername(self):
		inputUsername = self.getByXPath("//input[@id='username']")
		inputUsername.send_keys(self.__username)
		return inputUsername

	def __fillPassword(self):
		inputPassword = self.getByXPath("//input[@id='password']")
		inputPassword.send_keys(self.__password)
		return inputPassword

	def __clickSubmitLogin(self):
		submitButton = self.getByXPath("//input[@type='submit']")
		submitButton.click()
		return submitButton

	def __clickMaintenanceLink(self):
		maintenanceLink = self.getByXPath("//ul[@class='x_main_menu']/li/a/p[text()='Maintenance']")
		maintenanceLink.click()
		return maintenanceLink

	def __clickRebootLink(self):	
		rebootLink = self.getByXPath("//li[@class='x_sub_menu']/a[text()='Reboot Device']")
		rebootLink.click()
		return rebootLink

	def __switchToMainFrame(self):
		mainFrame = self.getByXPath("//iframe[@name='mainFrame']")		
		self.browser.switch_to.frame(mainFrame)

	def __clickRebootButton(self):
		rebootButton = self.getByXPath("//input[@class='buttonX' and @id='do_reboot']")
		rebootButton.click()
		return rebootButton

	def __confirmAlertMessage(self):
		#Alert(self.browser).dismiss()
		Alert(self.browser).accept()
		
	def __go(self):
		self.__routerUrl ="https://192.168.1.254"		
		self.browser.get(self.__routerUrl)


	