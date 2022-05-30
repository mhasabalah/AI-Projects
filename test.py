import pyautogui

while True:
    message = pyautogui.confirm(text='Are you Dump?', title='Confirm', buttons=['Yes', 'No'])
    if message == 'Yes':
        print('Yes')
        break