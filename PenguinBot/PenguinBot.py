"""
Login: PenguinBotPY
Password: Pythonscript160
Split-screen between Python IDE on the right and
Club Penguin window on the left for the program to work.
"""
import pyautogui
import time


def level_completer(key, count):
    for i in range(count):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        print('Pressed {}!'.format(key))


while True:
    pyautogui.click(x=200, y=506)  # Pixel coordinates for Thin Ice controller.
    time.sleep(3)  # Delay for walking animation from penguin position to Thin Ice controller.
    pyautogui.click(x=355, y=436)  # Pixel coordinates for "Yes" button.
    time.sleep(0.25)
    pyautogui.click(x=395, y=621)  # Pixel coordinates for "Start" button.
    time.sleep(0.25)
    pyautogui.click(x=218, y=621)  # Pixel coordinates for "Play" button.
    time.sleep(0.3)

    """ Level One """
    level_completer('left', 12)
    print("Level One Complete!")
    time.sleep(0.25)

    """ Level Two """
    level_completer('right', 4)
    level_completer('down', 2)
    level_completer('up', 2)
    level_completer('right', 4)
    level_completer('up', 2)
    level_completer('down', 2)
    level_completer('right', 4)
    level_completer('up', 3)
    print("Level Two Complete!")
    time.sleep(0.25)

    """ Level Three """
    level_completer('down', 4)
    level_completer('left', 1)
    level_completer('up', 1)
    level_completer('left', 3)
    level_completer('down', 1)
    level_completer('left', 1)
    level_completer('up', 1)
    level_completer('left', 2)
    level_completer('up', 1)
    level_completer('left', 1)
    level_completer('down', 1)
    level_completer('left', 2)
    level_completer('down', 1)
    level_completer('left', 1)
    level_completer('up', 4)
    print("Level Three Complete!")
    time.sleep(0.25)

    """ Level Four """
    level_completer('up', 4)
    level_completer('left', 1)
    level_completer('up', 2)
    level_completer('right', 2)
    level_completer('down', 2)
    level_completer('right', 3)
    level_completer('up', 1)
    level_completer('right', 1)
    level_completer('down', 3)
    level_completer('left', 1)
    level_completer('down', 1)
    level_completer('right', 3)
    level_completer('up', 1)
    level_completer('left', 1)
    level_completer('up', 3)
    level_completer('right', 1)
    level_completer('down', 1)
    level_completer('right', 3)
    level_completer('up', 2)
    level_completer('right', 2)
    level_completer('down', 2)
    level_completer('left', 1)
    level_completer('down', 4)
    print("Level Four Complete!")
    time.sleep(0.25)

    """ Level Five """
    level_completer('down', 2)
    level_completer('left', 9)
    level_completer('down', 1)
    level_completer('right', 10)
    level_completer('up', 1)
    level_completer('right', 1)
    level_completer('down', 2)
    level_completer('left', 12)
    level_completer('up', 1)
    level_completer('left', 2)
    print("Level Five Complete!")

    """ Exit and Restart """
    pyautogui.mouseDown(button='left', x=626, y=757)  # Pixel coordinates for left scroll button.
    time.sleep(1.25)
    pyautogui.mouseUp()
    pyautogui.click(x=368, y=245)  # Pixel coordinates for first exit button.
    time.sleep(0.25)
    pyautogui.click(x=222, y=275)  # Pixel coordinates for second exit button.
    print("Restarting...")
    pyautogui.mouseDown(button='left', x=14, y=757)  # Pixel coordinates for right scroll button.
    time.sleep(1.25)
    pyautogui.mouseUp()
