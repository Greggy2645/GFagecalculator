import time
import json
import random

def calculator():
    eigen_leeftijd = int(input("wat is jouw eigen leeftijd?\n"))
    minimale_leeftijd = (eigen_leeftijd / 2)+7
    #haal de json op
    with open('responses.json', "r+") as f:
        data = json.load(f)
    #genereer random getal
    num1 = random.randint(0, (len(data)-1))
    #wacht 1.5 seconden
    for i in range(3):
        print("\n.")
        time.sleep(0.5)
        
    print("minimale leeftijd voor relatie is: " + str(minimale_leeftijd))
    print(data[num1])
    time.sleep(0.5)
    calculator()

calculator()
