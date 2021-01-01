import uuid
#print (uuid.uuid().hex)
#getting date
import datetime
#today date
now=datetime.datetime.now()
#getting initial inputs
name=input("what is your name? ")
birth_year=int(input("what year were you born? "))

#Getting additional inputs
first= input ("Please chose a  number: ")
second= input ("a second number please: ")

sum =float(first)+float(second)
#age = int(now.year)-int(birth_year)
age = (now.year)-(birth_year)

future_age = round((float (age)+ float(first)))
kids=(second)

#results
print ("Hi " + name+ " the sum of your numbers is "+ str(sum))
print ("Wow, you are now " + str(age ) + " years old")
print ("Smile, you will be "+ str(future_age) + " in "+ str(first) + " years " + "and may have " + str(kids) + " kids")
