import pyautogui
from time import sleep
import webbrowser

# Pre-requirements:
'''
user must have the "Edit this cookie" extension in chrome 
'''

# open Bard Ai website
webbrowser.open("https://bard.google.com")

#Step 1: to get the location for extension button
sleep(5)  # to let the website fully load 
extension = pyautogui.position()   # place the cursor on the extesion key on chrome browser for 5 sec.
print(f"Extension Location: {extension}")


# Step 2: to get the location of "Edit the cookie" extension within the extension list
sleep(5)
Edit_the_cookie = pyautogui.position()  # after 5 sec completed, click on the extension button , and then place the cursor over the "Edit the cookie" extension key to get the location of that key on the screen

print(f"'Edit this Cookie' extension location:{Edit_the_cookie}")


#Step 3 : to get the Export button within the "Edit The Cookie" extension
sleep(5)
Export = pyautogui.position()  # after 5 sec complete, click the "Edit the Cookie" extension and place the cursor over the "Export" button
print(f"Export Button Location: {Export}")


#NOTE: Make sure to perform this function one by one ; to get the accurate location of each of the following things required
# then place this value into the "cookieScraper" function in Bard_Ai.py file to make it run properly