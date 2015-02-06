#Joshua B. Collins 
#Calculator app 
#5/1/2013

import Tkinter as t
import math as mt

class calculator:

	def __init__(self):

#Basic setup of some var and frame
		self.Main = t.Tk()
		self.userinput = t.StringVar(self.Main)
		self.stack = []
		self.userinput.set("")		
		self.Main.title("Calculator")
		self.Main.maxsize(300,200)
		self.Main.minsize(300,200)
		self.output = t.Label(self.Main,width = 25, textvariable = self.userinput,relief=t.SUNKEN)
		self.output.pack()




#Frames to justify buttons

		self.bf1 = t.Frame(self.Main,name="bf1")
		self.bf1.pack(side=t.LEFT)
		self.bfz = t.Frame(self.bf1,name="bfz")
		self.bfz.pack(side=t.BOTTOM)		
		self.bf3 = t.Frame(self.bf1,name="bf3")
		self.bf3.pack(side=t.BOTTOM)
		self.bf2 = t.Frame(self.bf1,name="bf2")
		self.bf2.pack(side=t.BOTTOM)




#Frames for operators

		self.opf1 = t.Frame(self.Main,name="opf1")
		self.opf1.pack(side=t.RIGHT)
		self.opf6 = t.Frame(self.opf1,name="opf6")
		self.opf6.pack(side=t.BOTTOM)
		self.opf5 = t.Frame(self.opf1,name="opf5")
		self.opf5.pack(side=t.BOTTOM)
		self.opf4 = t.Frame(self.opf1,name="opf4")
		self.opf4.pack(side=t.BOTTOM)
		self.opf3 = t.Frame(self.opf1,name="opf3")
		self.opf3.pack(side=t.BOTTOM)
		self.opf2 = t.Frame(self.opf1,name="opf2")
		self.opf2.pack(side=t.BOTTOM)
		

