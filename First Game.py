health=10
print( "Welcome to Greed Island")
name=input("What's your name?")
age=input("What's your age?")
print("Hello",name,",you're",age, "years old.")
if int(age)>=18:
    print("Ok, you're old enough to play this game. That's cool.")
    want_to_play= input("So, do you want to play?").lower() # im putting the .lower method so that whatever i write will be automatically in lower case
    if want_to_play == "Yes" or "yes" or "Yeah" or "yeah":
        print("Ok, let's get started then.")
        print("You will start with", health,"points of health. If you reach 0 points of health, it will be game over. Don't say i didnt warn you. ")
        left_or_right_choice=input("Your first choice will be to go either left or right... (left/right)")
        if left_or_right_choice=="left":
            print("That's a fine choice. You get to live another day.")
            ans=input("You follow the path and u manage to reach a lake. You can either swim across or go around it (across/around).")
            if ans=="across":
                print("Nicely done. What you didnt know though, is that this lake is filled with pirhanas. You manage to reach the shore somehow, but not unscathed. You will lose 3 points of health.")
                health -= 3
            elif ans=="around":
                print("Very well. You feel like it's better to just go around the lake, although it will take some time to do so. After a couple of hourse u manage to circumvent the lake.")

            ans=input("You leave the lake behind, and u venture into the woods. Here u see a house and a cave. Which way do u want to go (house/cave)?")
            if ans=="house":
                print("You go to the house, and u lose 7 points of health.")
                health-=7
                if health<=0:
                    print("You lost.")
                else:
                    print("U survive.")

            else:
                print("lost")


elif int(age)>=14 and int(age)<18:
    print("Uhm, you are allowed to play, but only with supervision.")
else:
    print("You're too young to play this game, try again once you're at least 18.")
