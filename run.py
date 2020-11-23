from tkinter import *


class password_strength_checker:
	def __init__(self,password):
		self.password =rf'{password}'

		# saving empty variables
		self.digits_count = 0
		self.small_letters_count = 0
		self.big_letters_count = 0
		self.special_count = 0

		# possibilities
		self.digit_possibility = 10
		self.letter_possibility = 26
		self.special_possibility = 33

	def counter(self):
		# clearing the whitespace from password
		password = self.password.strip()
		# looping in password
		for i in password:
			if i.isdigit() :
				# if it is a number [0-9] 
				# possiblity = 10
				self.digits_count +=1 

			elif i.isalpha() :
				# if is in [a-zA-Z]
				# possiblity = 26
				if i.isupper():
					self.big_letters_count += 1
				else :
					self.small_letters_count += 1
			else:
				# """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
				# possiblity = 33
				self.special_count += 1

	def total_possibitities(self):
		# to calculate the possible password of this format
		dig = self.digit_possibility**self.digits_count if self.digits_count != 0 else 1
		small_alfa = self.letter_possibility**self.small_letters_count if self.small_letters_count != 0 else 1
		big_alfa = self.letter_possibility**self.big_letters_count if self.big_letters_count != 0 else 1
		spe = self.special_possibility**self.special_count if self.special_count != 0 else 1

		# total possibility
		self.tp = (dig*small_alfa*big_alfa*spe)
		return self.tp

	def time_converter(self,time_in_sec):
		# convert the second time in readable format
		result = ''
		centurie = 60*60*24*365*100
		year = 60*60*24*365
		month =60*60*24*30
		week  =60*60*24*7
		day =60*60*24
		hour = 60*60
		minute = 60

		def func(centuries):
			if len(str(centuries)) > 2 and centuries > 20: 
				centuries = str(centuries)[:2] + f'x10**{len(str(centuries))-2}'
			else :
				centuries = str(int(centuries))
			return centuries


		# centuries
		if time_in_sec >= centurie:
			centuries = time_in_sec//centurie
			result += f'{func(centuries)} cen, '
			time_in_sec = time_in_sec%centurie
		else:
			centuries = 0

		# year
		if time_in_sec >= year :
			# convert in years
			years = time_in_sec//year
			result += f'{func(years)} y, '
			time_in_sec = time_in_sec%year
		else:
			years = 0

		# month
		if time_in_sec >= month:
			# convert in months
			months = time_in_sec//month
			result += f'{func(months)} m, '
			time_in_sec = time_in_sec%month
		else:
			months = 0

		# week
		if time_in_sec >= week:
			# convert in weaks
			weeks = time_in_sec//week
			result += f'{func(weeks)} w, '
			time_in_sec = time_in_sec%week
		else:
			weeks = 0

		# day
		if time_in_sec >= day:
			# convert into days
			days = time_in_sec//day
			result += f'{func(days)} d, '
			time_in_sec = time_in_sec%day
		else:
			days = 0

		# hour
		if time_in_sec >= hour:
			# convert into hours
			hours = time_in_sec//hour
			result += f'{func(hours)} h, '
			time_in_sec = time_in_sec%hour
		else:
			hours = 0

		# minute
		if time_in_sec >= minute :
			# convet into min
			minutes = time_in_sec//minute
			result += f'{func(minutes)} m, '
			time_in_sec = time_in_sec%minute
		else:
			minutes = 0

		result += f'{round(time_in_sec)} s'
		# print(result)

		return result,[centuries ,years , months, weeks, days, hours, minutes,time_in_sec]

	def brute_force_time(self) :
		self.total_possibitities()
		print('total_possibitities :',self.tp)
		print()	
		# Online Attack Scenario:
		# (Assuming one thousand guesses per second)	—
		print('Online Attack Scenario: Assuming one thousand guesses per second\n',self.time_converter(self.tp/1_000)[0])
		print()	

		# Offline Fast Attack Scenario:
		# (Assuming one hundred billion guesses per second)	—
		print('Offline Fast Attack Scenario :Assuming one hundred billion guesses per second\n',self.time_converter(self.tp/1_000_000_000)[0])
		print()	

		# Massive Cracking Array Scenario:
		# (Assuming one hundred trillion guesses per second)
		print('Massive Cracking Array Scenario :Assuming one hundred trillion guesses per second\n',self.time_converter(self.tp/1_000_000_000_000)[0])
		print()	

		# self.time_converter(self.tp/1_000)
		# self.time_converter(self.tp/1_000_000_000)
		# self.time_converter(self.tp/1_000_000_000_000)

	@classmethod
	def runner(cls,password):
		psc= cls(password)
		# run the counter
		psc.counter()
		# count total possibilities
		# psc.total_possibitities()
		# find brute_force runtime
		psc.brute_force_time()



# password = 'RiishI23##$khan'

# # running from classmethod
# password_strength_checker.runner(password)


# Gui for program

