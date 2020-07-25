from os import path, makedirs
import csv
import socket
import random
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import platform
from datetime import datetime

def Initialise():
	if not path.exists("C:\\Projects\\Python\\Banking2"):
		makedirs("C:\\Projects\\Python\\Banking2")
	
	if not path.exists("C:\\Projects\\Python\\Banking2\\All_Users.csv"):
		column_names = ["Name", "Username", "Email", "Balance", "Transactions", "Acc Cre. Date", "Password"]
		file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv", 'a', newline = '')
		cursor = csv.writer(file)
		cursor.writerow(column_names)
		file.close()

def Internet_Available():
	IP_Address = socket.gethostbyname(socket.gethostname())
	if IP_Address == "127.0.0.1":
		return False
	return True

def Check_For_Availabilty(utility_no, utility_value):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	all_users_details = list(csv.reader(file))
	file.close()
	for details in all_users_details:
		if details[utility_no] == utility_value:
			return True
	return False

def New_User_Write(user_details):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv", 'a', newline = '')
	cursor = csv.writer(file)
	cursor.writerow(user_details)
	file.close()

def Generate_Verification_Code():
	return str(random.randint(100000, 999999))

def Send_Verification_Code(user_email, vcc_code):
	try:
		sender_email = "YOUR EMAIL ID"
		reciever_email = user_email[:]

		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = reciever_email
		message["Subject"] = "Verification Code For Account Registration At Banking Project"
		body = "Respected Customer,\nYour Verification Code For The Account Registration Is {} .\nRegards,\nBank".format(vcc_code)
		message.attach(MIMEText(body, 'plain'))
		message = message.as_string()

		context = ssl.create_default_context()
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls(context=context)
		server.ehlo()
		server.login(sender_email, "YOUR EMAIL PASSWORD")
		server.sendmail(sender_email, reciever_email, message)
		server.quit()
	except:
		pass

def Get_System_Owner_Name():
	return str(platform.node()).title()

class Invalid_Name(Exception):
	'''This Exception Is Raised When The User Leaves
	The Name Field Empty.'''
	pass

class Invalid_Username(Exception):
	'''This Exception Is Raised When The User Leaves
	The Username Field Empty.'''
	pass

class Username_Taken(Exception):
	'''This Exception Is Raised When The User Enters
	An Username Which Is Already In Use.'''
	pass

class Invalid_Password(Exception):
	'''This Exception Is Raised When The User Leaves 
	The Password Field Empty.'''
	pass

class Password_Did_Not_Match(Exception):
	'''This Exception Is Raised When The Confirmation
	Password Did Not Match With The Password.'''
	pass

class Invalid_Email(Exception):
	'''This Exception Is Raised When The User Enters
	An Invalid Email Address In The Email Field.'''
	pass

class Email_Taken(Exception):
	'''This Exception Is Raised When The User Enters
	An Email Which Is Already In Use.'''
	pass

class Wrong_VCCode(Exception):
	'''This Exception Is Raised When The User Enters
	The Wrong Verification Code.'''
	pass

class Not_Agreed(Exception):
	'''This Exception Is Raised When The User Did Not
	Agree To The Terms And Conditions.'''
	pass

class No_Internet(Exception):
	'''This Exception Is Raised When The User Is
	Not Connected To The Internet'''
	pass

def Registration_Completion_Mail(user_name, user_email):
	try:
		sender_email = "YOUR EMAIL ID"
		reciever_email = user_email[:]

		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = reciever_email
		message["Subject"] = "Registration Successfull At The Banking Project"
		body = "Dear {},\nWe Appreciate You For Becoming Our Customer.\n"
		body = body + "Regards,\nBank\n"
		body = body + "\nYour Account Is Created From An Computer With Below Information :\n"
		body = body + "System Name : {}\nSystem OS : {}\nSystem IPv4 Address : {}\n\n"
		body = body.format(user_name, platform.node(), platform.system() + " " + platform.release(), socket.gethostbyname(socket.gethostname()))
		message.attach(MIMEText(body, 'plain'))

		message = message.as_string()

		context = ssl.create_default_context()
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls(context = context)
		server.ehlo()
		server.login(sender_email, "YOUR EMAIL PASSWORD")
		server.sendmail(sender_email, reciever_email, message)
		server.quit()
	except:
		pass

def Current_Date_Time():
	return datetime.now().strftime("%A %B %d, %I:%M %p, %Y")

def Check_True_User(uname_email, password):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()
	for user_details in contents:
		if user_details[1] == uname_email or user_details[2] == uname_email:
			if user_details[-1] == password:
				return True
	return False

class No_User(Exception):
	'''This Exception Is Raised When The User's Login
	Credentials Are Incorrent.'''
	pass

def Send_Password_Code(user_email, vcc_code):
	try:
		sender_email = "YOUR EMAIL ID"
		reciever_email = user_email[:]

		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = reciever_email
		message["Subject"] = "Verification Code For Account Password Reset At Banking Project"
		body = "Respected Customer,\nYour Verification Code For The Account Password Reset Is {} .\nRegards,\nBank".format(vcc_code)
		message.attach(MIMEText(body, 'plain'))
		message = message.as_string()

		context = ssl.create_default_context()
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls(context=context)
		server.ehlo()
		server.login(sender_email, "YOUR EMAIL PASSWORD")
		server.sendmail(sender_email, reciever_email, message)
		server.quit()
	except:
		pass

