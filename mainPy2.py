import random, time, os
from sys import exit
# Current gamestate of your playthrough
# Current Room is your current location
# Cursor Room is where you want to go after combat
# Current Enemy is a structure with Name, Weapon, Health, Bounty, Experience
# Experience is your current experience
# Level is your current leve
# Gold is your current gold
# Inventory is a structure with weapon, armour, and badges
gamestate = {"Current Room": "Home",
             "Cursor Room" : "",
             "Current Enemy":{"Name": "", "Weapon":{}, "Health":0, "Bounty":0, "Experience" : 0},
             "Experience" : 0,
             "Level" : 1,
             "Health": 150,
             "Gold": 10,
             "Inventory": {"Weapon":{}, "Armour":{}, "Boss Badges": [] }}

# To win you must collect all the boss badges

# Available armours
armour = {0: {"Name": "Bronze Shield", "Bonus": 30, "Price": 10},
          1: {"Name": "Silver Shield", "Bonus": 50, "Price": 20},
          2: {"Name": "Gold Shield", "Bonus": 70, "Price": 40},
          3: {"Name": "Platinum Shield", "Bonus": 150, "Price": 75}}
# Available weapons
# Accuracy out of 10 (e.g. 5 accuracy hits 50% of the time)
weapons_low = {0: {"Name": "Sword", "Damage": 10, "Accuracy": 9, "Price": 10},
               1: {"Name": "Bow + Arrow", "Damage": 8, "Accuracy": 7, "Price": 5},
               2: {"Name": "Dagger", "Damage" : 5, "Accuracy" : 10, "Price": 7}}

weapons_mid = {0: {"Name": "Spear", "Damage": 14, "Accuracy": 7, "Price": 15},
               1: {"Name": "Curved Sword", "Damage": 12, "Accuracy": 9, "Price": 18},
               2: {"Name": "Axe", "Damage": 15, "Accuracy": 8, "Price": 23},
               3: {"Name": "Large Club", "Damage": 20, "Accuracy": 6, "Price": 30}}

weapons_high = {0: {"Name": "Weed Leaf", "Damage": 420, "Accuracy" : 1, "Price": 45},
                1: {"Name": "Smallpox Blanket", "Damage": 50, "Accuracy": 8, "Price": 75}}

weapons_mythical = {0: {"Name": "Heavenly Sword", "Damage": 70, "Accuracy" : 10, "Price": 0},
                1: {"Name": "Devil's Trident", "Damage": 100, "Accuracy": 8, "Price": 0}}
# Various enemies
bad_guys = {0: {"Name": "Skeletor", "Weapon" : weapons_low[0], "Health" : 50, "Bounty": 10, "Experience" : 3},
            1: {"Name": "Slimy Slug", "Weapon": weapons_low[2], "Health" : 40, "Bounty": 5, "Experience" : 2},
            2: {"Name": "Zombie", "Weapon": weapons_mid[0], "Health": 60, "Bounty": 6, "Experience" : 5},
            3: {"Name": "Annoying Child", "Weapon": weapons_low[1], "Health": 15, "Bounty": 2, "Experience" : 1},
            4: {"Name": "Dastardly Pirate", "Weapon": weapons_mid[1], "Health": 50, "Bounty": 15, "Experience" : 8},
            5: {"Name": "Troll", "Weapon": weapons_mid[3], "Health": 110, "Bounty": 25, "Experience" : 14},
            6: {"Name": "Disease-ridden Child", "Weapon": weapons_high[1], "Health": 10, "Bounty": 5, "Experience" : 20},
            7: {"Name": "Leprechaun", "Weapon": weapons_high[0], "Health": 70, "Bounty": 50, "Experience" : 18}}

# All bosses
bosses = {0: {"Name": "Rotted Greatwood Monster",
              "Weapon" : {"Name": "Vines of DOOM", "Damage": 60, "Accuracy" : 7, "Price": 1000},
          "Health" : 150, "Bounty": 85, "Experience" : 45 },
          1: {"Name": "Cave Giant",
          "Weapon" : {"Name": "Rock Hurl", "Damage": 85, "Accuracy" : 6, "Price": 1000},
          "Health" : 200, "Bounty": 50,
          "Experience" : 60} }

#: {"Name": "", "Weapon": weapons[], "Health": , "Bounty": }
#Start_text =print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."

# Number used when randomly selecting a weapon for you
number_of_weapons_low = len(weapons_low) - 1
number_of_weapons_mid = len(weapons_mid) - 1
number_of_weapons_high = len(weapons_high) - 1
number_of_bad_guys = len(bad_guys) - 1
number_of_armours = len(armour) - 1

# Checks to see if you have won or if you have leveled up to level 2
def exp_call_1(gamestate):
    if "Forest" in gamestate["Inventory"]["Boss Badges"] and "Mountain" in gamestate["Inventory"]["Boss Badges"]:
        win()
    else:
        if gamestate["Experience"] >= 60:
        if gamestate["Level"] == 1:
            gamestate["Level"] = gamestate["Level"] + 1
            print "You've Leveled up to level " + str(gamestate["Level"]) + "!"
                time.sleep(2)
            exp_call_2(gamestate)
        else:
            exp_call_2(gamestate)
        else:
        room_call(gamestate)

# Checks to see if you have leveled up to level 3. Need to add a new level
def exp_call_2(gamestate):
    if gamestate["Experience"] >= 150:
    if gamestate["Level"] == 2:
        gamestate["Level"] = gamestate["Level"] + 1
        print "You've Leveled up to level " + str(gamestate["Level"]) + "!"
        time.sleep(2)
        exp_call_3(gamestate)
    else:
        exp_call_3(gamestate)
    else:
    room_call(gamestate)

def exp_call_3(gamestate):
    room_call(gamestate)

# Depending on your current room, it directs you to a different gamestate
def room_call(gamestate):
    if gamestate["Current Room"] == "Home":
    os.system('clear')
        Home_Room(gamestate)
    elif gamestate["Current Room"] == "Death Room":
    os.system('clear')
        Death_Room(gamestate)
    elif gamestate["Current Room"] == "Pre Fight Room":
    os.system('clear')
        Pre_Fight_Room(gamestate)
    elif gamestate["Current Room"] == "combat":
    os.system('clear')
        combat(gamestate)
    elif gamestate["Current Room"] == "Post Fight Room":
    os.system('clear')
        Post_Fight_Room(gamestate)
    elif gamestate["Current Room"] == "Treasure Room":
        os.system('clear')
        Treasure_Room(gamestate)
    elif gamestate["Current Room"] == "Store":
    os.system('clear')
        Store_Room(gamestate)
    elif gamestate["Current Room"] == "Forest Boss Room":
    os.system('clear')
        Forest_Boss_Room(gamestate)
    elif gamestate["Current Room"] == "Post Boss Room":
    os.system('clear')
        Post_Boss_Room(gamestate)
    elif gamestate["Current Room"] == "Casino Room":
    os.system('clear')
        Casino_Room(gamestate)
    elif gamestate["Current Room"] == "Dirt Road Room":
    os.system('clear')
        Dirt_Road_Room(gamestate)
    elif gamestate["Current Room"] == "Mountain Climb":
    os.system('clear')
        Mountain_Climb_Room(gamestate)
    elif gamestate["Current Room"] == "Mountain Peak":
    os.system('clear')
        Mountain_Peak_Room(gamestate)
    elif gamestate["Current Room"] == "Mountain Boss":
    os.system('clear')
        Mountain_Boss_Room(gamestate)
    elif gamestate["Current Room"] == "Faith":
    os.system('clear')
        Faith_Room(gamestate)

