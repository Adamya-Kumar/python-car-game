import dice

dice1=dice.Dice()
dice1.roll()


i=1
while i <= 3:
    commad = input(">")
    commad=commad.lower()
    if commad == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
        user_commad = ''
        flag=-1
        while user_commad != 'quit':
            user_commad=input(">")
            user_commad=user_commad.lower()
            if user_commad == 'start' :
                if flag == 1:
                    print("Car already started..")
                    continue
                print("Car started...Ready to go!")
                flag=1
            elif user_commad == 'stop' :
                if flag == 0:
                    print("Car already  stoped")
                    continue

                print("Car stopped")
                flag=0
            elif user_commad == 'quit':
                flag=-1
                commad = user_commad
            else:
                print("I don't understand that...")
        break
    else:
        print("Try Again , type help to start ")
    i+=1
if i == 3:
    print("Limit reach load the progam")
