class Introduction:
	def __init__(self, name, age):
		self.name=name
		self.age=age
class User(Introduction):
	def greet(self):
		return "Thank you"

guest=User(str(input("What's your name please?: ")), 17)
import requests, json
import datetime
import random
python_age = random.uniform(5643.564, 87546.7567)
Python=Introduction("Felix's bot", python_age)
print(" ")
print("Hello " ,guest.name, ", I am", Python.name, ", Your virtual Assistant. I am", Python.age, "years old! and I was created by Felix.")
print("I can't do much. I am still a toddler.But I can tell you my name, plural of simple words, today's date,  jokes, calculate and a few other things.")
print("Below are the commands available.\nname\ndate\ntime\ncalc\njoke\nplural\nleap year\nweather\nhello\ngame\nquit")
print("---------------\n---------------")
def jjokes():
	jokess=["When I see lovers' names carved in a tree, I don't think it's sweet. I just think it's surprising how many people bring a knife on a date.", "My dog is an awesome fashion adviser. Every time I ask him what I look like in my clothes, he says 'WOW!' ", "I went to see the doctor about my short-term memory problems. The first thing the bastard did was made me pay in advance.", "I ran into my ex in town yesterday. Then I ran over him and backed up to run into him again.", "What is pointless? To tell a bald guy a hair-raising story."]
	print(" ")
	print("Joke: ", random.choice(jokess))
def game():
	print("The game available is:")
	print("ROCK, PAPER AND SCISSORS")
	print('Let\'s play!')
	countt=0
	sum=0
	while True:
		print("--------------\n-------------")
		print("Enter choice: rock, paper or scissors. \nType 'quit' to end game")
		computer=["rock","paper","scissors"]
		desc=["Computer wins","You win","Its a draw!"]
		com=random.choice(computer)
		print("---------------------")
		player1=str(input("Enter choice: "))
		
		if player1==com:
			print("Computer: ",com)
			print(desc[2])
		elif com =="rock" and player1=="scissors":
			print("computer: ",com)
			print(desc[0])
			countt+=1
			print("Computer: ",countt, "You: ",sum)
		
		elif com =="rock" and player1=="paper":
			print("Computer: ",com)
			print(desc[1])
			sum+=1
			print("Computer: ",countt, "You: ",sum)
		
		elif com=="paper" and player1=="rock":
			print("Computer: ",com)
			print(desc[0])
			countt+=1
			print("Computer: ",countt, "You: ",sum)
		
		elif com =="paper" and player1=="scissors":
			print("Computer: ",com)
			print(desc[1])
			sum+=1
			print("Computer: ",countt, "You: ",sum)
		
		elif com=="scissors" and player1=="rock":
			print("Computer: ",com)
			print(desc[1])
			sum+=1
			print("Computer: ",countt, "You: ",sum)
		elif com=="scissors" and player1=="paper":
			print("Computer: ",com)
			print(desc[0])
			countt+=1
			print("Computer: ",countt, "You: ",sum)
		
		elif player1=="quit":
			print("Game over")
			print("Total score:")
			print("Computer: ",countt, "You: ",sum)
			if countt>sum:
				print("Computer won!")
			elif countt==sum:
				print("It is a draw!")
			else:
				print("You won!")
		
			break
		else:
			print("Invalid entry. Try again")
		
	
def redo():
	print("----------------")
	again=str(input("Is that all? or would you like something else? Please type Y for yes and N for no: "))
	if again.upper()=='Y':
		tasks()
	else:
		print(guest.greet(),guest.name, "See you later!")
def ddate():
	date=datetime.datetime.now()
	print(" ")
	print(guest.name, ", Today's date is: ", date)
def ttime():
	time=datetime.datetime.now().time()
	print(" ")
	print(guest.name, ", The time is currently ", time)
def pplural():
	while True:
		print(" ")
		print("This program gives you the plural of simple words.")
		print(" ")
		print("Singular and Plural")
		word=str(input("Enter word: "))
		if word.endswith('s') or word.endswith('x') or word.endswith('o'):
			plural=word + 'es'
			print("{}      -      {}".format(word, plural))
			print(" ")
			print(" ")
