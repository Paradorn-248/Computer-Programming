choice = input('Is Bulotelli injured?(y/n) ')
if choice == 'y' :
    print('Not available')
else :
    choice = input('Is Bulotelli late for the training?(y/n) ')
    if choice == 'y' : 
        choice = input('Did Bulotelli perform well in training?(y/n) ')
        if choice == 'y' :
            print('Substitute')
        else : 
            print('Not selected')
    else :
        print('Starter')