# How combat is initiated
def combat(gamestate):
    os.system('clear')
    player_weapon = gamestate["Inventory"]["Weapon"]
    enemy_weapon = gamestate["Current Enemy"]["Weapon"]
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "You wield a " + str(gamestate["Inventory"]["Weapon"]["Name"])
    print "You face a " + str(gamestate["Current Enemy"]["Name"]) + " who has " + str(gamestate["Current Enemy"]["Health"]) + " health."
    print "Fight begins in 5 seconds"
    time.sleep(5)
    os.system('clear')
    while gamestate["Health"] > 0 and gamestate["Current Enemy"]["Health"] > 0:
        # Actual combat
        a = player_weapon["Accuracy"] + 1
        accuracy = list(range(1, a))
        pick = random.randint(1,10)
        if pick in accuracy:
            print "You hit " + str(gamestate["Current Enemy"]["Name"]) + " for " + str(player_weapon["Damage"] * gamestate["Level"]) + " damage."
            gamestate["Current Enemy"]["Health"] = gamestate["Current Enemy"]["Health"] - (player_weapon["Damage"] * gamestate["Level"])
            print "Player: " + str(gamestate["Health"]) + " health."
            print "Enemy: " + str(gamestate["Current Enemy"]["Health"]) + " health."
            time.sleep(2)
            print ""
            pass
        else:
            print "You miss!"
            print ""
            time.sleep(1)
            pass
    # If the enemy is still alive
        if gamestate["Current Enemy"]["Health"] > 0:
            b = enemy_weapon["Accuracy"] + 1
            accuracy = list(range(1, b))
            pick = random.randint(0,8)
            if pick in accuracy:
                print str(gamestate["Current Enemy"]["Name"]) + " hits you for " + str(enemy_weapon["Damage"]) + " damage."
    if bool(gamestate["Inventory"]["Armour"]) is not False:
        current_armour = gamestate["Inventory"]["Armour"]["Bonus"]
        if current_armour > 0:
                        gamestate["Inventory"]["Armour"]["Bonus"]  = gamestate["Inventory"]["Armour"]["Bonus"]  - enemy_weapon["Damage"]
                        gamestate["Health"] = gamestate["Health"] + enemy_weapon["Damage"]
                        if gamestate["Inventory"]["Armour"]["Bonus"] <= 0:
        gamestate["Health"] = gamestate["Health"] + gamestate["Inventory"]["Armour"]["Bonus"]
                            print "Your armour shattered."
            	    gamestate["Inventory"]["Armour"] = {}
                            pass
                    else:
                        pass
                else:
                    pass
                gamestate["Health"] = gamestate["Health"] - enemy_weapon["Damage"]
    if bool(gamestate["Inventory"]["Armour"]) is not False:
                print "Player: " + str(gamestate["Health"]) + " health and " + str(gamestate["Inventory"]["Armour"]["Bonus"]) + "armour."
        	    print "Enemy: " + str(gamestate["Current Enemy"]["Health"]) + " health."
                    time.sleep(2)
        	    print ""
        	    pass
    else:
        print "Player: " + str(gamestate["Health"]) + " health."
        	    print "Enemy: " + str(gamestate["Current Enemy"]["Health"]) + " health."
        	    time.sleep(2)
                    print ""
                    pass
            else:
                print "They miss their attack!"
                print ""
                time.sleep(1)
                pass
        else:
            pass
    if gamestate["Health"] <= 0:
        print "You are dead"
        time.sleep(2)
        os.system('clear')
        dead()
    else:
        print "You win the fight and survive with " + str(gamestate["Health"]) + " health."
    print "You gain " + str(gamestate["Current Enemy"]["Experience"]) + " experience!"
    print "You loot the enemy for " + str(gamestate["Current Enemy"]["Bounty"]) + " Gold."
    gamestate["Experience"] =  gamestate["Experience"] + gamestate["Current Enemy"]["Experience"]
        gamestate["Gold"] = gamestate["Gold"] + gamestate["Current Enemy"]["Bounty"]
        time.sleep(3)
        os.system('clear')
        gamestate["Current Room"] = gamestate["Cursor Room"]
        exp_call_1(gamestate)

# Initiating original room
def Home_Room(gamestate):
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "Welcome home. Here are your options: "
    print " (1) East (2) West (3) North"
    decision = raw_input(" > ")
    if "1" in decision or "2" in decision or "3" in decision:
        if "1" in decision:
            gamestate["Current Room"] = "Death Room"
            time.sleep(1)
            exp_call_1(gamestate)
        elif "2" in decision:
            time.sleep(1)
            gamestate["Current Room"] = "Pre Fight Room"
            exp_call_1(gamestate)
        elif "3" in decision:
            time.sleep(1)
            gamestate["Current Room"] = "Dirt Road Room"
            exp_call_1(gamestate)
    else:
        print "Incorrect entry"
        time.sleep(1)
        Home_Room(gamestate)

def Death_Room(gamestate):
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "You have entered the Forest.\nIn front of you lie two patches of grass\nChoose a patch to walk over.. 1 or 2?"
    correct_choice = "1"
    choice = raw_input(" > ")
    if choice == correct_choice:
        print "You lucky SOB"
        time.sleep(2)
        os.system('clear')
        print "You've lived to fight another day."
        print "(1) North (2) West"
        choice = raw_input(" > ")
        if "1" in choice:
            gamestate["Current Room"] = "Store"
            exp_call_1(gamestate)
        elif "2" in choice:
            gamestate["Current Room"] = "Home"
            exp_call_1(gamestate)
        else:
            print "Misclick! You must face the forest trap once more."
            time.sleep(2)
            Death_Room(gamestate)
    else:
        print "Wrong choice bub. You fall through the booby trap and die"
        time.sleep(2)
        os.system('clear')
        dead()

def Pre_Fight_Room(gamestate):
    print "Welcome to the Coliseum young traveler"
    print "....the door closes behind you."
    while bool(gamestate["Inventory"]["Weapon"]) is False:
        x = random.randint(0,number_of_weapons_low)
        assigned_weapon = weapons_low[x]
        gamestate["Inventory"]["Weapon"] = assigned_weapon
        print "You find a " + str(assigned_weapon["Name"]) + " on the ground."
        time.sleep(2)
        pass
    y = random.randint(0,number_of_bad_guys)
    enemy = bad_guys[y]
    gamestate["Current Enemy"]["Name"] = enemy["Name"]
    gamestate["Current Enemy"]["Health"] = enemy["Health"]
    gamestate["Current Enemy"]["Weapon"] = enemy["Weapon"]
    gamestate["Current Enemy"]["Bounty"] = enemy["Bounty"]
    gamestate["Current Enemy"]["Experience"] = enemy["Experience"]
    print "You enter the fight room wielding a " + str(gamestate["Inventory"]["Weapon"]["Name"]) + " and must face a " + str(enemy["Name"]) + "!\n"
    raw_input("Press enter to continue")
    gamestate["Current Room"] = "combat"
    gamestate["Cursor Room"] = "Post Fight Room"
    room_call(gamestate)

