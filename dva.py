#Joshua Brent Collins 4/7/2013 
#This program uses the pygame libs to access multiple cameras at a specified
#resolution, then from each one grab a image and save them to the directory 
#from which it was invoked. Uncomment time if time is needed to free up resouces 
#before the next set of pictures are taken. 
import pygame
import pygame.camera
#import time



print "Please enter setup Information. Camera number: n resolution: w h Picture name: name"

args = raw_input("$>")
args = args.split()
picnum=0
command=""

while True:
	try:
		print "Press Enter to take picture exit to exit."
		option = raw_input("$>")
		index=0
		if len(option) == 0:
			while index < int(args[0]):
				pygame.camera.init()
				command ="/dev/video"+str(index)
				cam = pygame.camera.Camera(command,(int(args[1]),int(args[2])))
				cam.start()
				image = cam.get_image()
				pygame.image.save(image,str(args[3])+str(picnum))
#				time.sleep(.25)
				cam.stop()
				print "File saved!"
				index=index+1
				picnum=picnum+1
		if option == "exit" or option == "Exit":
			break
		else:
			continue
	except:
		print "Error please check arguments for erros or file access permissions!"
		break
