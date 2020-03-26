
import pyautogui
pyautogui.locateOnScreen("full.JPG")

import clipboard
# clipboard.copy("abc")  # now the clipboard content will be string "abc"

def reset():
    pyautogui.click() 
    # pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')

def copyandpaste(pincode):
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c') # ctrl-c to copy
    val = clipboard.paste() #pyautogui.hotkey('ctrl', 'v')
    return val

pincodes = range(500139,502350)

pincodes = [str(i) for i in pincodes]

def navigateEachAddress(pincode):
    pyautogui.PAUSE = 0.5
    pyautogui.press('up')
    # pyautogui.PAUSE = 0.5
    # pyautogui.press('enter')
    
for pincode in pincodes:
    reset()
    pyautogui.write(pincode, interval=0.25)

    for i in range(0,25):
        navigateEachAddress(pincode)
        val = copyandpaste(pincode)
        
        if pincode == str(val):
            break
        else:
            print(pincode, "|", str(val))