#present options
def Post_Fight_Room(gamestate):
    os.system('clear')
    print "Where will you go next?"
    print " (1) Exit Coliseum (2) Open door to the South "
    decision = raw_input(" > ")
    if "1" in decision or "2" in decision:
        if "1" in decision:
            gamestate["Current Room"] = "Home"
            time.sleep(1)
            exp_call_1(gamestate)
        elif "2" in decision:
            time.sleep(1)
            gamestate["Current Room"] = "Treasure Room"
            exp_call_1(gamestate)
    else:
        print "Incorrect entry"
        time.sleep(1)
        Post_Fight_Room(gamestate)

# Treasure room of the game
def Treasure_Room(gamestate):
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "You have entered a Treasure Room! A suspicious chest lies on the floor."
    print "Do you open the chest? (1) Yes (2) No"
    choice = raw_input(" > ")
    if "1" in choice:
        ab = random.randint(1,2)
        if ab == 1:
            x = random.randint(0,number_of_weapons_mid)
            random_weapon = weapons_mid[x]
            print "You open the chest and find a " + str(random_weapon["Name"]) + "!"
            print "Would you like to exchange your " + str(gamestate["Inventory"]["Weapon"]["Name"]) +  " for a " + str(random_weapon["Name"]) + " ?!"
            print "(1) Yes (2) No"
            choice = raw_input("> ")
            if "1" in choice:
                gamestate["Inventory"]["Weapon"] = random_weapon
    print "Congrats on the new weapon!"
    time.sleep(2)
                pass
            elif "2" in choice:
                print "As you wish"
    time.sleep(2)
                pass
        if ab == 2:
            y = random.randint(0,number_of_armours)
            random_armour = armour[y]
            print "You open the chest to find a " + str(random_armour["Name"]) + "!"
            print "Would you like to take the armour or keep your old gear?"
            print "(1) Hell yea (2) I prefer my current arrangement"
            choice = raw_input(" > ")
            if "1" in choice:
                gamestate["Inventory"]["Armour"] = random_armour
                print "Congratulations! You pick up the armour."
                time.sleep(2)
                pass
            elif "2" in choice:
                print "As you wish"
                time.sleep(2)
                pass
            else:
                print "You misclicked, therefore NO ARMOUR FOR YOU"
                time.sleep(2)
                pass
    else:
        print "Interesting choice. You leave the chest as is"
    time.sleep(2)
        pass
    os.system('clear')
    print "Where will you go next?"
    print " (1) Back to the Fight room (2) Take the back exit "
    decision = raw_input(" > ")
    if "1" in decision or "2" in decision:
        if "1" in decision:
            gamestate["Current Room"] = "Pre Fight Room"
            time.sleep(1)
            exp_call_1(gamestate)
        elif "2" in decision:
            time.sleep(1)
            gamestate["Current Room"] = "Home"
            exp_call_1(gamestate)
    else:
        print "Uh oh. Misclick means DEATH"
        time.sleep(2)
        dead()

# Store keeps replenishing a fresh random list of items everytime you walk in. Fix this. Make the items global so that buying one removes it from the store

#mid tier weapon
a = random.randint(0, number_of_weapons_mid)
a1 = weapons_mid[a]
#high tier weapon
b = random.randint(0, number_of_weapons_high)
b1 = weapons_high[b]
#armour
c = random.randint(0, (number_of_armours - 1))
c1 = armour[c]

store_wares = [a1, b1, c1]

def Store_Room(gamestate):
    os.system('clear')
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "You arrive upon a battered down shack.\nA man pops up from the counter and says:\nHowdy partner! What can I do for ya?\n(1) Buy\n(2) Heal up\n(3) Ignore man"
    choice = raw_input(" > ")
    #BUYING
    if "1" in choice:
    os.system('clear')
        print "What would you like to buy?"
        print "You currently have " + str(gamestate["Gold"]) + " Gold."
        print ""
        print ""
    print "(0) Nothing today, thanks."
        positions = []
    for item in store_wares:
            item_position = store_wares.index(item)
            positions.append(item_position)
            print "(" + str(item_position + 1) + ")" + str(item["Name"]) + " - " + str(item["Price"]) + " Gold."
        choice_2 = raw_input(" > ")
        chosen_item = int(choice_2)
    # Not buying
        if chosen_item == 0:
            print "The store owner wishes you safe travels."
            time.sleep(2)
            pass
    # Buying specific item
        elif chosen_item - 1 <= len(store_wares):
            store_wares_new = list(enumerate(store_wares))
            for item in store_wares_new:
                if chosen_item - 1 == item[0]:
                    finalized_item = item[-1]
                    #purchase
                    if gamestate["Gold"] >= finalized_item["Price"]:
                        gamestate["Gold"] = gamestate["Gold"] - finalized_item["Price"]
                        store_wares.remove(finalized_item)
                        #Armour or Weapon?
                        if "Damage" in finalized_item:
                            gamestate["Inventory"]["Weapon"] = finalized_item
                            print "Congrats on the new " +str(finalized_item["Name"]) + "!"
                            time.sleep(2)
                            pass
                        else:
                            gamestate["Inventory"]["Armour"] = finalized_item
                            print "Congrats on the new " +str(finalized_item["Name"]) + "!"
                            time.sleep(2)
                            pass
                    else:
                        print"Not enough gold to purchase. Owner gets upset and stabs you"
                        time.sleep(2)
                        dead()
                else:
                    pass
        else:
            pass
    #HEALING
    elif "2" in choice:
    os.system('clear')
        print "You currently have " + str(gamestate["Gold"]) + " Gold."
        print "Would you like to heal yourself by 50 for 10 gold?\n(1) Yes (2) No"
        choice = raw_input("> ")
        if "1" in choice:
            if gamestate["Gold"] >= 10:
                gamestate["Health"] = gamestate["Health"] + 50
                gamestate["Gold"] = gamestate["Gold"] - 10
                print "Your new health is " + str(gamestate["Health"])
    time.sleep(2)
    pass
            else:
                print "Insufficient funds. Store owner gets upset and stabs you"
                time.sleep(2)
                kill()
        if "2" in choice:
            print "The store owner wishes you safe travels."
            time.sleep(2)
            pass
    else:
        pass
    #CONTINUING
    os.system('clear')
    print " Where to from here?"
    print "(1) South (2) Northward Ho! (3) Wait I still want something"
    choice = raw_input(" > ")
    if "1" in choice:
        gamestate["Current Room"] = "Death Room"
        exp_call_1(gamestate)
    elif "2" in choice:
        gamestate["Current Room"] = "Forest Boss Room"
        exp_call_1(gamestate)
    elif "3" in choice:
        Store_Room(gamestate)
    else:
        print "You should know better than to input incorrectly"
        time.sleep(2)
        kill()