def Reset_Password(user_email, new_password):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()
	for details in contents:
		if details[2] == user_email:
			details[-1] = new_password
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv", "w", newline = '')
	cursor = csv.writer(file)
	for dc in contents:
		cursor.writerow(dc)
	file.close()

def Retrieve_Users_Data(uname_email):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()
	for data in contents:
		if data[1] == uname_email or data[2] == uname_email:
			return data

def Overwrite_Data(user_data, code = 0):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()

	if not code:
		pos = Retreive_User_Pos(user_data[1])
	else:
		pos = Retreive_User_Pos(user_data[2])

	contents[pos] = user_data

	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv", 'w', newline = '')
	cursor = csv.writer(file)
	for data in contents:
		cursor.writerow(data)
	file.close()

def Retreive_User_Pos(value):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()

	for i in range(len(contents)):
		if contents[i][1] == value or contents[i][2] == value:
			return i 

def Retreive_All_Users_Names():
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	user_names = [x[1] for x in list(csv.reader(file))]
	file.close()
	del user_names[0]
	return user_names

def Get_User_Position(uname_or_email):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()
	for i in range(len(contents)):
		if contents[i][1] == uname_or_email or contents[i][2] == uname_or_email:
			return i

class Invalid_Amount(Exception):
	'''This Exception Is Raised When The User Inputs
	An Invalid Amount.'''
	pass

class Insufficient_Balance(Exception):
	'''This Exception Is Raised When The User Tries 
	To Withdraw Money Greater Than His Actual Balance.'''
	pass

def Modify_Content_In_File(user_data):
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv")
	contents = list(csv.reader(file))
	file.close()

	contents[Get_User_Position(user_data[1])] = user_data
	file = open("C:\\Projects\\Python\\Banking2\\All_Users.csv", 'w', newline = '')
	cursor = csv.writer(file)
	for data in contents:
		cursor.writerow(data)
	file.close()

def Write_To_Passbook(code, pos, amount, balance, reciever = ""):
	file_loc = "C:\\Projects\\Python\\Banking2\\{}.txt".format(pos)
	file = open(file_loc, 'a')
	if not code:
		content_to_write = "{} Rs Has Been Deposited On {} . Account Balance : {} Rs".format(amount, Current_Date_Time(), balance)
	elif code == 1:
		content_to_write = "{} Rs Has Been Withdrawed On {} . Account Balance : {} Rs".format(amount, Current_Date_Time(), balance)
	elif code == 2:
		content_to_write = "{} Rs Has Been Transferred To {} On {} . Account Balance : {} Rs".format(amount, reciever, Current_Date_Time(), balance)
	elif code == 3:
		content_to_write = "{} Rs Has Been Recieved From {} On {} . Account Balance : {} Rs".format(amount, reciever, Current_Date_Time(), balance)
	file.write(content_to_write + "\n")
	file.close()

def Transactional_Email(code, user_data, amount, reciever = ""):
	try:
		sender_email = "YOUR EMAIL ID"
		reciever_email = user_data[2]

		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = reciever_email

		if not code:
			message["Subject"] = "Deposition On Bank Is Successfull"
			body = "Dear {},\nRs {} Has Been Added To Your Main Account Balance.\nYour Current Account Balance Is : {} Rs .\nRegards,\nThe Bank.\n"
			body = body.format(user_data[0], amount, user_data[3])
		elif code == 1:
			message["Subject"] = "Money Withdraw Successfull From Bank"
			body = "Dear {},\nRs {} Has Been Withdrawed From Your Main Account Balance.\nYour Current Account Balance Is : {} Rs .\nRegards,\nThe Bank.\n"
			body = body.format(user_data[0], amount, user_data[3])
		elif code == 2:
			message["Subject"] = "Money Has Been Transferred Successfully"
			body = "Dear {},\nRs {} Has Been Transferred To {} From Your Main Account Balance.\nYour Current Account Balance Is : {} Rs .\nRegards,\nThe Bank.\n"
			body = body.format(user_data[0], amount, reciever, user_data[3])
		elif code == 3:
			message["Subject"] = "Money Has Been Recieved Successfully"
			body = "Dear {},\nRs {} Has Been Recieved From {}.\nYour Current Account Balance Is : {} Rs .\nRegards,\nThe Bank.\n"
			body = body.format(user_data[0], amount, reciever, user_data[3])

		body = body + "\nTransaction Is Executed From An Computer With Below Information :\n"
		body = body + "System Name : {}\nSystem OS : {}\nSystem IPv4 Address : {}\n\n"
		body = body.format(platform.node(), platform.system() + " " + platform.release(), socket.gethostbyname(socket.gethostname()))
		message.attach(MIMEText(body, 'plain'))

		message = message.as_string()

		context = ssl.create_default_context()
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls(context = context)
		server.ehlo()
		server.login(sender_email, "YOUR EMAIL PASSWORD")
		server.sendmail(sender_email, reciever_email, message)
		server.quit()
	except:
		pass

#