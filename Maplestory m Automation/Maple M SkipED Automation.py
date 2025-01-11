#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui
import time
import random
import cv2
import os
from datetime import datetime
import asyncio



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


# In[ ]:


#DI -> Guild Dungeon -> ED * 2 -> CDD & Normal DD-> Collect Task Rewards -> Home System Collect AB -> Arcane * 5 -> Do CDD for 9 chars, in addition 
#for the first 4 chars, do ED as well. 

#Tangyoon OTOT, I didn't implement.  
#Mulung is implemented initially, but I realised I want to do it manually instead, so I commented out the Mulung part. If you want to auto-Mulung, 
#just uncomment that section of the code. 

async def wait_for_element(image, timeout= 600, confidence = 0.5):
    start_time = time.time()
    while time.time() - start_time < timeout: 
        try: 
            element = pyautogui.locateOnScreen(image, confidence = confidence)
            if element:
                return True
        except:
            print(f"Still checking for {image}")
            pass
            
        await asyncio.sleep(3) 
    return False

def wait_for_pixel_color(x, y, color, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.pixelMatchesColor(x, y, color):
            return True
        time.sleep(3)  # Brief sleep to avoid rapid polling
    return False

async def check_for_banner():
    while True:
        try: 
            banner = pyautogui.locateOnScreen('crossAdver.png', confidence=0.7)
            if banner:
                pyautogui.click(pyautogui.center(banner))
                print("Banner closed")
        except: 
            pass
        await asyncio.sleep(5)  # Pause briefly before checking again


async def check_confirmMiniDungeon():
    if await wait_for_element('confirmMiniDungeon.png', timeout=600, confidence=0.8):
        pyautogui.click(pyautogui.locateCenterOnScreen('confirmMiniDungeon.png', confidence=0.8))

async def check_exitMiniDungeon():
    if await wait_for_element('exitMiniDungeon.png', timeout=600, confidence=0.8):
        pyautogui.click(pyautogui.locateCenterOnScreen('exitMiniDungeon.png', confidence=0.8))

async def main_task():
    #Declaring variables
    counter = 0
    dimension_invade_clicked = False
    guild_clicked = False
    mulung_clicked = False
    ED_clicked = False
    DD_clicked = False
    DailyHunt = False
    Task_clicked  = False
    home_clicked = False
    arcane_clicked = False
    cdd_finished = False

    while not cdd_finished:

        if counter == 0:
            x = 0
            while (x < 2): 
                pyautogui.moveTo(1421, 521) 
                pyautogui.dragTo(1706, 517, 0.5, button='left')
                if x == 0: 
                    #Change character preset from 1 to 2 
                    pyautogui.click(1419, 508)
                    pyautogui.click(1524, 416)
                x += 1
                
            #Use nearest scroll, doesn't matter if in AF maps or in the Town already. 
            pyautogui.click(1631, 511)
    
            #Sometimes the banner for monthly attendance and advertisement comes out 
            if await wait_for_element(image='cross.png', timeout = 4, confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.7))
            if await wait_for_element(image='crossAdver.png', timeout = 2, confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('crossAdver.png', confidence = 0.7))

    
        #Here clicks on dungeon icon in each iteration, for a total of 4 times, to allow DI -> GD -> ED -> DD -> Daily Hunt. 
        #counter will run from counter = 0 to counter = 4, total 5 iterations. 
        if counter <5 and pyautogui.pixelMatchesColor(1270, 91, (255, 255, 255)): 
            
            pyautogui.click(1270, 91)
            print(counter)
            
    
        #DI -> party search -> confirm -> program waits for DI to run finish and search for exit button 
        if not dimension_invade_clicked:
            dimensionInvade_button = pyautogui.locateOnScreen('dimensionInvade_button.png', confidence = 0.7)
            pyautogui.click(pyautogui.center(dimensionInvade_button))
            pyautogui.click(pyautogui.locateOnScreen('quickPartySearch.png',  confidence = 0.7))
            pyautogui.click(pyautogui.locateOnScreen('confirm.png', confidence = 0.7))
            
            if await wait_for_element('exit.png', confidence = 0.7):
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
                if await wait_for_element('exit.png', confidence = 0.7):
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
            
            if await wait_for_element('goToMenuED.png', confidence = 0.75):
                pyautogui.click(pyautogui.locateCenterOnScreen('goToMenuED.png', confidence = 0.75))
            
            pyautogui.click(pyautogui.locateCenterOnScreen('normalED.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('quickPartySearch.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
            if await wait_for_element('exitED.png', confidence = 0.7):
                pyautogui.click(pyautogui.locateOnScreen('exitED.png', confidence = 0.7))
                ED_clicked = True
                counter += 1
                print("ED Finished")
    
    
            
        #CDD and if Monday-Thu, normalDDTicketCount == 4, Fri-Sun select purple jewel and max tickets. 
        elif not DD_clicked:
            DD_button = pyautogui.locateOnScreen('DD.png', confidence = 0.7)
            pyautogui.click(pyautogui.center(DD_button))
            
            pyautogui.click(pyautogui.locateCenterOnScreen('enterDD.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
            
            if await wait_for_element('goToMenuDD.png', confidence = 0.7):
                pyautogui.click(pyautogui.locateCenterOnScreen('goToMenuDD.png', confidence = 0.7))
                
            today = datetime.today()
            day_of_week = today.strftime("%A")
            print(day_of_week)
            
            pyautogui.click(pyautogui.locateCenterOnScreen('NormalDDSelection.png', confidence = 0.8))
            
            if (day_of_week in ["Friday", "Saturday", "Sunday"]):
                pyautogui.click(pyautogui.locateCenterOnScreen('Friday.png', confidence = 0.7))
    
            pyautogui.click(pyautogui.locateCenterOnScreen('Option2.png', confidence = 0.9))
            pyautogui.click(pyautogui.locateCenterOnScreen('enterNormalDD.png', confidence = 0.7))
            
            if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday"]: 
                pyautogui.click(pyautogui.locateCenterOnScreen('Decrement.png', confidence = 0.9), clicks = 8, interval = 0.5)
                pyautogui.click(pyautogui.locateCenterOnScreen('Increment.png', confidence = 0.9), clicks = 4, interval = 0.5)
            pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
            
            
            if await wait_for_element('exit.png', confidence = 0.7):
                pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))
            
                DD_clicked = True 
                counter += 1
                print("DD Finished")

            pyautogui.click(657, 917) #Open up AB window
            pyautogui.click(clicks = 2, interval = 0.5, x=1003, y=444) #Load 2x 10min AB 
            pyautogui.click(pyautogui.locateOnScreen('cross.png',  confidence = 0.7))

        elif not DailyHunt: 
            
            
            miniDungeon_button = pyautogui.locateOnScreen('miniDungeon.png', confidence = 0.7)
            pyautogui.click(pyautogui.center(miniDungeon_button))
            pyautogui.click(pyautogui.locateCenterOnScreen('monsterAutoSelect.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('enterMiniDungeon1.png', confidence = 0.7))
            # if await wait_for_element('autoProceedNextStage.png', timeout = 3, confidence = 0.7):
            #     pyautogui.click(pyautogui.locateCenterOnScreen('autoProceedNextStage.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('enterMiniDungeon2.png', confidence = 0.7))
            if await wait_for_element(image='cross.png', timeout = 5, confidence=0.7): 
                pyautogui.click(pyautogui.locateCenterOnScreen('cross.png', confidence = 0.7))


            # await asyncio.gather(check_confirmMiniDungeon(), check_exitMiniDungeon())

            
            if await wait_for_element('exitMiniDungeon.png', timeout = 600, confidence = 0.8):
                pyautogui.click(pyautogui.locateCenterOnScreen('exitMiniDungeon.png', confidence = 0.8))            
            if await wait_for_element('confirmMiniDungeon.png', timeout = 600, confidence = 0.8):
                pyautogui.click(pyautogui.locateCenterOnScreen('confirmMiniDungeon.png', confidence = 0.8))
            
            DailyHunt = True
            counter += 1
            print("Daily Hunt Finished")
                   
            
        #Collect Task Rewards 
        elif not Task_clicked:
            pyautogui.click(1185, 77)
    
            for i in range(2):
                pyautogui.click(pyautogui.locateCenterOnScreen('getAll.png', confidence = 0.7))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirmTask.png', confidence = 0.7))

            pyautogui.click(245, 457)
            pyautogui.click(pyautogui.locateCenterOnScreen('getAllDailyHunt.png', confidence = 0.7))
            pyautogui.click(pyautogui.locateCenterOnScreen('confirmDailyHunt.png', confidence = 0.7))           
    
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
    
        #Arcane Dailies * 5
        elif not arcane_clicked: 
            arcaneCount = 0 
            while arcaneCount < 4: #so arcaneCount runs from 0 to 3, total 5 iterations: 0,1,2,3
    
                print("Arcane Count:", arcaneCount)
    
                #What I'm doing below is before start of dailies, assuming the 4 slots (for inserting pots) are alr at default, drag once and change 
                #char preset to preset 2, then drag once more and use nearest scroll. 
                #I'm just changing char preset for my own use, if don't need can delete/comment out the code. 
                        
                #Clicking on arcane dailies
                pyautogui.click(193, 315)
                if arcaneCount != 0: 
                    if await wait_for_element(image='goNow.png', timeout = 5, confidence=0.7): 
                        pyautogui.click(pyautogui.locateCenterOnScreen('goNow.png', confidence = 0.7))
              
                    
                if await wait_for_element(image='skip.png', confidence=0.7): 
                    pyautogui.click(pyautogui.locateCenterOnScreen('skip.png', confidence = 0.7))
                pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
                if await wait_for_element(image='returnToTown.png', confidence=0.7): 
                    pyautogui.click(pyautogui.locateCenterOnScreen('returnToTown.png', confidence = 0.7))
    
                #When arcane dailies have been completed, set back char preset to 1, drag once more to default slots.
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
    
            #Loading 4 positions into the array, so at the changing char page, it can select 4 different positions, top left, top right, btm left, 
            #btm right corresponding to 4 diff. chars. 
            positions = [(783,489), (1327, 486), (761,640), (1354, 641)] 
            
            while cddCount < 10: #cdd runs from cddCount = 1 to cddCount = 9, so total 9 iterations. 
    
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
                        pyautogui.dragTo(969, 154, 1.8, button='left')
                    
                x, y = positions[(cddCount - 1) % 4]  # Modulo 4 to repeat positions
                pyautogui.click(x, y)
                pyautogui.click(pyautogui.locateCenterOnScreen('changeChar.png', confidence = 0.7))
    
                #Here's for alts that have been left to finish AB prev., confirm button would pop up.  
                if await wait_for_element('confirm.png', timeout = 8, confidence = 0.7):
                    pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))
    
                #Click on dungeon icon 
                if wait_for_pixel_color(1270, 91, (255, 255, 255)):
                    pyautogui.click(1270, 91)
                DD_button = pyautogui.locateOnScreen('DD.png', confidence = 0.7)
                pyautogui.click(pyautogui.center(DD_button))
                pyautogui.click(pyautogui.locateCenterOnScreen('enterDD.png', confidence = 0.7)) 
                pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence = 0.7))
                if await wait_for_element('exit.png', confidence = 0.7):
                    pyautogui.click(pyautogui.locateCenterOnScreen('exit.png', confidence = 0.7))
            
                
                    
                    
                cddCount += 1
                
            cdd_finished = True 

async def main():
    await asyncio.gather(
        check_for_banner(), 
        main_task()
    )        

time.sleep(3)
if __name__ == "__main__":
    asyncio.run(main())


        