def Forest_Boss_Room(gamestate):
    os.system('clear')
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "A clearing opens into a small arena"
    while bool(gamestate["Inventory"]["Weapon"]) is False:
        x = random.randint(0,number_of_weapons_low)
        assigned_weapon = weapons_low[x]
        gamestate["Inventory"]["Weapon"] = assigned_weapon
        print "You find a " + str(assigned_weapon["Name"]) + " on the ground."
        time.sleep(2)
        pass
    print "A large tree on the opposite side suddenly comes alive!"
    enemy = bosses[0]
    gamestate["Current Enemy"]["Name"] = enemy["Name"]
    gamestate["Current Enemy"]["Health"] = enemy["Health"]
    gamestate["Current Enemy"]["Weapon"] = enemy["Weapon"]
    gamestate["Current Enemy"]["Bounty"] = enemy["Bounty"]
    gamestate["Current Enemy"]["Experience"] = enemy["Experience"]
    time.sleep(4)
    gamestate["Current Room"] = "combat"
    gamestate["Cursor Room"] = "Post Boss Room"
    exp_call_1(gamestate)

def Dirt_Road_Room(gamestate):
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "You find yourself on a boring dirt road.\nTo the West lies an old run-down building.\nWhere to from here?"
    print "(1) South (2) West (3) North"
    choice = raw_input(" > ")
    if "1" in choice:
        gamestate["Current Room"] = "Home"
        exp_call_1(gamestate)
    elif "2" in choice:
        gamestate["Current Room"] = "Casino Room"
        exp_call_1(gamestate)
    elif "3" in choice:
        gamestate["Current Room"] = "Mountain Climb"
        exp_call_1(gamestate)
    else:
        print "Incorrect Input"
        time.sleep(1)
        Dirt_Road_Room(gamestate)

def Casino_Room(gamestate):
    os.system('clear')
    print "Welcome to the Mountaineer's Casino!!"
    print ""
    print "You currently have " +str(gamestate["Gold"]) + " gold."
    print "Would you like to\n(1) Play Roulette (2) Play Blackjack (3) Hit the Slots (4) Exit Casino"
    choice = raw_input("> ")
    time.sleep(2)
    os.system('clear')
    if "1" in choice:
        Roulette_Room(gamestate)
        Casino_Room(gamestate)
    elif "2" in choice:
        if gamestate["Gold"] > 0:
            start(jackstate)
            Casino_Room(gamestate)
        else:
            print "Sorry bud, you don't have enough gold."
            Casino_Room(gamestate)
    elif "3" in choice:
        Slots(gamestate)
    elif "4" in choice:
        gamestate["Current Room"] = "Dirt Road Room"
        exp_call_1(gamestate)
    else:
        pass

#################################################################
##SLOT MACHINE SECTION##
#################################################################

Slot_Symbols = ["   $   ", "   @   ", "   *   ", "   #   ", "   %   "]

def Slots(gamestate):
    print "Welcome to the Slot machine!!"
    print ""
    print "$ $ $ $ --> 50 gold"
    print ""
    print "$ $ $ --> 15 gold"
    print ""
    print "$ $ --> 6 gold"
    print ""
    print "@ @ @ @ --> 30 gold"
    print ""
    print "@ @ @ or @ @ --> 4 gold"
    print ""
    print "* * * * or * * * -->  4 gold"
    print ""
    print "You currently have " + str(gamestate["Gold"]) + " Gold."
    print "(1) Enter 2 Gold and spin (2) Back out"
    choice = raw_input(" > ")
    if "2" in choice:
        Casino_Room(gamestate)
    elif "1" in choice:
        if gamestate["Gold"] >= 2:
            gamestate["Gold"] = gamestate["Gold"] - 2
            os.system('clear')
            Slot_State = []
            Slotted = list(enumerate(Slot_Symbols))
            #Spin First Symbol
            print Slot_State
            aa = random.randint(0, 2)
            for item in Slotted:
                if aa == item[0]:
                    Slot_State.append(item[-1])
                else:
                    pass
            time.sleep(1)
            os.system('clear')
            #Spin Second Symbol
            print Slot_State
            bb = random.randint(0, 4)
            for item in Slotted:
                if bb == item[0]:
                    Slot_State.append(item[-1])
                else:
                    pass
            time.sleep(1)
            os.system('clear')
            #Spin Third Symbol
            print Slot_State
            cc = random.randint(0, 3)
            for item in Slotted:
                if cc == item[0]:
                    Slot_State.append(item[-1])
                else:
                    pass
            time.sleep(1)
            os.system('clear')
            print Slot_State
            #Spin Fourth Symbol
            dd = random.randint(0, 4)
            for item in Slotted:
                if dd == item[0]:
                    Slot_State.append(item[-1])
                else:
                    pass
            time.sleep(1)
            os.system('clear')
            print Slot_State
            time.sleep(3)
            os.system('clear')
            if Slot_State.count("   $   ") == 4:
                gamestate["Gold"] = gamestate["Gold"] + 50
                print "JACKPOT!\nYou win 50 Gold!"
                time.sleep(2)
                Slots(gamestate)
            elif Slot_State.count("   $   ") == 3:
                gamestate["Gold"] = gamestate["Gold"] + 15
                print "You win 15 Gold!"
                time.sleep(2)
                Slots(gamestate)
            elif Slot_State.count("   $   ") == 2:
                gamestate["Gold"] = gamestate["Gold"] + 6
                print "You win 6 Gold!"
                time.sleep(2)
                Slots(gamestate)
            elif Slot_State.count("   @   ") == 4:
                gamestate["Gold"] = gamestate["Gold"] + 30
                print "You win 30 Gold!"
                time.sleep(2)
                Slots(gamestate)
            elif Slot_State.count("   @   ") == 3 or Slot_State.count("   @   ") == 2:
                gamestate["Gold"] = gamestate["Gold"] + 4
                print "You win 4 Gold!"
                time.sleep(2)
                Slots(gamestate)
            elif Slot_State.count("   *   ") == 4 or Slot_State.count("   *   ") == 3:
                gamestate["Gold"] = gamestate["Gold"] + 4
                print "You win 4 Gold!"
                time.sleep(2)
                Slots(gamestate)
            else:
                print "You Lose :/"
                time.sleep(2)
                Slots(gamestate)
        else:
            print "You Don't have enough money!"
            time.sleep(2)
            Casino_Room(gamestate)
    else:
        Casino_Room(gamestate)

###################################################################################
##END OF SLOT MACHINE SECTION##
###################################################################################

