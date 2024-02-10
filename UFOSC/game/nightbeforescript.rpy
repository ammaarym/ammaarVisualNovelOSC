# Characters
define p = Character("Python")
define c = Character("C++")
define j = Character("Java")

# Backgrounds
image bg dorm_room = "backgrounds/bg dorm_room.jpg"
image bg university_campus = "backgrounds/bg university_campus.jpg"

# Screens
image vending_machine = "images/vending_machine.png"
image room_service_menu = "images/room_service_menu.png"

# The game starts here.
label start:
    # INTRODUCTION

    "It's the night before orientation at the University of Byteborough. An exciting journey awaits!"

    $ mc = renpy.input("Your name: ").strip()

    "Your name is [mc]."

    # Set the scene
    show bg dorm_room with fade

    "[mc]" "Man, I can't believe it, I'm really starting my first day at University of Byteborough. I can't wait for everything I'm going to experience, all the parties, friends, clubs, and ladies! (...if i can even talk to them), my real college life starts tomorrow!!"
    "[mc]" "I’m tired from the drive here, 4 hours was brutal. I’m glad I didn’t have to fly here though, I definitely don’t have the money for that. I am super grateful my parents gave me this car to take to college, I would be lost without it. They also gave me $50 to get through the weekend."

    # Stomach rumbles
    "[mc]" "*Stomach rumbles* Oh man I’m hungry, I guess being on the road all day will do that to you. What should I get to eat?"

    # Choice for food
    menu:
        "Vending Machine":
            vending_machine_choice()
            "You chose Vending Machine"
        "Room Service":
            room_service_choice()
            "You chose Room Service"
        "Doordash":
            doordash_choice()
            "You chose Doordash"

label vending_machine_choice:
    show vending_machine

    # Vending Machine Choice
    "[mc]" "I think I will go downstairs to the vending machine, I could really go for a Snickers bar and a bag of Doritos right now. And, I will save some money, you never know when you will need it. But, I am pretty hungry maybe I should eat some more to fuel my body and mind."
    # AFFECTS: Money, PERL
    # Continue to next choice

    # Interaction with Perl
    show bg university_campus with fade

    p "Hey there! My name is Perl! Do you go to UB?"
    menu:
        "Friendly":
            friendly_interaction()
        "Flirty":
            flirty_interaction()
        "Rude":
            rude_interaction()

# Define interactions based on choices
label friendly_interaction:
    "[mc]" "Yeah I do, my name is [mc], nice to meet you! What major are you?"

    p "*Smiles* I am a computer science major, what about you?"

    "[mc]" "Oh my gosh, me too! I am hoping to take programming 1 this semester, are you as well?"

    p "Yes, I have some programming experience from highschool, but I am excited to start learning."

    p "Well anyway, I have to get back to my room so I can get a good night's sleep. See you later!"
    # Perl leaves
    return

label flirty_interaction:
    "[mc]" "Yeah, I do, my name is [mc]. What’s your room number?"

    p "Uh, what?"

    "[mc]" "I was just thinking we could finish this conversation in your room *smirk*"

    p "No, I don’t think I want to do that. But it was nice to meet you!"
    # Perl walks away

    "[mc]" "Whatever, she wasn’t even pretty anyway. I don’t care. I have never met someone so self-centered and rude!"
    return

label rude_interaction:
    "[mc]" "Uh yeah, what’s it to you?"

    p "Well I go there too. I was... I just thought we might have something in common…"

    "[mc]" "You thought wrong. Why would someone like me have something in common with someone like you?"

    p "Oh. Okay. Sorry to bother you…"

    "[mc]" "I do not have time to be talking to girls like that…"
    return
    # Perl leaves, feeling hurt

label room_service_choice:
    "[mc]" "I know, I will get room service, nothing beats hotel room service. People bring me fresh hot food, and I don’t even have to do dishes."

    "[mc]" "*Looking at menu* Well I don’t even know what I want, there are so many options…"

    # AFFECTS: Money

    menu:
        "Burger":
            order_burger()
        "Mac and Cheese":
            order_mac_and_cheese()
        "Chicken Fingers":
            order_chicken_fingers()
        "Pizza":
            order_pizza()