class Gui(password_strength_checker):
	"""Gui for the password strength generaotor"""
	def __init__(self,master):
		# showing the tk window 
		self.root = master
		master.title('Password Strength Checking.')

		# hwight of the windows
		self.height = 700
		self.width = 1000
		self.root.geometry(f"{self.width}x{self.height}")
		self.root.configure(bg ='#34495E')
		self.head()
		self.input()
		self.calculation_filed()

	def head(self):
		# heading
		head = Label(self.root,text='Password Strength Checker',font=('arial',30,'bold'),fg ='white',bg ='#34495E')
		head.place(relheight=0.15,relwidth=1)

	def input(self):
		password = Entry(self.root,bd=5,font=('arial',20),relief=GROOVE ,exportselection=0,justify=CENTER)
		password.place(relx=0.1,rely=0.15,relheight=0.075,relwidth=0.8)
		# giving placeholder
		password.insert(0, 'Enter your password here')
		# add eventlistener
		password.bind("<FocusIn>", lambda _ : password.delete('0','end'))

		# press enter events execute commends 
		# self.update_cal()
		password.bind("<Return>",lambda _:self.update_cal(password.get()))

	def update_cal(self,password):
		calculations = password_strength_checker(password)
		calculations.counter()
		# character counts 
		self.digits.set(calculations.digits_count)
		self.upppercase.set(calculations.big_letters_count)
		self.lowercase.set(calculations.small_letters_count)
		self.special.set(calculations.special_count)

		# saveign total possibility
		calculations.total_possibitities()
		# time calculations
		one = calculations.time_converter(calculations.tp/1_000)[0]
		self.online.set(one)
		two = calculations.time_converter(calculations.tp/1_000_000_000)[0]
		self.offline.set(two)
		three =calculations.time_converter(calculations.tp/1_000_000_000_000)[0]
		self.massive.set(three)

	def calculation_filed(self):
		# calculations of the password
		# character counts digits ,upppercase,lowercase,special
		Label(self.root,text='Digits',font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.05,rely=0.3,relheight=0.075)
		Label(self.root,text='Upppercase',font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.23,rely=0.3,relheight=0.075)
		Label(self.root,text='Lowercase',font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.55,rely=0.3,relheight=0.075)
		Label(self.root,text='Special',font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.8,rely=0.3,relheight=0.075)

		# values
		self.digits  = StringVar()
		self.upppercase = StringVar()
		self.lowercase = StringVar()
		self.special = StringVar()
		
		# self.digits.set(500)

		Label(self.root,textvariable= self.digits,font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.05,rely=0.38,relheight=0.075)
		Label(self.root,textvariable= self.upppercase,font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.23,rely=0.38,relheight=0.075)
		Label(self.root,textvariable= self.lowercase,font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.55,rely=0.38,relheight=0.075)
		Label(self.root,textvariable= self.special,font=('arial',20),fg ='white',bg ='#34495E').place(relx=0.8,rely=0.38,relheight=0.075)

		# time taken by 3 methods
		# 1. 1_000 Online Attack Scenario: Assuming one thousand guesses per second
		# 1. 1_000_000 Offline Fast Attack Scenario :Assuming one hundred billion guesses per second
		# 1. 1_000_000_000  Massive Cracking Array Scenario :Assuming one hundred trillion guesses per second
		Label(self.root,text=" Online Attack Scenario: Assuming one thousand guesses per second",font=('arial',14,'bold'),wraplength=500,fg ='white',bg ='#34495E').place(rely=0.5,relheight=0.1, relwidth=0.5)
		Label(self.root,text=" Offline Fast Attack Scenario :Assuming one hundred billion guesses per second",font=('arial',14,'bold'),wraplength=500,fg ='white',bg ='#34495E').place(rely=0.7,relheight=0.1, relwidth=0.5)
		Label(self.root,text=" Massive Cracking Array Scenario :Assuming one hundred trillion guesses per second",font=('arial',14,'bold'),wraplength=500,fg ='white',bg ='#34495E').place(rely=0.9,relheight=0.1, relwidth=0.5)

		self.online = StringVar()
		self.offline = StringVar()
		self.massive = StringVar()

		# self.massive.set(10)

		Label(self.root,textvariable=self.online,font=('arial',14),wraplength=300,fg ='white',bg ='#34495E').place(relx=0.55,rely=0.45,relheight=0.17,relwidth=0.45)
		Label(self.root,textvariable=self.offline,font=('arial',14),wraplength=300,fg ='white',bg ='#34495E').place(relx=0.55,rely=0.65,relheight=0.17,relwidth=0.45)
		Label(self.root,textvariable=self.massive,font=('arial',14),wraplength=300,fg ='white',bg ='#34495E').place(relx=0.55,rely=0.85,relheight=0.17,relwidth=0.45)

	@classmethod
	def run(cls):
		root = Tk()
		func = cls(root)
		root.mainloop()


Gui.run()