######################################################################
#Roulette
######################################################################
bets = {"Number": {"Bet": 0, "Single": 0}, "Color": {"Bet": 0, "color": ""}, "Odd/Even": {"Bet": 0, "Parity": ""}}
roll = {"Single": 0, "Color": 0, "Odd/Even": 0}
def Roulette_Room(gamestate):
    roulettegold = gamestate["Gold"]
    while gamestate["Gold"] > 0:
        totalbet = int(bets["Number"]["Bet"]) + int(bets["Color"]["Bet"]) + int(bets["Odd/Even"]["Bet"])
        currentgold = roulettegold - totalbet
        time.sleep(2)
        os.system('clear')
        print "You have " + str(currentgold) + " Gold to gamble."
        print "What would you like to do? \n(1) Place bet (2) Spin the wheel (3) Return"
        choice = raw_input("> ")
        if int(totalbet) <= int(roulettegold):
            if "1" in choice:
                os.system('clear')
                print "You currently have " + str(currentgold) + " Gold."
                print "You are currently wagering " + str(totalbet) + " Gold."
                print "What would you like to place a bet on?"
                print "(1) Number (2) Color (3) Odd/Even"
                choice5 = raw_input("> ")
                if "1" in choice5:
                    if int(bets["Number"]["Bet"]) == 0:
                        os.system('clear')
                        print "Odds 35:1"
                        print "How much do you want to bet?"
                        choice = raw_input("> ")
                        if int(choice) <= int(gamestate["Gold"]):
                            bets["Number"]["Bet"] = choice
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "Which number? (0-36)"
                        choice2 = raw_input("> ")
                        bets["Number"]["Single"] = choice2
                        Roulette_Room(gamestate)
                    else:
                        bets["Number"]["Bet"] = 0
                        bets["Number"]["Number"] = 0
                        os.system('clear')
                        print "Odds 35:1"
                        print "How much do you want to bet?"
                        choice = raw_input("> ")
                        if int(choice) <= int(gamestate["Gold"]):
                            bets["Number"]["Bet"] = choice
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "Which number? (0-36)"
                        choice2 = raw_input("> ")
                        bets["Number"]["Single"] = choice2
                        Roulette_Room(gamestate)
                elif "2" in choice5:
                    if int(bets["Color"]["Bet"]) == 0:
                        os.system('clear')
                        print "Odds 2:1"
                        print "How much do you want to bet?"
                        choice7 = raw_input("> ")
                        if int(choice7) <= int(gamestate["Gold"]):
                            bets["Color"]["Bet"] = choice7
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "Which color? (1) Black or (2) Red"
                        choice6 = raw_input("> ")
                        if "1" in choice6:
                            bets["Color"]["color"] = "Black"
                        elif "2" in choice6:
                            bets["Color"]["color"] = "Red"
                        else:
                            print "Print either 1 or 2"
                            pass
                        Roulette_Room(gamestate)
                    else:
                        bets["Color"]["Bet"] = 0
                        bets["Color"]["Number"] = 0
                        os.system('clear')
                        print "Odds 2:1"
                        print "How much do you want to bet?"
                        choice7 = raw_input("> ")
                        if int(choice7) <= int(gamestate["Gold"]):
                            bets["Color"]["Bet"] = choice7
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "Which color? (1) Black or (2) Red"
                        choice6 = raw_input("> ")
                        if "1" in choice6:
                            bets["Color"]["color"] = "Black"
                        elif "2" in choice6:
                            bets["Color"]["color"] = "Red"
                        else:
                            print "Print either 1 or 2"
                            pass
                        Roulette_Room(gamestate)
                elif "3" in choice5:
                    if int(bets["Odd/Even"]["Bet"]) == 0:
                        os.system('clear')
                        print "Odds 2:1"
                        print "How much do you want to bet?"
                        choice8 = raw_input("> ")
                        if int(choice8) <= int(gamestate["Gold"]):
                            bets["Odd/Even"]["Bet"] = choice8
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "(1) Odd or (2) Even?"
                        choice3 = raw_input("> ")
                        if "1" in choice3:
                            bets["Odd/Even"]["Parity"] = "Odd"
                        elif "2" in choice3:
                            bets["Odd/Even"]["Parity"] = "Even"
                        Roulette_Room(gamestate)
                    else:
                        bets["Odd/Even"]["Bet"] = 0
                        bets["Odd/Even"]["Number"] = 0
                        os.system('clear')
                        print "Odds 2:1"
                        print "How much do you want to bet?"
                        choice8 = raw_input("> ")
                        if int(choice8) <= int(gamestate["Gold"]):
                            bets["Odd/Even"]["Bet"] = choice8
                            pass
                        else:
                            print "You don't have enough."
                            Roulette_Room(gamestate)
                        print "(1) Odd or (2) Even?"
                        choice3 = raw_input("> ")
                        if "1" in choice3:
                            bets["Odd/Even"]["Parity"] = "Odd"
                        elif "2" in choice3:
                            bets["Odd/Even"]["Parity"] = "Even"
                        Roulette_Room(gamestate)
                else:
                    Roulette_Room(gamestate)
            elif "2" in choice:
                os.system('clear')
                bet1 = random.randint(0,36)
                roll["Single"] = bet1
                if bet1 == 0:
                    roll["Number"] = 0
                    roll["Odd/Even"] = "None"
                    roll["Color"] = "None"
                if bet1 in range(1,10):
                    if bet1 % 2 == 0:
                        roll["Odd/Even"] = "Even"
                        roll["Color"] = "Black"
                    elif bet1 % 2 != 0:
                        roll["Odd/Even"] = "Odd"
                        roll["Color"] = "Red"
                elif bet1 in range(11,18):
                    if bet1 % 2 == 0:
                        roll["Odd/Even"] = "Even"
                        roll["Color"] = "Red"
                    elif bet1 % 2 != 0:
                        roll["Odd/Even"] = "Odd"
                        roll["Color"] = "Black"
                elif bet1 in range(19,28):
                    if int(bet1) % 2 == 0:
                        roll["Odd/Even"] = "Even"
                        roll["Color"] = "Black"
                    elif int(bet1) % 2 != 0:
                        roll["Odd/Even"] = "Odd"
                        roll["Color"] = "Red"
                elif bet1 in range(19,37):
                    if int(bet1) % 2 == 0:
                        roll["Odd/Even"] = "Even"
                        roll["Color"] = "Red"
                    elif bet1 % 2 != 0:
                        roll["Odd/Even"] = "Odd"
                        roll["Color"] = "Black"
                print "You rolled a " + str(roll["Single"]) + " which is " + str(roll["Color"]) + "."
                totalbet = int(bets["Number"]["Bet"]) + int(bets["Color"]["Bet"]) + int(bets["Odd/Even"]["Bet"])
                winnings = []
                if bets["Number"]["Single"] == bet1:
                    winnumber = winnings.append(int(bets["Number"]["Bet"]) * 36)
                else:
                    winnumber = 0
                    pass
                if str(roll["Color"]) in str(bets["Color"]["color"]):
                    wincolor = winnings.append(int(bets["Color"]["Bet"]) * 2)
                else:
                    wincolor = 0
                    pass
                if str(roll["Odd/Even"]) in str(bets["Odd/Even"]["Parity"]):
                    winparity = winnings.append(int(bets["Odd/Even"]["Bet"]) * 2)
                else:
                    winparity = 0
                    pass
                actualwinnings = sum(winnings)
                time.sleep(3)
                print "You win " + str(actualwinnings) + " Gold."
                gamestate["Gold"] = int(currentgold) + int(actualwinnings)
                print "You currently have " + str(gamestate["Gold"]) + " gold."
                print "All bets are reset"
                print "Would you like to play again? (1) Yes or (2) No?"
                choice2 = raw_input("> ")
                if "1" in choice2:
                    bets["Number"]["Bet"] = 0
                    bets["Number"]["Single"] = 0
                    bets["Color"]["color"] = ""
                    bets["Color"]["Bet"] = 0
                    bets["Odd/Even"]["Parity"] = ""
                    bets["Odd/Even"]["Bet"] = 0
                    roll["Single"] = 0
                    roll["Color"] = ""
                    roll["Odd/Even"] = ""
                    Roulette_Room(gamestate)
                elif "2" in choice2:
                    bets["Number"]["Bet"] = 0
                    bets["Number"]["Single"] = 0
                    bets["Color"]["color"] = ""
                    bets["Color"]["Bet"] = 0
                    bets["Odd/Even"]["Parity"] = ""
                    bets["Odd/Even"]["Bet"] = 0
                    roll["Single"] = 0
                    roll["Color"] = ""
                    roll["Odd/Even"] = ""
                    Casino_Room(gamestate)
            elif "3" in choice:
                print "Very well"
                bets["Number"]["Bet"] = 0
                bets["Number"]["Single"] = 0
                bets["Color"]["color"] = ""
                bets["Color"]["Bet"] = 0
                bets["Odd/Even"]["Parity"] = ""
                bets["Odd/Even"]["Bet"] = 0
                roll["Single"] = 0
                roll["Color"] = ""
                roll["Odd/Even"] = ""
                Casino_Room(gamestate)
        else:
            print "You don't have enough money to add to the table. Please spin the wheel or leave."
            pass
    print "Sorry, you don't have enough gold"
    time.sleep(3)
    Casino_Room(gamestate)

