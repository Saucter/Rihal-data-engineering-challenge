#Libraries
import re
import datetime
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#OCR
email_image = cv2.imread("email.png")
txt = pytesseract.image_to_string(email_image)

#Dates
print("")
dates = re.findall(r"[0-9]+/[0-9]+/[0-9]+", txt)
dates_sorted_2 = []
num_of_dates = len(dates)
x = 0
while x < num_of_dates:
    dates_2 = datetime.datetime.strptime(dates[x], '%d/%m/%Y')
    dates_sorted = dates_2.strftime('%Y/%m/%d')
    dates_sorted_2.append(dates_sorted)
    x+=1
print("Dates:", dates_sorted_2)
print("")

#Room Names
room_names = re.findall(r"Room:\s\w+", txt)
room_names_new = []
for i in room_names:
    room_names_new.append(i[6:])
print("Room Names:", room_names_new)
print("")

#Room Rates
Room_Rates = re.findall(r"\$[0-9]+", txt)
print("Room Rates:", Room_Rates)
print("")

#Names
names = re.findall(r"[A-Z][a-z]+ \w+, [A-Z][a-z]+|[A-Z][a-z]+, [A-Z][a-z]+", txt)
i = 0
names_sorted = []
num_names = len(names)
while i < num_names:
    names_comma = names[i].replace(",", "")
    names_new = names_comma.split()
    names_new.insert(0, names_new.pop())
    names_new_2 = " ".join(names_new)
    names_sorted.append(names_new_2)
    i += 1
print("Names:", names_sorted)
print("")

#Emails
emails = re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9-_.]+[a-zA-Z]", txt)
print("Emails:", emails)