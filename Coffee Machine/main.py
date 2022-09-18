#Simple Program using funcions (not OOP) for a Coffee vending Machine.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 200,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def have_resources(choic, accep):

    if choic not in ["espresso"]:
        if milk < MENU[choic]["ingredients"]["milk"]:
            accep = False

    if water < MENU[choic]["ingredients"]["water"]:
        accep = False
    elif coffee < MENU[choic]["ingredients"]["coffee"]:
        accep = False
    else:
        accep = True

    return accep


def prices():
    print(f"Espresso: ${MENU['espresso']['cost']}")
    print(f"Latte: ${MENU['latte']['cost']}")
    print(f"Cappuccino: ${MENU['cappuccino']['cost']}")



def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def meet_requirement(choic, accep):

    if choic not in ["espresso"]:
        if milk < MENU[choic]["ingredients"]["milk"]:
            print("Not enough Milk")
            accep = False
        else:
            accep = True

    if water < MENU[choic]["ingredients"]["water"]:
        print("Not enough Water")
        accep = False
    elif coffee < MENU[choic]["ingredients"]["coffee"]:
        print("Not enough coffee")
        accep = False
    else:
        accep = True

    return accep


def user_cash(cent, nickel, dime, quarter):

    return cent*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25


playing = True
while playing:
    asking = True
    while asking:
        choice = input("What Would You Like? (espresso/latte/cappuccino), check prices(prices), maintenance options(report/off): ").lower()
        if choice not in ["espresso", "latte", "cappuccino", "report","off","prices"]:
            print("Please choose a valid option.")
            continue
        else:
            asking = False

    if choice == "report":
        report()
        continue
    elif choice == "off":
        print("Machine Shutting Down.")
        playing = False
        break

    elif choice == "prices":
        prices()
        continue

    accept = True
    accept = meet_requirement(choice, accept)

    if not accept:
        continue

    # ASKING FOR USER CASH INPUT
    asking_cents = True
    while asking_cents:
        try:
            cents = int(input("How many cents?: "))
        except:
            print("That is not a number, Try again")
            continue
        else:
            asking_cents = False

    asking_nickel = True
    while asking_nickel:
        try:
            nickels = int(input("How many nickels?: "))
        except:
            print("That is not a number, Try again")
            continue
        else:
            asking_nickel = False

    asking_dimes = True
    while asking_dimes:
        try:
            dimes = int(input("How many dimes?: "))
        except:
            print("That is not a number, Try again")
            continue
        else:
            asking_dimes = False

    asking_quarter = True
    while asking_quarter:
        try:
            quarters = int(input("How many quarters?: "))
        except:
            print("That is not a number, Try again")
            continue
        else:
            asking_quarter = False

    userccash = user_cash(cents,nickels,dimes,quarters)
    usercash = round(userccash,3)

    if usercash < MENU[choice]["cost"]:
        print("Not enough money to complete the purchase, try again.")
        continue
    else:
        water -= MENU[choice]["ingredients"]["water"]
        if choice not in ["espresso"]:
            milk -= MENU[choice]["ingredients"]["milk"]
        coffee -= MENU[choice]["ingredients"]["coffee"]
        money += MENU[choice]["cost"]
        return_cash = round(usercash-MENU[choice]["cost"],3)
        if return_cash > 0:
            print(f"Here is your change: ${return_cash}")
        else:
            pass
        print(f"Here!, Enjoy your awsome {choice} ☕!.")

    count = 0
    accept = True
    for n in ["espresso", "latte", "cappuccino"]:
        accept = have_resources(n, accept)
        if accept == False:
            count += 1
        if count == 3:
            print("The Machine Doesnt have more resources to make any kind of coffee and its shutting down.")
            playing = False