###################################################################################
##END OF Roulette SECTION##
###################################################################################


################################################################################################
##BLACKJACK SECTION##
################################################################################################

###blackjack
suits = ['S','C','D','H']
value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
number_min = [1,2,3,4,5,6,7,8,9,10,10,10,10]
number_max = [11,2,3,4,5,6,7,8,9,10,10,10,10]
jackstate = {'Deck': [], 'Player': [], 'Dealer': [], 'Split': False, 'Gold': gamestate["Gold"], 'Wager': 0}

def start(jackstate):
    jackstate = {'Deck': [], 'Player': [], 'Dealer': [], 'Split': False, 'Gold': gamestate["Gold"], 'Wager': 0}
    while jackstate['Gold'] > 0:

        print "Would you like to play a hand?\n(1) Yes (2) No"
        choice = raw_input(" > ")
        if "1" in choice:
            play_hand(jackstate)
        else:
            gamestate["Gold"] = int(jackstate['Gold'])
            print "You leave the table with " + str(gamestate["Gold"]) + " Gold."
            time.sleep(2)
            Casino_Room(gamestate)

    print "You have lost all your money"
    time.sleep(2)
    gamestate["Gold"] = int(jackstate['Gold'])
    Casino_Room(gamestate)
def deck_creation():
    deck = []
    for a in suits:
        for b in value:
            for c in range(0,4):
                deck.append(b + a)
    return deck

def reshuffle(jackstate):
    player_hand = []
    dealer_hand = []
    deck = deck_creation()
    for a in range(0,2):
        card = random.choice(deck)
        player_hand.append(card)
        deck.remove(card)
    for b in range(0,2):
        card = random.choice(deck)
        dealer_hand.append(card)
        deck.remove(card)
    jackstate['Deck'] = deck
    jackstate['Player'] = player_hand
    jackstate['Dealer'] = dealer_hand
    jackstate['Split'] = False
    return jackstate

def deal(jackstate):
    player_hand = []
    dealer_hand = []
    for a in range(0,2):
        card = random.choice(jackstate['Deck'])
        player_hand.append(card)
        jackstate['Deck'].remove(card)
    for b in range(0,2):
        card = random.choice(jackstate['Deck'])
        dealer_hand.append(card)
        jackstate['Deck'].remove(card)
    jackstate['Player'] = player_hand
    jackstate['Dealer'] = dealer_hand
    jackstate['Split'] = False
    return jackstate

def same_value(hand):
    card_1 = hand[0]
    card_2 = hand[1]
    if card_1[0] == card_2[0]:
        return True
    else:
        return False

def check_sum(hand):
    sum_hand_min = 0
    sum_hand_max = 0
    for card in hand:
        for v in value:
            if v in card:
                sum_hand_min += number_min[value.index(v)]
                sum_hand_max += number_max[value.index(v)]
    if len(hand) == 2 and sum_hand_max == 21:
        return 'Blackjack'
    if sum_hand_min > 21:
        return 'Bust'
    elif sum_hand_max > 21 and sum_hand_min < 21:
        return sum_hand_min
    else:
        return sum_hand_max

def compare_sums(jackstate,dealer_sum):
    player_sum_min = 0
    player_sum_max = 0
    your_hand_text = 'You: '
    for cards in jackstate['Player']:
        your_hand_text += cards + ' '
    dealer_hand_text = 'Dealer: '
    for cards in jackstate['Dealer']:
        dealer_hand_text += cards + ' '
    for card in jackstate['Player']:
        for v in value:
            if v in card:
                player_sum_min += number_min[value.index(v)]
                player_sum_max += number_max[value.index(v)]
    if player_sum_max > 21:
        player_sum = player_sum_min
    else:
        player_sum = player_sum_max
    if dealer_sum > player_sum:
        os.system('clear')
        print(your_hand_text)
        print(dealer_hand_text)
        print('The dealer wins.')
        jackstate['Gold'] -= jackstate['Wager']
        return
    elif player_sum > dealer_sum:
        os.system('clear')
        print(your_hand_text)
        print(dealer_hand_text)
        print('You win')
        jackstate['Gold'] += jackstate['Wager']
        return
    else:
        os.system('clear')
        print(your_hand_text)
        print(dealer_hand_text)
        print("It's a tie")
        return

def dealer_doing_his_thing(jackstate):
    dealer_sum = check_sum(jackstate['Dealer'])
    if dealer_sum == 'Bust':
        your_hand_text = 'You: '
        for cards in jackstate['Player']:
            your_hand_text += cards + ' '
        dealer_hand_text = 'Dealer: '
        for cards in jackstate['Dealer']:
            dealer_hand_text += cards + ' '
        os.system('clear')
        print(your_hand_text)
        print(dealer_hand_text)
        print('Dealer busts. You win!')
        jackstate['Gold'] += jackstate['Wager']
        return
    elif dealer_sum == 'Blackjack':
        your_hand_text = 'You: '
        for cards in jackstate['Player']:
            your_hand_text += cards + ' '
        dealer_hand_text = 'Dealer: '
        for cards in jackstate['Dealer']:
            dealer_hand_text += cards + ' '
        os.system('clear')
        print(your_hand_text)
        print(dealer_hand_text)
        print('Dealer has blackjack. You lose')
        jackstate['Gold'] -= jackstate['Wager']
        return
    elif dealer_sum > 16:
        compare_sums(jackstate,dealer_sum)
    else:
        card = random.choice(jackstate['Deck'])
        jackstate['Dealer'].append(card)
        jackstate['Deck'].remove(card)
        dealer_doing_his_thing(jackstate)

