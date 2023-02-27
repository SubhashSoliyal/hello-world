#  Healthy programmer

# 9am - 5pm
# water - water.mp3 (3.5 litres) - drank - log, 18 glass of water
# Eyes - eyes.mp3 - EyDone, every 30 min - log
# physical activity - physical.mp3 ,every - 45 min ExDone-  log

# rules 
# pygame module to play audio


import pygame
import time

initial_time = time.time()
localTime = time.asctime(time.localtime(time.time()))
file = open('data_of_All_day_work.txt','a')


def Water():
    Water = 'water.mp3'
    pygame.init()
    pygame.mixer.music.load(filename= Water)
    pygame.mixer.music.play()

    input_done = input("Enter 'drank' If you drank water: ")
    if input_done == 'drank':
        pygame.mixer.music.pause()
        file.write("\n\nYou drank water at " + localTime)
        print("\n\nYou drank water at " + localTime)
    else:
        print("sorry I can't understend, Retry")
        input_done = input("Enter 'drank' If you drank water: ")
        if input_done == 'drank':
            pygame.mixer.music.pause()
            file.write("\n\nYou drank water at " + localTime)
            print("\n\nYou drank water at " + localTime)
        
def Eyes():
    Eyes = 'eyes.mp3'
    pygame.init()
    pygame.mixer.music.load(filename= Eyes)
    pygame.mixer.music.play()

    input_done = input("Enter 'EyDone' If you  done eye Excise: ")
    if input_done == 'EyDone':
        pygame.mixer.music.pause()
        file.write("\n\nYou done eye Excise at " + localTime)
        print("\n\nYou done eye Excise at " + localTime)
    else:
        print("sorry I can't understend, Retry")
        input_done = input("Enter 'EyDone' If you  done eye Excise : ")
        if input_done == 'EyDone':
            pygame.mixer.music.pause()
            file.write("\n\nYou done eye Excise at " + localTime)
            print("\n\nYou done eye Excise at " + localTime)

def physical_activity():
    physical = 'physical.mp3'
    pygame.init()
    pygame.mixer.music.load(filename= physical)
    pygame.mixer.music.play()

    input_done = input("Enter 'ExDone' If you  done Physical Excise: ")
    if input_done == 'ExDone':
        pygame.mixer.music.pause()
        file.write("\n\nYou done Physical Excise at " + localTime)
        print("\n\nYou done Physical Excise at " + localTime)
    else:
        print("sorry I can't understend, Retry")
        input_done = input("Enter 'ExDone' If you  done Physical Excise : ")
        if input_done == 'ExDone':
            pygame.mixer.music.pause()
            file.write("\n\nYou done Physical Excise at " + localTime)
            print("\n\nYou done Physical Excise at " + localTime)
    

if __name__ == '__main__':

    file.write(localTime)
    Water_time = 26.67 *60
    Eyes_time = 30 *60
    physical_activity_time = 45 *60
    print(localTime)

    while True:
        now_time = time.time()
        time_d = now_time - initial_time

        if time_d == Water_time:
            Water()
            Water_time += Water_time
        
        elif time_d == Eyes_time:
            Eyes()
            Eyes_time += Eyes_time
        
        elif time_d == physical_activity_time:
            physical_activity()
            physical_activity_time += physical_activity_time

        else:
            if time_d - Water_time == time_d - Eyes_time:
                Water()
                Eyes()
            elif time_d - Water_time == time_d - physical_activity_time:
                physical_activity()
                Water()
            elif time_d - Eyes_time == time_d - physical_activity_time:
                physical_activity()
                Eyes()


    
