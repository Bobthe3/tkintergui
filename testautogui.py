import pyautogui as pag

# print(pyautogui.size())

print(pag.position())

# # my computer size 1440(width) by 900(height)
# pyautogui.moveTo(100, 100, duration = 0)

# pag.click(14, 67)

# pag.click(781, 442)
# pag.click(781, 442)
# pag.typewrite(["enter"])
# pag.typewrite("Loppa")
# pag.click(156, 77)
# pag.hotkey("ctrl","s")
# pag.click(473,326)




# pag.moveTo(770,420,duration=1,tween=pag.easeOutElastic)

# f = pag.prompt(text='nice', title='nice22' , default='sfdfg')
# print(f)

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')