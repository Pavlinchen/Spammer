import time as t
from pyautogui import press, typewrite, click

Spam_Text = input("What message do you want to send? ")
TIMES = int(input("How many times do you want to send it? "))

print("You have 5 seconds to enter the chat with your cursor")
print("Press CTRL + C to cancel")
t.sleep(5)

for step in range(TIMES):
    typewrite(Spam_Text)
    press("enter")
    print("sent message number", step + 1)

print("\nDone!")
print("you have sent", Spam_Text, TIMES, "times!")
t.sleep(3)