#Buttons
		self.clear = t.Button(self.Main,text="CLR",name="clear",height = 1,width=2)
		self.clear.bind("<ButtonPress>",self.event_listener)
		self.clear.pack(side = t.BOTTOM)


		self.enter = t.Button(self.Main,text="Enter",name="enter",height = 1,width=2)
		self.enter.bind("<ButtonPress>",self.event_listener)
		self.enter.pack(side = t.BOTTOM)

		self.one = t.Button(self.bfz,text="+/-",name="+/-",width=4)
		self.one.bind("<ButtonPress>",self.event_listener)
		self.one.pack(side=t.BOTTOM)


		self.one = t.Button(self.bf1,text="1",name="1")
		self.one.bind("<ButtonPress>",self.event_listener)
		self.one.pack(side=t.LEFT)


		self.two = t.Button(self.bf1,text="2",name="2")
		self.two.bind("<ButtonPress>",self.event_listener)
		self.two.pack(side=t.LEFT)

		self.three = t.Button(self.bf1,text="3",name="3")
		self.three.bind("<ButtonPress>",self.event_listener)
		self.three.pack(side=t.LEFT)

		self.four = t.Button(self.bf2,text="4",name="4")
		self.four.bind("<ButtonPress>",self.event_listener)
		self.four.pack(side=t.LEFT)

		self.five = t.Button(self.bf2,text="5",name="5")
		self.five.bind("<ButtonPress>",self.event_listener)
		self.five.pack(side=t.LEFT)

		self.six = t.Button(self.bf2,text="6",name="6")
		self.six.bind("<ButtonPress>",self.event_listener)
		self.six.pack(side=t.LEFT)

		self.seven = t.Button(self.bf3,text="7",name="7")
		self.seven.bind("<ButtonPress>",self.event_listener)
		self.seven.pack(side=t.LEFT)

		self.eight = t.Button(self.bf3,text="8",name="8")
		self.eight.bind("<ButtonPress>",self.event_listener)
		self.eight.pack(side=t.LEFT)

		self.nine = t.Button(self.bf3,text="9",name="9")
		self.nine.bind("<ButtonPress>",self.event_listener)
		self.nine.pack(side=t.LEFT)

		self.pi = t.Button(self.bfz,text="pi",name="pi",height = 1,width=1)
		self.pi.bind("<ButtonPress>",self.event_listener)
		self.pi.pack(side=t.LEFT)

		self.zero = t.Button(self.bfz,text="0",name="0")
		self.zero.bind("<ButtonPress>",self.event_listener)
		self.zero.pack(side=t.LEFT)

		self.e = t.Button(self.bfz,text="e",name="e",height = 1,width=1)
		self.e.bind("<ButtonPress>",self.event_listener)
		self.e.pack(side=t.LEFT)

		self.add = t.Button(self.opf1,text="+",name="+",height = 1,width=1)
		self.add.bind("<ButtonPress>",self.event_listener)
		self.add.pack(side=t.RIGHT)

		self.sub = t.Button(self.opf1,text="-",name="-",height = 1,width=1)
		self.sub.bind("<ButtonPress>",self.event_listener)
		self.sub.pack(side=t.RIGHT)

		self.div= t.Button(self.opf2,text="/",name="/",height = 1,width=1)
		self.div.bind("<ButtonPress>",self.event_listener)
		self.div.pack(side=t.RIGHT)

		self.mult = t.Button(self.opf2,text="*",name="*",height = 1,width=1)
		self.mult.bind("<ButtonPress>",self.event_listener)
		self.mult.pack(side=t.RIGHT)

		self.sqrt = t.Button(self.opf3,text= u'\u221a',name="sqrt",height = 1,width=1)
		self.sqrt.bind("<ButtonPress>",self.event_listener)
		self.sqrt.pack(side=t.RIGHT)

		self.pow = t.Button(self.opf3,text="^",name="pow",height = 1,width=1)
		self.pow.bind("<ButtonPress>",self.event_listener)
		self.pow.pack(side=t.RIGHT)

		self.mod = t.Button(self.opf4,text="%",name="mod",height = 1,width=1)
		self.mod.bind("<ButtonPress>",self.event_listener)
		self.mod.pack(side=t.RIGHT)


		self.recp = t.Button(self.opf4,text="1/x",name="recp",height = 1,width=1)
		self.recp.bind("<ButtonPress>",self.event_listener)
		self.recp.pack(side=t.RIGHT)

		self.sin = t.Button(self.opf5,text="sinx",name="sin",height = 1,width=1)
		self.sin.bind("<ButtonPress>",self.event_listener)
		self.sin.pack(side=t.RIGHT)

		self.cos = t.Button(self.opf5,text="cosx",name="cos",height = 1,width=1)
		self.cos.bind("<ButtonPress>",self.event_listener)
		self.cos.pack(side=t.RIGHT)

		self.tan = t.Button(self.opf6,text="tanx",name="tan",height = 1,width=1)
		self.tan.bind("<ButtonPress>",self.event_listener)
		self.tan.pack(side=t.RIGHT)

		self.dec = t.Button(self.opf6,text=".",name="dec",height = 1,width=1)
		self.dec.bind("<ButtonPress>",self.event_listener)
		self.dec.pack(side=t.RIGHT)


		#Start execution
		self.Main.mainloop()


	def event_listener(self,event):
		
		hold  = ""
				
		if(str(event.widget) == ".clear"):
			self.stack=[]
			self.userinput.set("")
			
		if(str(event.widget) == ".enter"):
 			try:
				temp = self.userinput.get()
				temp= float(temp)
				self.stack.append(temp)
				self.userinput.set("")
			except ValueError:
				self.userinput.set("ERR! Please clear and try again.")

					
		if(str(event.widget) == ".bf1.bfz.0"):
			hold = self.userinput.get() + "0"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bfz.pi"):
			hold = self.userinput.get() + str(mt.pi)
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bfz.e"):
			hold = self.userinput.get() + str(mt.e)
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.1"):
			hold = self.userinput.get() + "1"
			self.userinput.set(hold)		
		if(str(event.widget) == ".bf1.2"):
			hold = self.userinput.get() + "2"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.3"):
			hold = self.userinput.get() + "3"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf2.4"):
			hold = self.userinput.get() + "4"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf2.5"):
			hold = self.userinput.get() + "5"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf2.6"):
			hold = self.userinput.get() + "6"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf3.7"):
			hold = self.userinput.get() + "7"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf3.8"):
			hold = self.userinput.get() + "8"
			self.userinput.set(hold)
		if(str(event.widget) == ".bf1.bf3.9"):
			hold = self.userinput.get() + "9"
			self.userinput.set(hold)
		if(str(event.widget) == ".opf1.opf6.dec"):
			hold = self.userinput.get() + "."
			self.userinput.set(hold)
		if(str(event.widget) == ".opf1.+"):
			try:
				self.stack.append("+")
				self.calculatebinary()
			except ValueError:
				pass
		if(str(event.widget) == ".opf1.-"):
			try:
				self.stack.append("-")
				self.calculatebinary()
			except ValueError:
				pass

			except ValueError:
				pass
		if(str(event.widget) == ".opf1.opf2.*"):
			try:
				self.stack.append("*")
				self.calculatebinary()
			except ValueError:
				pass
		if(str(event.widget) == ".opf1.opf2./"):
			try:
				self.stack.append("/")
				self.calculatebinary()
			except ValueError:
				pass
		if(str(event.widget) == ".opf1.opf3.pow"):
			try:
				self.stack.append("^")
				self.calculatebinary()
			except ValueError:
				pass
		if(str(event.widget) == ".opf1.opf3.sqrt"):
			try:
				self.stack.append("sqrt")
				self.calculateunary()
			except ValueError:
				pass
		if(str(event.widget) == ".opf1.opf4.mod"):
			try:
				self.stack.append("%")
				self.calculatebinary()
			except ValueError:
				pass

		if(str(event.widget) == ".opf1.opf4.recp"):
			try:
				self.stack.append("1/")
				self.calculateunary()
			except ValueError:
				pass

		if(str(event.widget) == ".opf1.opf5.sin"):
			try:
				self.stack.append("sin")
				self.calculateunary()
			except ValueError:
				pass

		if(str(event.widget) == ".opf1.opf5.cos"):
			try:
				self.stack.append("cos")
				self.calculateunary()
			except ValueError:
				pass

		if(str(event.widget) == ".opf1.opf6.tan"):
			try:
				self.stack.append("tan")
				self.calculateunary()
			except ValueError:
				pass
		if(str(event.widget) == ".bf1.bfz.+/-"):
			try:
				if(self.userinput.get()[0] == "-"):
					self.userinput.set(self.userinput.get()[1:])
				else:
					self.userinput.set("-"+self.userinput.get())
				
			except :
				pass



	def calculatebinary(self):
		try:
			check = str(self.stack.pop())
			if(not(check == "^")):					
				exp=""			
				exp = exp + str(self.stack.pop(-2))
				exp = exp + check
				exp = exp + str(self.stack.pop())
				answer = eval(exp)
							
			else:
				
				answer =str(pow(self.stack.pop(-2),self.stack.pop()))


			self.stack.append(answer)
			self.userinput.set(self.stack[-1])





				
				
		except:
			self.userinput.set("Expr Error! Clear and try again.")										
	def calculateunary(self):
		try:
			op = self.stack.pop()
			num = self.stack.pop()
			if(op == "sin"):
				answer = str(mt.sin(num))
			if(op == "cos"):
				answer = str(mt.cos(num))
			if(op == "tan"): 
				answer = str(mt.tan(num))
			if(op == "1/"):
				answer = str((1/num))
			if(op == "+/-"):
				answer = num * -1
			if(op == "sqrt"):
				answer = str(mt.sqrt(num))

			self.stack.append(answer)
			self.userinput.set(self.stack[-1])

				
			
									


		except:
			self.userinput.set("Expr Error! Clear and try again.")	
		
cal = calculator()

