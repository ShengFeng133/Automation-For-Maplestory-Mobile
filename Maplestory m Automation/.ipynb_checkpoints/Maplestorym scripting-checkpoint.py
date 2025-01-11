import pyautogui
import time
import random

#Global variables
pyautogui.PAUSE = random.uniform(0.5, 0.7)

counter = 0
dimension_invade_clicked = False
guild_clicked = False
mulung_clicked = False
ED_clicked = False 
DD_clicked = False 
task_clicked  = False 

def wait_for_element(image, timeout=360):
    start_time = time.time()
    while time.time() - start_time < timeout:
        element = pyautogui.locateOnScreen(image)
        if element:
            return True
        time.sleep(5)  # Brief sleep to avoid rapid polling
    return False

while not DD_clicked:

    if counter <6 and pyautogui.pixelMatchesColor(634, 281, ((243, 243, 243))):
    pyautogui.click(634, 281)
    counter += 1
    time.sleep(1)

    if not dimension_invade_clicked:
        dimensionInvade_button = pyautogui.locateOnScreen('dimensionInvade_button.png')
        if dimensionInvade_button:
                pyautogui.click(pyautogui.center(dimensionInvade_button))
                pyautogui.click(pyautogui.center('quickpartysearch_button.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
                if wait_for_element('exit.png'):
                    pyautogui.click(pyautogui.locateCenterOnScreen('exit.png'))
                    dimension_invade_clicked = True

                time.sleep(1)

    elif not guild_clicked:
        guild_button = pyautogui.locateOnScreen('guild_button.png')
        if guild_button:
                pyautogui.click(pyautogui.center(guild_button))
                pyautogui.click(pyautogui.center('guildDungeon.png'))
                pyautogui.click(pyautogui.center('claimGuildReward.png'))  
                pyautogui.click(pyautogui.center('enter.png'))
                if wait_for_element('exit.png'):
                    pyautogui.click(pyautogui.locateCenterOnScreen('exit.png'))
                    guild_clicked = True

                time.sleep(1)
    
    elif not mulung_clicked:
        mulung_button = pyautogui.locateOnScreen('mulung_button.png')
        if mulung_button:
                pyautogui.click(pyautogui.center(mulung_button))
                pyautogui.click(pyautogui.center('enter.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
                if wait_for_element('exit.png'):
                    pyautogui.click(pyautogui.locateCenterOnScreen('exit.png'))
                    mulung_clicked = True

                time.sleep(1)

    elif not ED_clicked:
        pyautogui.click(pyautogui.center('quickpartysearch_button.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
        if wait_for_element('goToMenu.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('goToMenu.png'))

        pyautogui.click(pyautogui.locateCenterOnScreen('normalED_button.png'))
        pyautogui.click(pyautogui.center('quickpartysearch_button.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
        if wait_for_element('exit.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('exit.png'))
            ED_clicked = True`

        time.sleep(1)

    else not DD_clicked:
        pyautogui.click(pyautogui.center('enter.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
        if wait_for_element('goToMenu.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('goToMenu.png'))

        pyautogui.click(pyautogui.locateCenterOnScreen('normalDD_button.png'))
        pyautogui.click(pyautogui.center('enter.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
        if wait_for_element('exit.png'):
            pyautogui.click(pyautogui.locateCenterOnScreen('goToMenu.png'))
            DD_clicked = True

        time.sleep(1)


if not task_clicked:
        if pyautogui.pixelMatchesColor(1204, 226, (66, 166, 234)):
            pyautogui.click(1204, 226)
            pyautogui.click(pyautogui.locateCenterOnScreen('getAll.png'))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm_button.png'))
            pyautogui.click(pyautogui.locateCenterOnScreen('cross.png'))

            task_clicked = True  
            time.sleep(1) 
