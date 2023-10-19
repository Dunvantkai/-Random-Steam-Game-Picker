import random
import os
while True:
    user_input = input("Would you like to pick a Random game Y/N : ")
    if user_input.lower() =='y':
        Directory_Val = "SteamGAme.txt"
        Default_Directory = "C:\Program Files (x86)\Steam\steamapps\common"
        if os.path.exists(Directory_Val):
            os.system('cls')
        else: 
            f = open("SteamGAme.txt", "w")
            print("A New file Was Made")
            f.write(Default_Directory)
            f.close
        txtdir = open("SteamGAme.txt", "r")
        lit = txtdir.read()
        print("The Directory Selected:", lit)
        list = os.listdir(lit)
        # print("Debug", list)
        print("The Game you Should Play is:", random.choice(list))
    else:
        break
#Made by Dunvant_kai