#
# Python: 3.9.5
#
# Author: Randall Jackson
#
#
# Purpose: First functioning game program built with python.
# You will have the option to be mean or nice to strangers you meet 
# in your travels. Your decisions will determine if people love you
# or hate you if you decide to be nice or mean. 

def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
    Check if this is a new game or not.
    If it is new, get the user's name.
    If it is not new, thank the player for
    Playing again and continue with the game.
    """
    
    # Meaning, if we do not have this user's name,
    # Then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("What is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people.\nYou can choose to be nice or mean")
                    print("But at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nAs stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe strangeer glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables.
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use themk
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nCongratulations! {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    # substitue the {} wildcards with our variable values
    print("\nWow you're Mean, game over! \n{}, everyone thinks you stink and \nyou live in a beat up house, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)
    





if __name__ == "__main__":
    start()