#asks if the user wants to enter another word
			reply=input("Do you want to try another word? Please type Y for yes and N for no: ")
			if reply.upper()=='Y':
				continue
			else:
				print(" ")
				redo()
		if word[:-1].endswith('a') or word[:-1].endswith('e') or word[:-1].endswith('i') or word[:-1].endswith('o') or word[:-1].endswith('u') or word[:-1].endswith('t'):
			plural=word + 's'
			print("{}      -      {}".format(word, plural))
			print(" ")
			print(" ")
			reply=input("Do you want to try another word? Please type Y for yes and N for no: ")
			if reply.upper()=='Y':
				continue
			else:
				print(" ")
				print("See you later!")
			redo()
		elif word.endswith('y'):
			plural=word[:-1] + 'ies'
			print("{}      -      {}".format(word, plural))
			print(" ")
			print(" ")
			reply=input("Do you want to try another word? Please type Y for yes and N for no: ")
			if reply.upper()=='Y':
				continue
			else:
				print(" ")
				print("See you later!")
				redo()
		elif word.endswith('h'):
			plural=word+'es'
			print("{}      -      {}".format(word, plural))
			print(" ")
			print(" ")
			reply=input("Do you want to try another word? Please type Y for yes and N for no: ")
			if reply.upper()=='Y':
				continue
			else:
				print(" ")
				print("See you later!")
				redo()
		else:
			plural=word + "s"
			print("{}      -      {}".format(word, plural))
			print(" ")
			print(" ")
			reply=input("Do you want to try another word? Please type Y for yes and N for no: ")
			if reply.upper()=='Y':
				continue
			else:
				print(" ")
				print("See you later!")
				redo()
def nname():
	print("My name is", Python.name)
def hhello():
	print("Hey", guest.name, ", I'm very excited to meet you. Just tell me what I can do for you today!")
	tasks()
def tasks():
	com=str(input("So, what do you do need me to do?: "))
	if com=="hello":
		hhello()
	elif com=="game":
		game()
		redo()
	elif com=="quit":
		print(guest.greet(),guest.name, "See you later!")
	elif com=="time":
		ttime()
		redo()
	elif com=="date":
		ddate()
		redo()
	elif com=="joke":
		jjokes()
    elif com=="name":
		nname()
		redo()
	elif com=="weather":
		print(" ")
		print("Welcome to Felix's Weather Forecast! Please ensure your data connection is turned on. Thank you.")
		print(" ")
		api_key=
		base_url="http://api.openweathermap.org/data/2.5/weather?"
		city_name=input("Enter city name: ")
		complete_url= base_url + "appid=" + api_key + "&q=" + city_name
		response=requests.get(complete_url)
		x=response.json()
		if x['cod'] !='404':
			y=x["main"]
			current_temperature=y['temp']
			current_pressure=y['pressure']
			current_humidity=y["humidity"]
			z=x["weather"]
			weather_description=z[0]["description"]
			print(" Temperature (in kelvin unit) = " +

                    str(current_temperature) + 

          "\n atmospheric pressure (in hPa unit) = " +

                    str(current_pressure) +

          "\n humidity (in percentage) = " +

                    str(current_humidity) +

          "\n description = " +

                    str(weather_description)) 

  

		else: 

   		 print(" City Not Found ")
		redo()
	elif com=="calc":
		while True:		
			print(".")
			print(".")
			print("Hello,", guest.name, ", Welcome to Felix's calculator, Below are the available options:")
			print("Enter 'add' to add numbers")
			print("Enter 'subtract' to subtract numbers")
			print("Enter 'multiply' to multiply numbers")
			print("Enter 'divide' to divide numbers")
			print("Enter 'quit' to end program")
			print(".")
			word=input("What do you want to do?:")
	
			if word == "quit":
				print(guest.greet(), guest.name, "for using Felix's calculator")
				input(" How was your experience? \n'Good' or 'bad'?: ")
				print(guest.greet(), guest.name, " for the comment. We'll also work on an upgrade. See you soon", name, "!")
				redo()
			elif word == "add":
				num1=(input("Type first number: "))
				num2 = (input("Type second number: "))
				ans=float(num1) + float(num2)
				print("{} + {} =".format(num1, num2))
				print(ans)
		
			elif word == "subtract":
				num1=(input("Type first number: "))
				num2= (input("Type second number: "))
				ans=float(num1) - float(num2)
				print("{} + {} = ".format(num1, num2))
				print(ans)
			
			elif word == "multiply":
				num1= (input("Type first number: "))
				num2= (input("Type second number: "))
				ans= float(num1) * float(num2)
				print("{} * {} = ".format(num1, num2))
				print(ans)
		
			elif word == "divide":
				num1 = (input("Type first number: "))
				num2 = (input("Type second number: "))
				ans= float(num1)/float(num2)
				print("{} / {} = ".format(num1, num2))
				print(ans)
		
			else:
				print("I'm sorry", guest.name, ", invalid operation!\nPlease, Try again")
	elif com=="plural":
		pplural()
	elif com=="leap year":
		print(" ")
		print("Welcome to Felix Leap Year calculator!")
		year = int(input("Enter a year: "))  
		if (year % 4) == 0:  
			if (year % 100) == 0: 
				if (year % 400) == 0:
					print("{} is a leap year".format(year))
				else:
					print("{} is not a leap year".format(year))
			else: 
				print("{} is a leap year".format(year))  
		else:
			print("{} is a leap year".format(year))
		redo()
	else:
		print(" ")
		print("Felix Bot: Ooops, Sorry, I can't do that now. Try another command")
		tasks()
tasks()