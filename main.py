# A program designed to run through a few different rulesets, and view the most viable to survive species.
# Essentially, takes the inputs, rates them with a score, then returns the most viable combination.
# At one point, I will hopefully add complicated features, such as Sp02 and respiration values.

# v1.0-PR-WNT
# Program Version 1.0 | Production Release build WindowsNT

## Imports
from classes import Cell
from os import system
from random import randint, choice
import time
import datetime

## Rulesets
# Environment Rulesets
o2 = 7 # O2 level as a percentage. 7 is nominal, 8+ is dangerously high, and anything below 4 has a percent chance to kill the organism.
lghtmt = 7 # Light amount as a percentage. 7 is nominal, +7 can cause mutations if exposed for too long, while 3 below will slowly begin killing you, depending on factors. Applies to photosynthesis cells. 
fodden = 7 # Food density as a percentage. 7 is nominal, +9 is a high density with near-guaranteed food, while 4 below has a chance to kill the organism. Applies to cellular respiration cells. 
risk = 3 # Starting survival chance, based on certain factors.
pred = 1 # Number of predator species, in a multiple. 1 is Nominal, 2 is dangerous, and three can result in instant death.

# General Rulesets
energy = 6 # Starting cell energy. Wears down over time. If it reaches zero, the cell will instantly die.
MAX_ENERGY = 115 # Maximum cell energy. If the cell passes this energy level, it will die.
hour = 0 # The current number of hours the cell has survived.
filter_type = int(input("Enter a filter (Ten times the numeral you enter): ")) # The current type of data filter requested. 1 = No Filter, 2 = Results with More than 20 Hours Lived, 3 = Results with more than 30 Hours lived.
runtim = int(input("Enter a runtime in generations: "))
i = 0
keypressed = False

## To be worked on in the Beta channel. 
logname = datetime.datetime.now()
logname = datetime.datetime.now()
lgflname = str(logname.strftime("%d") + "-" + logname.strftime("%m") + "-" + logname.strftime("%Y") + "_CellLogFile_" + logname.strftime("%H") + ":" + logname.strftime("%M") + ":" + logname.strftime("%S") + ".log")


## General Variable Establishment
index = 0
cell_id = 0
compl = False # Whether the program is complete running.

dump = open(lgflname, "x")
dump.close()

dump = open(lgflname, "a")
cell_types = ["photo", "respr"]

## ASCII Colour Codes
RST = "\u001b[0m"
RED = "\u001b[31m"
BLU = "\u001b[34;1m"
YLL = "\u001b[33m"
GRN = "\u001b[32m"

## Functions
def clear():
    system('cls')

def dumpfl(hour):
    dump.write(cell.cellDetails(hour))

def timr(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  st = str("{0}:{1}:{2}").format(int(hours),int(mins),sec)
  return st

## Classes  

## Main
start_time = time.time()

try:
    while(i != runtim and keypressed == False):
        # This code just sets up the variables for cell calculations, 'n all that. 
        clear()
        hour = 0
        risk = 3
        cell_id = cell_id + 1
        celtyp = choice(cell_types)
        celcir = randint(1, 10)
        celwal = randint(1, 10)
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(BLU + "Run Number " + str(cell_id) + "/" + str(runtim) + RST)
        print(BLU + "Time Elapsed Since Start: " + timr(time_lapsed) + RST)
        tmptim = time.time()
        #print(BLU + "Elapsed Time: " + timr(tmptim))
        print(BLU + "Notice: Press keys 'Control' and 'C' at the same time to terminate early." + RST)

        cell = Cell(cell_id, energy, celtyp, celcir, celwal) # Create a cell.
        
        ## Risk Calculations
        print(BLU + "Beginning cellular calculations..." + RST)
        # Cell Wall Calculations
        if(cell.wall > 7):
            risk = risk - (cell.wall - 7)
        elif(cell.wall < 7):
            risk = risk + (7 - cell.wall)
            if(risk <= 0):
                risk = 0
        print("Wall calculations compelte | 25%")
        # Food Calculations
        #print(str(cell.celtyp)) #<!-- Debug line. -->
        if(cell.celtyp == "photo"):
            if(lghtmt > 7):
                risk = risk - (lghtmt - 7)
            elif(lghtmt < 7):
                risk = risk + (7 - lghtmt)
                if(risk <= 0):
                    risk = 0
            else:
                risk = risk
        elif(cell.celtyp == "respr"):
            if(fodden > 7):
                risk = risk - (fodden - 7)
            elif(fodden < 7):
                risk = risk + (7 - fodden)
            else:
                risk = risk
        print("Food calculations complete | 50%")
        # Predator Species Calculations
        risk = risk*pred
        print("Predator calculations complete | 75%")
        if(risk >= 7):
            print(YLL + "Alert: Risk rating for cell ID " + str(cell_id) + "| Risk level is at " + str(risk) + "." + RST)
        print(GRN + "Calculations complete. Beginning process for cell ID " + str(cell_id) + RST)

        ## Survival Process and Calculations
        while(cell.energy >= 0):
            hour = hour + 1
            cell.energy = cell.energy - 1
            temp_food = randint(1, 10)
            temp_pred = randint(1, 20)
            if(temp_pred < risk):
                cell.energy = cell.energy - 3
            if(temp_food > fodden):
                cell.energy = cell.energy + 2
        if(cell.energy <= 0):
            print(BLU + "Cell ID " + str(cell_id) + " complete." + RST)
            if(filter_type == 1):
                dumpfl(hour)
            elif(filter_type >= 2):
                temp = filter_type * 10
                if(hour > temp):
                    dumpfl(hour)
        del cell # (At least in small cases), will keep the time down by a micron.
        i = i + 1

except KeyboardInterrupt:
    print("")
    keypressed = True

end_time = time.time()

time_lapsed = end_time - start_time
tottime = str("Time Lapsed: " + timr(time_lapsed))
dump.write(tottime)
clear()

if(keypressed == False):
    print(GRN + "Program completed with zero errors. " + tottime + RST)
else:
    print(RED + "Program terminated manually via keypress. " + RST)
