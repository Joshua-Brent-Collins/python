#Joshua Brent Collins 4/5/2013


while True:
	try:
		print "Enter the name of the file to be analyzed."
		fname = raw_input("$>")
		data = open(fname,'r').readlines()
		break
	except IOError:
		print "Error bad file name or permissions!"
		continue

print "Please wait while data is analyzed this may take several minutes dependening on documnet size."
x=0
analysis = dict()
#convert to lower and replace punctuation
for word in data[:]:
	word=word.lower()
	for char in word[:]:
		if ord(char) >= 48 and ord(char) <= 57 or ord(char) >= 97 and ord(char) <= 122 :
			pass
		else:	
			word = word.replace(char," ")
	data[x] = word
	x=x+1
#break word into list
data = ''.join(data)
data = data.split(" ")
#strip extra spaces
for i in data[:]:
	if i == '':
    		data.remove(i) 
x=0


while True:
	print "Please select the option for data analysis. -1 to exit."
	print "1.Letter frequency with ordered respect to letter frequency."
	print "2.Letter frequency with ordered respect to alphanumeric order."
	print "3.Word frequency with ordered respect to word frequency."
	print "4.Word frequency with ordered respect to alphanumeric order."
	try:
		option = int( raw_input("$>") )
		if(option == 1):
			x=0
			print "Please wait while data is analyzed this may take several minutes dependening on document size."
			hold = set(data)
			del analysis
			analysis = dict()			   
			for j in hold:
				for i in j:
					analysis.update({i:0})
			for wc in data:
				for ch in wc:
					analysis[ch]=analysis[ch]+1
			for t in sorted(analysis,key=analysis.get,reverse=True):  
					print sorted(analysis,key=analysis.get,reverse=True)[x] ,"occurs :",analysis[t]," time(s) in ", fname	
					x=x+1
		if(option == 2):
			x=0
			print "Please wait while data is analyzed this may take several minutes dependening on document size."
			hold = set(data)
			del analysis
			analysis = dict()			   
			for j in hold:
				for i in j:
					analysis.update({i:0})
			for wc in data:
				for ch in wc:
					analysis[ch]=analysis[ch]+1
			for t in sorted(analysis):  
					print sorted(analysis)[x] ,"occurs :",analysis[t]," time(s) in ", fname	
					x=x+1
		if(option == 3):
			x=0
			print "Please wait while data is analyzed this may take several minutes dependening on document size."
			hold = set(data)
			del analysis
			analysis = dict()			   
			for j in hold:
				analysis.update({j:0})
			for wc in data:
				analysis[wc]=analysis[wc]+1
			for t in sorted(analysis,key=analysis.get,reverse=True):  
					print sorted(analysis,key=analysis.get,reverse=True)[x] ,"occurs :",analysis[t]," time(s) in ", fname	
					x=x+1
	
		if(option == 4):
			x=0
			print "Please wait while data is analyzed this may take several minutes dependening on document size."
			hold = set(data)
			del analysis
			analysis = dict()			   
			for j in hold:
				analysis.update({j:0})
			for wc in data:
				analysis[wc]=analysis[wc]+1
			for t in sorted(analysis):  
					print sorted(analysis)[x] ,"occurs :",analysis[t]," time(s) in ", fname	
					x=x+1
		if(option == -1):
			break
	except ValueError:
		print "Invalid option!"
		option = 0
		continue



	
	
