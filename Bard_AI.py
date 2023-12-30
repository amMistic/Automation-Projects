# accessing Bard A.I.

from bardapi import BardCookies
import datetime
import webbrowser
from time import sleep
import pyautogui
import keyboard
import pyperclip
import json

# chorme_exe_path = "D:\python\chromedriver-win64\chromedriver.exe"


# chrome automation
def chrome_automation(link):
    chrome_path ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(link)


# cookies handling 
def cookieScraper():

    chrome_automation("https://bard.google.com")
    sleep(5)
    pyautogui.click(x=1214, y=59)
    sleep(2)
    pyautogui.click(x=986, y=304)
    sleep(3)
    pyautogui.click(x=985, y=92)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    # load the copied cookies
    data = pyperclip.paste()

    # json file
    try:
        json_data = json.loads(data)
        print("*** The Cookies Loaded Successfully ***")
        pass
    
    except Exception as e:
        print("*** Cookies Load Unsuccessful ***")
        
    SID = "__Secure-1PSID"
    SIDTS = "__Secure-1PSIDTS"
    SIDCC = "__Secure-1PSIDCC"

    
    try :
            # Iterate throught the json file to scrap the values of cookies
            SIDValue = next((item for item in json_data if item['name'] == SID),None)
            SIDTSValue = next((item for item in json_data if item['name'] == SIDTS),None)
            SIDCCValue = next((item for item in json_data if item['name'] == SIDCC),None)

            # error handling
            if SIDValue is not None:
                SIDValue = SIDValue['value']
            else:
                print("__Secure-1PSID  values is not founded")

            if SIDTSValue is not None:
                SIDTSValue = SIDTSValue['value']
            else:
                print("__Secure-1PSIDTS values is not founded")

            if SIDCCValue is not None:
                SIDCCValue = SIDCCValue['value']
            else:
                print("__Secure-1PSIDCC values is not founded")

            # Displaying the cookies valuse
            print("")
            print(f"===> Cookie 1 - {SIDValue}")
            print(f"===> Cookie 2 - {SIDTSValue}")
            print(f"===> Cookie 3 - {SIDCCValue}")
            print("")

    except Exception as e :
        print(e)
    
    # Store the cookies value in the dictionary along with their respective keys
    cookies_dict = {
        "__Secure-1PSID" : SIDValue,
        "__Secure-1PSIDTS" : SIDTSValue,
        "__Secure-1PSIDCC" : SIDCCValue
    }
    
    return cookies_dict


# main execution
def Conversation(bard):

    print("start your conversation..")
    
    while True:

        query  = str(input("Enter Query Here:"))

        if "exit" in query:
            exit()

        # check for automated tasks
        with open('D:\Automation\CurrentChat.txt','w') as file:
            file.write(query)
        
        try:

            # current conversation chat
            file = open('D:\Automation\CurrentChat.txt','r')
            data = file.read()  
            file.close()

            # history of conversation chat
            file_hist = open('D:\Automation\histChat.txt', 'r')
            data_hist = file_hist.read() 
            file.close()
            if str(data) ==  str(data_hist):
                sleep(0.5)
                pass
            
            else:  
                real_query = str(data)
                print("\nResponse:")
                results = bard.get_answer(real_query)['content']
                current_time = datetime.datetime.now()
                format_time = current_time.strftime("%H%M%S")
                filenamedate = str(format_time) + str(".txt")
                Response = "D:\Automation\Database\\" + filenamedate
                with open (Response , 'w') as file:
                    file.write(results)
                print(results)  

                # add the recent conversation into the history chat
                file_hist = open('D:\Automation\histChat.txt', 'w')
                file_hist.write(data)
                file_hist.close()

        except Exception as e:
            print("Error Founded!!")
            print(f"Fixed the Error:{e}")
            pass


# Automating the Bard Ai
def bardAI():

    # seting up the cookies of the BardAPI
    cookies_dict = cookieScraper()

    # create the instance of the instance of BardCookies
    bard = BardCookies(cookie_dict=cookies_dict)

    # Calling Conversation Function
    Conversation(bard)


if __name__ == "__main__":

    # accessing Automate Bard
    bardAI()