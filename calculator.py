def calculator():
    import random
    eigen_leeftijd = int(input("wat is jouw eigen leeftijd?\n"))
    minimale_leeftijd = (eigen_leeftijd / 2)+7
    #haal de json op
    with open('responses.json') as f:
        data = json.load(f)
    #genereer random getal
    num1 = random.randint(0, 5)
    #wacht 1.5 seconden
    print("\r.", end='\r')
    time.sleep(0.5)
    print("\r.", end='\r')
    time.sleep(0.5)
    print("\r.")
    #antwoord
    print("minimale leeftijd voor relatie is: " + str(minimale_leeftijd))
    #print een response die random nummer in de array van de JSON is
    print (data[num1])
    #wacht 0.5 seconden totdat ie weer door gaat
    time.sleep(0.5)
    calculator()
import time
import json
import random
import sys
calculator()

