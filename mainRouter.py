
from nokiaRouter import RouterNokia
from time import clock
import atexit
from timing import endlog, log 


if __name__ == '__main__':

	try:
		nokia =  RouterNokia()
		nokia.reboot()
	except Exception as ex:
		print (ex)
	
	finally:
		print "Closing browser"
		#nokia.closeBrowser()
		
		