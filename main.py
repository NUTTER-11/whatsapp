import pyautogui
import webbrowser as wb
import time
import pywhatkit


def sendtimestampmsg():
    wb.open("https://web.whatsapp.com/")
    pywhatkit.sendwhatmsg('enter_your_mobile_no','enter_your name', 22, 12)


def spam100():
    wb.open("https://web.whatsapp.com/")
    time.sleep(20)
    for i in range(100):

        pyautogui.typewrite("hi")
        pyautogui.press("i")
        pyautogui.press("enter")


if __name__ == '__main__':
    spam100().run()
    sendtimestampmsg().run()
