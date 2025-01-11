#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui
import time
import random
import cv2
import os

current_directory = os.getcwd()
print(current_directory)

#Declare Global variables
pyautogui.PAUSE = 3 #This line makes sure after each click, the program pauses for 3 seconds. Why? Sometimes the computer system lags, so to have
#enough buffer time before the program execute next line of code. 
counter = 0
dimension_invade_clicked = False
guild_clicked = False
mulung_clicked = False
ED_clicked = False
DD_clicked = False
Task_clicked  = False 
home_clicked = False
arcane_clicked = False
cdd_finished = False


# In[3]:


#DI -> Guild Dungeon -> Mulung -> ED * 2 -> CDD -> Collect Task Rewards -> Home System Collect AB -> Arcane * 4 -> Do CDD for 9 chars, in addition 
#for first 4 char, do ED as well. 

#DD & Tangyoon ownself OTOT, I didn't implement.  

def wait_for_element(image, timeout= 600, confidence = 0.5):
    start_time = time.time()
    while time.time() - start_time < timeout: 
        try: 
            element = pyautogui.locateOnScreen(image, confidence = confidence)
            if element:
                return True
        except:
            print(f"Still checking for {image}")
            pass
            
        time.sleep(3)  
    return False

def wait_for_pixel_color(x, y, color, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.pixelMatchesColor(x, y, color):
            return True
        time.sleep(3)  # Brief sleep to avoid rapid polling
    return False

#Time imposed here to allow time (3 seconds) to switch to the right window before running the program
time.sleep(3)

while not cdd_finished:

    #Here clicks on dungeon icon in each iteration, for a total of 5 times e.g. dungeon icon -> DI complete -> exit -> main screen -> dungeon icon ...  
    if counter <4 and pyautogui.pixelMatchesColor(1270, 91, (255, 255, 255)): 
        pyautogui.click(1270, 91)
        print(counter)
        

    #DI -> party search -> confirm -> program waits for DI to run finish and search for exit button 
    if not dimension_invade_clicked:
        dimensionInvade_button = pyautogui.locateOnScreen('dimensionInvade_button.png', confidence = 0.7)
        pyautogui.click(pyautogui.center(dimensionInvade_button))
        pyautogui.click(pyautogui.locateOnScreen('quickPartySearch.png',  confidence = 0.7))
        pyautogui.click(pyautogui.locateOnScreen('confirm.png', confidence = 0.7))
        
        if wait_for_element('exit.png', confidence = 0.7):
            pyautogui.click(pyautogui.locateOnScreen('exit.png', confidence = 0.7))
            dimension_invade_clicked = True
            counter += 1
            print("DI Finished")


            
    #guild button -> guildDungeon -> claim guild reward, if don't have e.g. claim guild reward button is greyed, then will skip through the line of 
    #code without breaking the whole program -> enter -> wait for it to finish and click on exit button
    elif not guild_clicked:
        guild_button = pyautogui.locateOnScreen('guild_button.png', confidence = 0.7)
        if guild_button:

            pyautogui.click(pyautogui.center(guild_button))
            pyautogui.click(pyautogui.locateOnScreen('guildDungeon.png', confidence = 0.7))
            try:
                claim_guild_reward = pyautogui.locateOnScreen('claimGuildReward.png', confidence=0.7)
                if claim_guild_reward:
                    pyautogui.click(pyautogui.center(claim_guild_reward))
                else:
                    print("Image not found")
            except Exception as e:
                print(f"An error occurred: {e}")  
            pyautogui.click(pyautogui.locateOnScreen('entergd.png', confidence = 0.7))
            if wait_for_element('exit.png', confidence = 0.7):
                pyautogui.click(pyautogui.locateOnScreen('exit.png', confidence = 0.7))
                guild_clicked = True
                counter += 1
                print("GD Finished")


            
    #mulung -> search for confirm button for weekly rewards at start of the week, for 3 seconds as mentioned at timeout = 3, can modify if u want ->
    #enter -> confirm -> exit 
    
    # elif not mulung_clicked:
    #     mulung_button = pyautogui.locateOnScreen('mulung.png', confidence = 0.7)
    #     if mulung_button:
    #         pyautogui.click(pyautogui.center(mulung_button))
    #         if wait_for_element('confirmMulungWeeklyRewards.png', timeout = 3, confidence = 0.8):
    #             pyautogui.click(pyautogui.locateOnScreen('confirmMulungWeeklyRewards.png', confidence = 0.8))
    #         pyautogui.click(pyautogui.locateCenterOnScreen('enterMulung.png', confidence = 0.7))
    #         pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
    #         if wait_for_element('exitMulung.png', confidence = 0.7):
    #             pyautogui.click(pyautogui.locateOnScreen('exitMulung.png', confidence = 0.7))
    #             mulung_clicked = True
    #             counter += 1
    #             print("Mulung Finished")


    #Chaos ED then followed by normal ED             
    elif not ED_clicked:
        ed_button = pyautogui.locateOnScreen('ed_button.png', confidence = 0.7)
        pyautogui.click(pyautogui.center(ed_button))
        pyautogui.click(pyautogui.locateCenterOnScreen('quickPartySearch.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
        
        if wait_for_element('goToMenuED.png', confidence = 0.75):
            pyautogui.click(pyautogui.locateCenterOnScreen('goToMenuED.png', confidence = 0.75))
        
        pyautogui.click(pyautogui.locateCenterOnScreen('normalED.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('quickPartySearch.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
        if wait_for_element('exitED.png', confidence = 0.7):
            pyautogui.click(pyautogui.locateOnScreen('exitED.png', confidence = 0.7))
            ED_clicked = True
            counter += 1
            print("ED Finished")


        
    #Do CDD only on my main
    elif not DD_clicked:
        DD_button = pyautogui.locateOnScreen('DD.png', confidence = 0.7)
        pyautogui.click(pyautogui.center(DD_button))
        
        pyautogui.click(pyautogui.locateCenterOnScreen('enterDD.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
        
        if wait_for_element('exit.png', confidence = 0.7):
            pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))
            DD_clicked = True 
            counter += 1
            print("DD Finished")

        

    #Collect Task Rewards 
    elif not Task_clicked:
        pyautogui.click(1185, 77)

        pyautogui.click(pyautogui.locateCenterOnScreen('getAll.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirmTask.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('getAll.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('confirmTask.png', confidence = 0.7))
        pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.5))

        Task_clicked = True  
        print("Task Finished")

    #Home system collect ABs 
    elif not home_clicked:  
        pyautogui.click(1756, 84)
        pyautogui.moveTo(1407,680)
        pyautogui.dragTo(1653, 271, 1, button='left')
        pyautogui.click(pyautogui.locateCenterOnScreen('home.png', confidence = 0.7))
        pyautogui.click(clicks = 5, interval = 0.5, x=1636, y=323) 
        pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.7))
        pyautogui.click(889, 519)
        home_clicked = True
        print("Home finished")

    #Arcane Dailies * 4 
    elif not arcane_clicked: 
        arcaneCount = 0 
        while arcaneCount < 4: 

            print("Arcane Count:", arcaneCount)

            #What I'm doing below is before start of dailies, assuming the 4 slots (for inserting pots) are alr at default, drag once and change 
            #char preset to preset 2, then drag once more. 
            #I'm just changing char preset for my own use, if don't need can delete the code. 

            if arcaneCount == 0:
                x = 0
                while (x < 2): 
                    pyautogui.moveTo(1421, 521) 
                    pyautogui.dragTo(1706, 517, 0.5, button='left')
                    if x == 0: 
                        #Change character preset 
                        pyautogui.click(1419, 508)
                        pyautogui.click(1524, 416)
                    x += 1
                    
                #Use nearest scroll, doesn't matter if in AF maps or in the Town already. 
                pyautogui.click(1631, 511)

                #Sometimes the banner for monthly attendance and advertisement comes out 
                if wait_for_element(image='cross.png', timeout = 4, confidence=0.7): 
                    pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.7))
                if wait_for_element(image='crossAdver.png', timeout = 2, confidence=0.7): 
                    pyautogui.click(pyautogui.locateCenterOnScreen('crossAdver.png', confidence = 0.7))
                    
            #Clicking on arcane dailies
            pyautogui.click(193, 315)
            if wait_for_element(image='goNow.png', timeout = 5, confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('goNow.png', confidence = 0.7))
          
                
            if wait_for_element(image='skip.png', confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('skip.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
            if wait_for_element(image='returnToTown.png', confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('returnToTown.png', confidence = 0.7))

            #When arcane dailies have been completed, drag back the slots, change back char preset to 1, drag once more to default slots.
            if arcaneCount == 3:
                x = 0
                while (x < 2): 
                    pyautogui.moveTo(1744, 521) 
                    pyautogui.dragTo(1418, 550, 0.5, button='left')
                    if x == 0: 
                        pyautogui.click(1419, 508)
                        pyautogui.click(1426, 401)
        
                    x += 1
                            
        
            arcaneCount += 1
            
        arcane_clicked = True 
        print("Arcane finished")

    #Do CDD for 9 chars 
    elif not cdd_finished: 
        cddCount = 1

        #Loading 4 positions into the array, so during the changing char page, it can select 4 different positions, top left, top right, btm left, 
        #btm right
        positions = [(783,489), (1327, 486), (761,640), (1354, 641)] 
        
        while cddCount < 10: 

            print("CDD Count:", cddCount)

            #Open up menu and change char icon 
            pyautogui.click(1756, 84)
            pyautogui.click(1592, 934)

            #This is for mouse drag. When cdd has been done on 4 characters, to do cdd for next 4 chars, drag the screen up once, to do cdd for the 
            #next 4 char after 8 char, drag the screen up twice etc. 
            if cddCount >= 5:
                group = (cddCount - 5) // 4  # This will group 1-4, 5–8, 9–12, etc.
                repeat_count = group + 1
        
                for _ in range(repeat_count):
                    pyautogui.moveTo(783, 489) 
                    pyautogui.dragTo(969, 154, 1, button='left')
                
            x, y = positions[(cddCount - 1) % 4]  # Modulo 4 to repeat positions
            pyautogui.click(x, y)
            pyautogui.click(pyautogui.locateCenterOnScreen('changeChar.png', confidence = 0.7))

            #Here's for alts that have been left to finish AB prev., confirm button would pop up. Without this code, the program would stop/ break. 
            if wait_for_element('confirm.png', timeout = 8, confidence = 0.7):
                pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))

            #Click on dungeon icon 
            if wait_for_pixel_color(1270, 91, (255, 255, 255)):
                pyautogui.click(1270, 91)
            DD_button = pyautogui.locateOnScreen('DD.png', confidence = 0.7)
            pyautogui.click(pyautogui.center(DD_button))
            pyautogui.click(pyautogui.locateCenterOnScreen('enterDD.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
            if wait_for_element('exit.png', confidence = 0.7):
                pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))
        
            #Running ED on first 4 alts 
            if cddCount < 5: 
                if wait_for_pixel_color(1270, 91, (255, 255, 255)):
                    pyautogui.click(1270, 91)
                
                
                    
                ed_button = pyautogui.locateOnScreen('ed_button.png', confidence = 0.7)
                pyautogui.click(pyautogui.center(ed_button))
                if cddCount == 1:
                    pyautogui.click(pyautogui.locateCenterOnScreen('normalED.png', confidence = 0.7))
                    
                pyautogui.click(pyautogui.locateCenterOnScreen('quickPartySearch.png', confidence = 0.7))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
                if wait_for_element('exitED.png', confidence = 0.7):
                    pyautogui.click(pyautogui.locateOnScreen('exitED.png', confidence = 0.7))
                time.sleep(1)
                pyautogui.click(1185, 77)
                pyautogui.click(pyautogui.locateCenterOnScreen('getAll.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirmTask.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.7))
                
                
            cddCount += 1
            
        cdd_finished = True 

    

