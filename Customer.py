import re
import datetime

class Customer:
	def __init__(self):
		# Initialize variables
		self.fullName = ''
		self.gender = ''
		self.canDrink = None
		self.birthDay = None
		self.DOB = None
		self.height = None
		self.weight = None
		self.age = None
		self.budget = None
		self.id = None
		self.firstDrink =None
		self.stdDrink = 0
		#
	def processData(self, rawData):
		# Get raw data from ID card

		# COMMENTED OUT THIS LINE AS RAW DATA SHOULD BE PASSED INTO THE METHOD
		#rawData = input("Swipe ID --> ")

		# Split data into seperate fields
		dividedData = re.split(r'[%^$?;=+ ]+', rawData)
		self.fullName = dividedData[3]+ " " + dividedData[4] + " " + dividedData[2]
		#pull the raw DOB in YYYYMMDD
		self.DOB = dividedData[9][4:12]
		# Divide data
		year = int(self.DOB[0:4])
		month = int(self.DOB[4:6])
		day = int(self.DOB[6:8])
		# Run calculations to get birthday as datetime object
		self.birthDay = datetime.date(year, month, day)
		today = datetime.date.today()


		# Check if user is old enough to drink
		if (int(str(today - self.birthDay)[0:4]) > (21*365)):
		    self.canDrink = True
		else:
		    self.canDrink = False
		self.age = int(str(today - self.birthDay)[0:4]) /365
		self.height = dividedData[13][1] + "\'" + dividedData[13][2:4] + "\""
		self.weight = dividedData[13][4:7] + " pounds"
		if (int(dividedData[13][0]) == 1):
			self.gender = "Male"
		elif (int(dividedData[13][0]) == 2):
			self.gender = "Female"

		self.firstDrink = datetime.datetime.now()
		self.budget = input("Enter your budget for the night --> ")

	def printData(self):
		print(self.fullName)
		print(self.gender)
		print(self.canDrink)
		print(self.birthDay)
		print(self.DOB)
		print(self.height)
		print(self.weight)


	def serializeData(self):
		return {"fullname" : self.fullName, "gender" : self.gender, "canDrink" : str(self.canDrink), "Age":self.age , "Budget": self.budget, "weight":self.budget , "initDrink":self.firstDrink, "stdDrink":self.stdDrink}