def split_options(jackstate):
    if not jackstate['Split']:
        your_hand_text = 'You: '
    elif jackstate['Split'] == 1:
        your_hand_text = 'You (Hand 1 of Split): '
    elif jackstate['Split'] == 2:
        your_hand_text = 'You (Hand 2 of Split): '
    for cards in jackstate['Player']:
        your_hand_text += cards + ' '
    dealer_hand_text = 'Dealer: ' + jackstate['Dealer'][0] + ' *'
    options = "  (1) Hit\n  (2) Stay"
    if same_value(jackstate['Player']) and not jackstate['Split'] and jackstate['Gold'] >= 2*jackstate['Wager']:
        options += "\n  (3) Split"
    os.system('clear')
    print(your_hand_text)
    print(dealer_hand_text)
    if check_sum(jackstate['Player']) == 'Bust':
        print('You busted.')
        jackstate['Gold'] -= jackstate['Wager']
        return
    if check_sum(jackstate['Player']) == 'Blackjack':
        if check_sum(jackstate['Dealer']) == 'Blackjack':
            print('You and the dealer both have blackjack. Tie.')
            return
        else:
            print('Blackjack! You win!')
            jackstate['Gold'] += 1.5*jackstate['Wager']
            return
    print(options)
    choice = raw_input('> ')
    player_choice(jackstate,choice)

def split_hand(jackstate):
    cards = jackstate['Player']
    jackstate['Player'] = {'Hand 1': [cards[0]],
            'Hand 2': [cards[1]]}
    for i in range(1,3):
        hand_name = 'Hand ' + str(i)
        card = random.choice(jackstate['Deck'])
        jackstate['Player'][hand_name].append(card)
        jackstate['Deck'].remove(card)
    new_hands = [jackstate['Player']['Hand 1'],jackstate['Player']['Hand 2']]
    n = 0
    for hands in new_hands:
        n += 1
        jackstate['Split'] = n
        jackstate['Player'] = hands
        split_options(jackstate)
        if n == 1:
            raw_input('')

def player_choice(jackstate,choice):
    if choice == '1':
        card = random.choice(jackstate['Deck'])
        jackstate['Player'].append(card)
        jackstate['Deck'].remove(card)
        player_options(jackstate)
    elif choice == '2':
        dealer_doing_his_thing(jackstate)
    elif choice == '3':
        split_hand(jackstate)
    else:
        print("wrong input")
        choice = raw_input('> ')
        player_choice(jackstate,choice)

def player_options(jackstate):
    if not jackstate['Split']:
        your_hand_text = 'You: '
    elif jackstate['Split'] == 1:
        your_hand_text = 'You (Hand 1 of Split): '
    elif jackstate['Split'] == 2:
        your_hand_text = 'You (Hand 2 of Split): '
    for cards in jackstate['Player']:
        your_hand_text += cards + ' '
    dealer_hand_text = 'Dealer: ' + jackstate['Dealer'][0] + ' *'
    options = "  (1) Hit\n  (2) Stay"
    if same_value(jackstate['Player']) and not jackstate['Split'] and len(jackstate['Player']) == 2 and jackstate['Gold'] >= 2*jackstate['Wager']:
        options += "\n  (3) Split"
    os.system('clear')
    print(your_hand_text)
    print(dealer_hand_text)
    if check_sum(jackstate['Player']) == 'Bust':
        print('You busted.')
        jackstate['Gold'] -= jackstate['Wager']
        return
    if check_sum(jackstate['Player']) == 'Blackjack':
        if check_sum(jackstate['Dealer']) == 'Blackjack':
            print('You and the dealer both have blackjack. Kill Yourself')
            return
        else:
            print('Blackjack! You win!')
            jackstate['Gold'] += jackstate['Wager']
            return
    print(options)
    choice = raw_input('> ')
    player_choice(jackstate,choice)

def place_bet(jackstate):
    os.system('clear')
    print('You currently have ' + str(jackstate['Gold']) + ' Gold.')
    print('How much will you wager, young one?')
    wager = raw_input('> ')
    try:
        wager = float(wager)
    except ValueError:
        print("That's not a number.")
        time.sleep(1.5)
        place_bet(jackstate)
    if not wager.is_integer():
        print 'Get outta here with your decimals chump'
        time.sleep(1.5)
        place_bet(jackstate)
    if wager < 0:
        print 'You sneaky little demon'
        time.sleep(1.5)
        place_bet(jackstate)
    if wager > jackstate['Gold']:
        print('Nice try, guy.')
        time.sleep(1.5)
        place_bet(jackstate)
    else:
        jackstate['Wager'] = wager
    return jackstate

def play_hand(jackstate):
    jackstate['Wager'] = 0
    if len(jackstate['Deck']) < 52:
        os.system('clear')
        print('The decks have been shuffled.')
        time.sleep(2)
        jackstate = reshuffle(jackstate)
    else:
        jackstate = deal(jackstate)
    jackstate = place_bet(jackstate)
    player_options(jackstate)
    return jackstate

################################################################################################
##END OF BLACKJACK SECTION##
################################################################################################

Climb_Events = { 0 : {"Name" : "You must stop climbing for the night due to exhaustion",  "Health Impact" : 10, "Restart" : False, "Done" : False },
                  1 : {"Name" : "You narrowly escape marauders, but are left injured", "Health Impact" : 15, "Restart" : False, "Done" : False },
                  2 : {"Name" : "You are ambushed by deranged mountain goats and must flee", "Health Impact" : 5, "Restart" : False, "Done" : False },
                  3 : {"Name" : "You somehow manage to sprain your leg whilst climbing", "Health Impact" : 20, "Restart" : False, "Done" : False },
                  4 : {"Name" : "You slip and fall off the trail!", "Health Impact" : 5, "Restart" : True, "Done" : False},
                  5 : {"Name" : "You make it up the mountain", "Health Impact" : 0, "Restart" : False, "Done" : True } }

