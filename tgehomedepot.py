import time
print("You were doing your routine Friday night shopping at Home Depot when you noticed two shady people arguing by the paint aisle.")
time.sleep(5)
print("You immediately recognize them as rival bank robbers from Gary, Illinois.")
time.sleep(5)
print("They notice that you noticed them and begin to approach you.")
time.sleep(5)
print("The security guards have noticed them buying odd supplies such as duct tape, ropes, torches, and gasoline.")
time.sleep(5)
print("Both begin begging for your help to escape, offering you a cut from their heist, but you can only help one...")

def chooseCharacter():
    choice = input("Choose who you want to help: Juanita or John")
    if choice == "Juanita":
        print("Hola! I am Juanita, nice to meet you! Let's get out of here!")
    elif choice == "John":
        print("What's up? I'm John. Let's do this!")
    else:
        print("Sorry, incorrect choice")

chooseCharacter()

time.sleep(3)

print("You and your partner have two options: you can either make a run for it or you can try to escape without being seen.")

def choosePath1():
    choice = input("What do you want to do: a)run or b)slyly escape")
    if choice == "a":
        print("Oh no! The security guards are chasing you")
        time.sleep(2)
        choice = input("You choose to lie. You can either say 1) my parents sent me on an errand. I have no idea what the things are for and I was just running late or 2) I need this for my movie set and we need to start building as soon as possible.")
        if choice == "1":
            print("Congrats! The security guards believed your lie and you made it out safely! The bank robbery was a success and you got 50 million dollars.")
        elif choice == "2":
            print("The security guards did not believe your lie and your taken to the interrogation room for questioning.")
            time.sleep(2)
            print("In the interrogation room, you crack and admit you are guilty for conspiring to rob a bank. You are sentenced to 25 years without parole.")
        else:
            print("Sorry, incorrect choice")
    if choice == "b":
        print("You decide to act natural and start walking through the aisles.")
        time.sleep(1)
        print("However, you lose control of your shopping cart and it slams into a pile of lumber, blocking the path towards the exit.")
        time.sleep(2)
        print("You have to act fast, even customers are starting to notice your suspicious activity.")
        time.sleep(2)
        choice = input("You think of three escape plans: 1) you notice an employee walking by who you can overpower and steal his Home Depot apron.  You can use the apron to disguise yourself and walk out. 2)You smell flowers and quickly follow the scent to the greenhouse.  From there you can climb the fence and get to you car.  3) You feel a breeze on your legs and notice a vent by your foot. You think that you can escape through the vents.")
        if choice == "1":
            print("Ouch! The scrawny looking employee is actually a MMA fighter! She fights back and kills you in the process.")
        elif choice == "2":
            print("Your rock climbing classes finally came in handy! You made it over the fence and successfully made into your car. Your partner follows closely behind you and you guys end up robbing the bank together, splitting the profit fifty-fifty.")
        elif choice == "3":
            print("Aw man! Your slim partner crawled into the vents with the supplies and was able to escape, but your wide shoulders could not fit. You got caught and were blamed for the entire fiasco.")
        else:
            print("Sorry, invalid choice")
    else:
        print("Sorry, invalid choice")
choosePath1()
