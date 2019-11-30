'''
This python file is to make whatsapp text.
'''
#!/python3.6

from selenium import webdriver
from platform import system
from time import sleep
import os

def inter():
    try:
        #? Get the current directory and checks for platform
        #! Currently Linux and Windows ---> if changed also modify chromedrive 
        path=os.path.join(os.getcwd(),'chromedriver')
        if system() == 'Linux':
            path=os.path.join(path,'linux')
        else:
            path=os.path.join(path,'win.exe')
        return path
    except Exception as e:
        print(e)
        exit()

driver=webdriver.Chrome(executable_path=inter())
# TODO: If not working 'body' and 'button' has to change
# For 'body': select full xpath from input element
# For 'button': select full xpath of send button. Note that enter a text in input element to make button visible.
body='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
button='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button'

def screenshort():
    #? It for screenshot
    print("Enter The Name: ")
    filename=input("Enter: ")
    driver.save_screenshot(filename+'.png')
    print("DONE")

def textLoop():
    text=str(input("Enter The Text: "))
    n=int(input("Enter Number Of Time: "))
    delay=float(input("Enter Delay(in seconds): "))
    for _ in range(n):
        driver.find_element_by_xpath(body).send_keys(text)
        driver.find_element_by_xpath(button).click()
        sleep(delay)

def langPlay():
    pass

def whatsapp():
    print("The browser is started.....")
    driver.get('https://web.whatsapp.com/')
    print('''
    You here means browser running perfectly without any error.
    Scan the bar code with your whatsapp barcode scanner to link your account.
    Unless you do the step above script will not work.
    If did it than wait for few seconds as javascript is loading in the browser.
    Press Enter to continue.
    ''')
    input()
    while(True):
        # TODO: To be included
        # Text triangle
        #? Text loop
        #? Screenshort
        # Scrapy inputs
        print('''
        Select the contact where you want do fun.
        OPTIONS:
            1> Text Looping 
            2> Screenshort
            3> Langauge Play
            4> Exit
        ''')
        choice=int(input("\tEnter: "))
        if choice == 1:
            textLoop()
        elif choice == 2:
            screenshort()
        elif choice == 3:
            pass
        elif choice == 4:
            driver.quit()
            exit()
        else:
            print("Invalid Input")


if __name__=='__main__':
    whatsapp()