def Mountain_Climb_Room(gamestate):
    os.system('clear')
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "In front of you is a treacherous mountain climb\nWhere to from here?"
    print "(1) Ascend the mountain (2) South"
    choice = raw_input(" > ")
    if "2" in choice:
        gamestate["Current Room"] = "Dirt Road Room"
        exp_call_1(gamestate)
    elif "1" in choice:
        random_gen = random.randint(0, 4)
        random_event = Climb_Events[random_gen]
        print "you begin your climb..."
        time.sleep(2)
        os.system('clear')
        print random_event["Name"]
        time.sleep(2)
        print "You lose " + str(random_event["Health Impact"]) + " health."
        gamestate["Health"] = gamestate["Health"] - random_event["Health Impact"]
        time.sleep(3)
        if random_event["Restart"] is True:
            Mountain_Climb_Room(gamestate)
        else:
            if random_event["Done"] is True:
                pass
                # leads to mountain peak
            else:
                random_gen_two = random.randint(4, 5)
                random_event_two = Climb_Events[random_gen_two]
                os.system('clear')
                print random_event_two["Name"]
                time.sleep(3)
                if random_event_two["Done"] is True:
                    pass
                else:
                    print "You lose " + str(random_event_two["Health Impact"]) + " health."
                    gamestate["Health"] = gamestate["Health"] - random_event_two["Health Impact"]
                    time.sleep(2)
                    Mountain_Climb_Room(gamestate)
            print "You arrive at the peak"
            time.sleep(3)
            os.system('clear')
            gamestate["Current Room"] = "Mountain Peak"
            exp_call_1(gamestate)

    else:
        print "Incorrect input"
        time.sleep(2)
        Mountain_Climb(gamestate)

def Mountain_Peak_Room(gamestate):
    os.system('clear')
    print "Welcome to the Peak of the Mountain"
    print ""
    print "To your left lies a cave, to your right is a wooden sign overlooking a cliff."
    print "(1) Enter the cave (2) Read the sign (3) Easily slide back down the mountain"
    choice = raw_input(" > ")
    if "1" in choice:
        gamestate["Current Room"] = "Mountain Boss"
        exp_call_1(gamestate)
    elif "2" in choice:
        os.system('clear')
        print "You walk closer to the sign."
        time.sleep(1)
        os.system('clear')
        print "It simply reads: Leap of Faith"
        time.sleep(1)
        print "Jump?"
        print "(1) Yes (2) No"
        choice_2 = raw_input(" > ")
        if "2" in choice_2:
            Mountain_Peak_Room(gamestate)
        elif "1" == choice_2:
            print "You jump off the cliff!"
            time.sleep(2)
            gamestate["Current Room"] = "Faith"
            exp_call_1(gamestate)
        else:
            print "Incorrect input"
            time.sleep(1)
            Mountain_Peak_Room(gamestate)
    elif "3" in choice:
        gamestate["Current Room"] = "Mountain Climb"
        exp_call_1(gamestate)
    else:
        print "Incorrect input"
        time.sleep(2)
        Mountain_Peak_Room(gamestate)

def Faith_Room(gamestate):
    faith = int(random.randint(0,2))
    if faith == 0:
        print "You hit the ground with a splat"
        time.sleep(2)
        dead()
    elif faith == 1:
        print "As you plummet towards the ground, something odd happens."
        print ""
        time.sleep(1)
        print "An angel appears in front of you.."
        print ""
        time.sleep(1)
        print "She gives you a warm smile"
        time.sleep(3)
        print "....."
        time.sleep(3)
        os.system('clear')
        print "Welcome to Heaven!"
        print "The angel gives you a Heavenly Sword!"
        gamestate["Inventory"]["Weapon"] = weapons_mythical[0]
        time.sleep(2)
        os.system('clear')
        print "The angel touches your shoulder and you fall asleep....."
        time.sleep(5)
        gamestate["Current Room"] = "Home"
        exp_call_1(gamestate)
    elif faith == 2:
        print "As you plummet towards the ground, something odd happens."
        print ""
        time.sleep(1)
        print "An angel appears in front of you.."
        print ""
        time.sleep(1)
        print "She gives you a smirk"
        time.sleep(3)
        print "....."
        time.sleep(3)
        os.system('clear')
        print "Welcome to Hell!"
        time.sleep(1)
        print "You stand before the devil."
        time.sleep(2)
        os.system('clear')
        print "The devil wants to play a game...\nwith your life as the wager!"
        print "All you must do is solve the following riddle:"
        print "What contains the answer to all questions?"
        choice = raw_input(" > ")
        os.system('clear')
        if "Drosophila" or "drosophila" in choice:
            print "You win this round....\nYou are rewarded with a special weapon."
            gamestate["Inventory"]["Weapon"] = weapons_mythical[1]
            print "The devil knocks you out."
            time.sleep(4)
            gamestate["Current Room"] = "Home"
            exp_call_1(gamestate)
        else:
            print "WRONG ANSWER"
            dead()

def Mountain_Boss_Room(gamestate):
    os.system('clear')
    print "You have " + str(gamestate["Health"]) + " Health, " + str(gamestate["Gold"]) + " Gold, and are level " + str(gamestate["Level"]) + "."
    print "The cave is dark....."
    while bool(gamestate["Inventory"]["Weapon"]) is False:
        x = random.randint(0,number_of_weapons_low)
        assigned_weapon = weapons_low[x]
        gamestate["Inventory"]["Weapon"] = assigned_weapon
        print "You find a " + str(assigned_weapon["Name"]) + " on the ground."
        time.sleep(2)
        pass
    time.sleep(2)
    print "Suddenly, the cave is ablaze with torches!"
    print ""
    print "An enormous Giant appears!"
    enemy = bosses[1]
    gamestate["Current Enemy"]["Name"] = enemy["Name"]
    gamestate["Current Enemy"]["Health"] = enemy["Health"]
    gamestate["Current Enemy"]["Weapon"] = enemy["Weapon"]
    gamestate["Current Enemy"]["Bounty"] = enemy["Bounty"]
    gamestate["Current Enemy"]["Experience"] = enemy["Experience"]
    time.sleep(4)
    gamestate["Current Room"] = "combat"
    gamestate["Cursor Room"] = "Post Boss Room"
    exp_call_1(gamestate)

# Will require slight alterations when more bosses are added
def Post_Boss_Room(gamestate):
    print "You have defeated the " +str(gamestate["Current Enemy"]["Name"]) + "!"
    time.sleep(3)
    if gamestate["Current Enemy"]["Name"] == "Rotted Greatwood Monster":
    if "Forest" in gamestate["Inventory"]["Boss Badges"]:
            pass
    else:
        gamestate["Inventory"]["Boss Badges"].append("Forest")
            print "You've acquired the forest boss badge!"
    time.sleep(3)
    pass
    elif gamestate["Current Enemy"]["Name"] == "Cave Giant":
    if "Mountain" in gamestate["Inventory"]["Boss Badges"]:
            pass
    else:
        gamestate["Inventory"]["Boss Badges"].append("Mountain")
            print "You've acquired the mountain boss badge!"
    time.sleep(3)
    pass
    else:
        print "Glitched"
        time.sleep(2)
    pass
    print "You will now be teleported home."
    time.sleep(3)
    gamestate["Current Room"] = "Home"
    gamestate["Cursor Room"] = ""
    exp_call_1(gamestate)

def dead():
    print "Thank you Zork Souls"
    time.sleep(2)
    exit(0)

def win():
    print "You've collected all the Boss Badges!"
    print "you win baby... for now"
    time.sleep(2)
    exit(0)

exp_call_1(gamestate)
