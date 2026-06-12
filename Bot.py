
import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE"  # your key here
)

def is_last_message_from_sender(chat_log, sender_name="~월식 🌙"):
    messages = chat_log.strip().split("/2026]") [-1]
    if sender_name in messages:
        return True
    return False

pyautogui.keyDown('shift')
time.sleep(2)
pyautogui.click(1464, 900)
pyautogui.keyUp('shift')
time.sleep(2)

pyautogui.click(1344, 1054)
time.sleep(2)
while True:


    pyautogui.moveTo(605, 137)
    pyautogui.dragTo(1846, 946, duration=1.0, button='left')


    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1497, 934)

    chat_history = pyperclip.paste()

    print(chat_history)
    
    
    if is_last_message_from_sender(chat_history):

     completion = client.chat.completions.create(
         model="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a person named soumyadeep who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and respond like soumyadeep. Output should be the next chat response as soumyadeep"},
            {"role": "user", "content": chat_history}
         ]
     )

     response = completion.choices[0].message.content

     pyperclip.copy(response)
     time.sleep(2)

     pyautogui.click(1609, 974)
     time.sleep(1)

     pyautogui.hotkey('ctrl', 'v')
     time.sleep(1)

     pyautogui.press('enter')

