manu = input("What's the result of Manchester city's match? ")
liv = input("What's the result of Liverpool's match? ")

if manu == 'won' and liv == 'lost' :
    print("Manchester city is the champion of Premier League.")

elif manu == 'lost' and liv == 'won' :
    print("Liverpool is the champion of Premier League.")

elif manu == 'won' and liv == 'won' :
    manu_goal = int(input("What is the margin that Manchester city won by? "))
    liv_goal = int(input("What is the margin that Liverpool won by? "))
    if manu_goal > liv_goal :
        print("Manchester city is the champion of Premier League.")
    elif liv_goal > manu_goal :
        print("Liverpool is the champion of Premier League.")
    elif manu_goal == liv_goal :
        play_off = input("Which team won the play-off match?(Manchester city/Liverpool) ")
        if play_off == 'Manchester city' :
            print("Manchester city is the champion of Premier League.")
        elif play_off == 'Liverpool' :
            print("Liverpool is the champion of Premier League.")