label order_burger:
    "[mc]" "Yeah, I have to get a burger, you can’t go wrong with that."

    # Wait for the order
    "[mc]" "*5 minutes pass* I hope this doesn’t take too long I am getting pretty hungry here"

    # Food arrives
    "[mc]" "*Knock on door* Oh man, thank goodness"

    "[mc]" "Thank you man, that was so fast!"

    return

label order_mac_and_cheese:
    "[mc]" "Yeah, I have to get mac and cheese, you can’t go wrong with that."

    # Wait for the order
    "[mc]" "*5 minutes pass* I hope this doesn’t take too long I am getting pretty hungry here"

    # Food arrives
    "[mc]" "*Knock on door* Oh man, thank goodness"

    "[mc]" "Thank you man, that was so fast!"

    return

label order_chicken_fingers:
    "[mc]" "Yeah, I have to get chicken fingers, you can’t go wrong with that."

    # Wait for the order
    "[mc]" "*5 minutes pass* I hope this doesn’t take too long I am getting pretty hungry here"

    # Food arrives
    "[mc]" "*Knock on door* Oh man, thank goodness"

    "[mc]" "Thank you man, that was so fast!"

    return

label order_pizza:
    "[mc]" "Yeah, I have to get pizza, you can’t go wrong with that."

    # Wait for the order
    "[mc]" "*5 minutes pass* I hope this doesn’t take too long I am getting pretty hungry here"

    # Food arrives
    "[mc]" "*Knock on door* Oh man, thank goodness"

    "[mc]" "Thank you man, that was so fast!"

    return


label doordash_choice:
    "[mc]" "I passed Chipotle like fifteen times on the way here, I bet I can order some for delivery."

    "[mc]" "*15 minutes later* This driver sucks! I ordered this 30 minutes ago and he still hasn’t picked it up!!!"

    "[mc]" "*20 minutes later* Uuuugggghhhhh. I’m so hungry. Can this loser hurry up? It isn’t that hard to deliver food."

    "[mc]" "*20 more minutes later, there is a knock at the door* Finally!"

    css "Here you go."

    "[mc]" "*Upset/Annoyed/Stern* What took you so long?"

    css "*Sigh* Orientation is tomorrow, everyone is ordering food."

    "[mc]" "Whatever man, at least you finally got here"

    menu:
        "Tip the Driver":
            tip_driver()
        "Don't Tip the Driver":
            dont_tip_driver()

label tip_driver:
    css "Your total is $30."

    "[mc]" *Hands over 35 dollars* "Keep the change I guess, have a good one."

    css "Mhm."

    "[mc]" *Shouts* "You’re welcome!"

    "[mc]" *To themselves* "Some people are just awful…"

    return

label dont_tip_driver:
    css "Your total is $30."

    "[mc]" *Hands over 30 dollars* "Here."

    css "What? No tip? Are you kidding me?"

    "[mc]" "You took eight years to get me my food."

    "[mc]" "Get lost old man."

    "[mc]" *Looks inside the Chipotle bag* *Shocked and angry* "WHERE ARE MY CHIPS AND QUESO????"

    return


# Next scene
label after_eating:
    "[mc]" "Man that hit the spot. What am I going to do with the rest of my night?"

    "[mc]" "I know I will play some Valorant, I have been grinding to go from silver to gold."

    "[mc]" "Now I am Silver III! I just have to win a few more games to push to gold! Do I play one more ranked game on Valorant so I can get gold rank? Or do I head to bed early so I'm not late in the morning? I have to make big decisions tomorrow when"

    menu:
        "Gaming Grind":
            gaming_grind()
        "Sleep Early":
            sleep_early()

label gaming_grind:
    "[mc]" "Wow, that was miserable. I went back and forth for 4 hours, and sacrificed my pride and rank. Now It’s 3:30, I have deranked to Silver I, and I am so tired. I am literally never going to play this game ever again..."

    return

label sleep_early:
    "[mc]" "*Shift, turn, shift,..,roll* Jeez, I can't seem to get comfy enough to get some sleep. Maybe I'll watch some YouTube until I feel tired…"
    # *Show time lapse of time passing and youtube videos watch count increasing at 20 minute time intervals.*
    # *Finish with a picture of him passed out at 3:30 with his phone still playing videos, next to him.*
    return
