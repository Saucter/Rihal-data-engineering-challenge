#Libraries
#installation of the all the required libraries
import re
import datetime
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #telling tesseract the executable  file's location


#OCR
#The code that would read the image given in the challenge
email_image = cv2.imread("email.png") #Converts the image email.png (which is the image that is used for the challenege) into a an image that can be used by the program
txt = pytesseract.image_to_string(email_image) #pytesseract converts the text in the image into a string which is then placed into the variable (txt)


#Dates
print("")
dates = re.findall(r"[0-9]+/[0-9]+/[0-9]+", txt) #Finds integers from 0 to 9 that occur more than once, and after which have a '/', this is done three tiems so that the code looks for xxxx/xx/xx
dates_sorted_2 = [] #An array/list that would be used later
num_of_dates = len(dates) #This turns the total numbers of items (no matter what type) within the list and turns it into an integer, which has been placed into num_of_dates
x = 0
while x < num_of_dates: #The indented code will repeat as long as x (which is initally 0) is less than num_of_dates (the total numebr of items in the list dates
    dates_2 = datetime.datetime.strptime(dates[x], '%d/%m/%Y') #This line turns the string date[x] -an array that would initially date[0] which is the first date in the list- into a data type known as date which can be recognized by datetime, this is done by showing that the dates in the list are formatted as date, month, year, said date is then palced in a variable called date_2
    dates_sorted = dates_2.strftime('%Y/%m/%d') #This lines formats the vairiable that contains the dates (date_2) into a years, months, dates. It is then stored into a variable called date_sorted
    dates_sorted_2.append(dates_sorted) #This appends dates_sorted into the list that was previously made (dates_sorted_2)
    x+=1 #This line increments x so that when the while loop repeats (i.e. it would turn from 0 to 1 in the second loop), which would change the date[x] string, making it the second item in the list


#Room Names
room_names = re.findall(r"Room:\s\w+", txt) #This line looks for anything that comes after the word "Room:"
room_names_new = [] #A list that would be used later
for i in room_names: #Makes a for loop with a temporary variable 'i'
    room_names_new.append(i[6:]) #Removes the first 6 characters from every item in the list, with said characters being the Room:(whites space)


#Room Rates
room_rates = re.findall(r"\$[0-9]+", txt) #Looks for any numbers that come after a dollar sign symbol ($) and puts them in the variable room_rates


#Names
names = re.findall(r"[A-Z][a-z]+ \w+, [A-Z][a-z]+|[A-Z][a-z]+, [A-Z][a-z]+", txt) #Looks for a string that starts with capital latter, followed by a comma, and then another string that starts with a capital letter. It either looks for that or any anything that starts with two string that start with a capital letter before a comma and a string that starts with a capital letter, this is done to take into account names with more than one word such as Indian, Chineese, or in this case, Arabic names
i = 0
names_sorted = [] #A list that would be used later
num_names = len(names) #Takes the numerb of total items in the list names and turns it into an integer, said integer is palced into a variable called num_names
while i < num_names: #The indented lines will loop as long as i is smaller than the number of items in in the names list (smaller than num_names)
    names_comma = names[i].replace(",", "") #This takes the first item in the list as s tring and removes the comma from the name, it is then put into a variable (names_comma)
    names_new = names_comma.split() #This takes names_comma and changes it to a list called names_new in which all words are separate items in the list
    names_new.insert(0, names_new.pop()) #This takes the last name in the list and moves it to position 0 (which is the first position in the list), this allows for the formatting to change from last name - first name to first name - last name
    names_new_2 = " ".join(names_new) #This turns the items in the list names_new into a string that is placed in the same order as the order of the items in the list. Said string is placed into a variable called names_new_2
    names_sorted.append(names_new_2) #This puts names_new_2 into the list that was made earlier (names_sorted)
    i += 1 #This increments i so that in the next loop names[i] would be the second item in the list


#Emails
emails = re.findall(r"[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+[a-zA-Z]", txt) #This looks for anything that starts with any upper or lowercase, period, number, or underscore that is followed by an @, that is then followed by the aforementioned criteria, which afterwhich is followed by a period and any character


#Printing
#The following just simply prints the required output
print("Dates:", dates_sorted_2)
print("")
print("Room Names:", room_names_new)
print("")
print("Room Rates:", room_rates)
print("")
print("Names:", names_sorted)
print("")
print("Emails:", emails)
