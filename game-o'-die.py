
# I, Ranvir Singh, 000819787, certify that all code submitted is my own
# work; that I have not copied it from any other source.  I also certify that
# I have not allowed my work to be copied by others.


#python 3.6.5


import random


def strcheckyes(message):
    #ASSUME message is a string
    #For converting user input to boolean value along with validation
    print(message)
    value=str(input())
    
    strvalid=validcheck(value)
    if not strvalid:
        flag=True
        while flag:
            value=str(input("\n Please state your answer in 'Yes' or 'No', "+ message))
            strvalid=validcheck(value)
            if strvalid:
                flag=False

    flag=simp(value)
    return flag

def strchecky(message):
    #ASSUME message is a string
    #For converting user input to boolean value along with validation
    print(message)
    value=str(input())
    
    strvalid=validcheck1(value)
    if not strvalid:
        flag=True
        while flag:
            value=str(input("\n Please state your answer in 'Y' or 'N', "+ message))
            strvalid=validcheck1(value)
            if strvalid:
                flag=False

    flag=simp(value)
    return flag    

def intvalid(minV,maxV,message,value):
    # ASSUME value is integer
    # ASSUME minV and maxV are valid positive integers, and that min < max
    if value<minV or value>maxV :
    
        while True:
           print(" \nError, Entered value is not a valid positive integer")
           
           value=intcheck(message)
           
           
           if value>=minV and value<=maxV:
               return value
               break
    else:
        return value
def lengthcheck(message):
    #ASSUME message is a string
    print(message)
    value=str(input())
    if len(value)>2:
        while True:
            print("\n Error, Entered value is not a valid positive integer, " , end="")
            print(message)
            value=str(input())
            if len(value)<=2:
                break
    return value
    
def intcheck(message):
    #ASSUME message is a string
    #For checking if the input is a integer or not
    
    value=lengthcheck(message)
    flag=True
    while True:
        for i in value:
            if not(i.isdecimal()):
                print("\n Error, Entered value is not a valid positive integer, " , end="")
                value=lengthcheck(message)
                flag=False
                break
            else:
                flag=True
        if flag:
            break

    value=int(value)
    return value
        
    
    
def diceroll(faces):
    # ASSUME faces is a valid positive integer, greater than 1
    return_value=random.randint(1,faces)
    return return_value
    
def Average(Sum,n):
    # ASSUME n is a valid positive integer, greater than 1
    # ASSUME Sum is a valid positive integer, greater than 0
    return_value=Sum//n
    return return_value

def pattern1(rollturn):
    #ASSUME rollturn is a list of positive integers
    flag=True
    x=0
    while x<((len(rollturn)-1)):
        if rollturn[x]!=rollturn[x+1]:
            flag=False
            break
        x=x+1
    return flag
            
def pattern2(Sum):
    #ASSUME Sum is a positive integer
    flag=True
    x=2
    while x<(Sum-1):
        if Sum%x==0:
            flag=False
            break
        x=x+1
    return flag

def pattern3(average,rollturn):
    #ASSUME average is a positive float
    #ASSUME rollturn is a list of positive integers
    flag=False
    count=0
    x=0
    length=len(rollturn)
    while x<length:
        if rollturn[x]>=average:
            count=count+1
        x=x+1
    if count>(length//2):
        flag=True

    return flag

def pattern4(rollturn):
    #ASSUME rollturn is a list of positive integers
    flag=True
    x=0
    while x<((len(rollturn)-1)):
        if rollturn[x]==rollturn[x+1]:
            flag=False
            break
        x=x+1
    return flag



def bonuscalc(faces,diceNumber,average,rollturn,maxscore,Sum):
    #ASSUME rollturn is a list of positive integers
    #ASSUME Sum,diceNumber,faces,maxscore are positive integers
    #ASSUME average is a positive float
    
    bonusFactor=0
    flag=pattern1(rollturn)
    if faces>=4 and flag:
        bonusFactor=bonusFactor+10
        print("\n Pattern 1 matched as all dice have same number")
        
    if faces<4 and not(flag):
        print("\nPattern 1 doesnot matched!!!! as number of faces are less than 4 \n and all dice are not same ")
    else:
        if faces<4:
            print("\n Pattern 1 doesnot matched!! as number of faces are less than 4")
        else:
            print("\n Pattern 1 doesnot matched!! as all dice are not same")

    flag=pattern2(Sum)
    if maxscore>=20 and flag:
        bonusFactor=bonusFactor+15
        print("\n Pattern 2 matched as sum of dice is a Prime number")
        
    if  maxscore<20 and not(flag):
        print("\n Pattern 2 doesnot matched!!!! as Sum of dice is not a Prime number \n and Max Score is less than 20 ")
    else:
        if maxscore<20:
            print(" \n Pattern 2 doesnot matched!! as Max Score is less than 20")
        else:
            
            print("\n Pattern 2 doesnot matched !! as Sum of dice is not a Prime number ")

       
    if diceNumber>=5 and pattern3(average,rollturn):
        bonusFactor=bonusFactor + 5
        print("\n Pattern 3 matched as half of dice numbers are more than or equal to average")
    
    else:
        if diceNumber<5:
            print("\n Pattern 3 doesnot matched!! as number of dices are less than 5")
        else:
            print("\n Pattern 3 doesnot matched!! either there are not enough dice numbers or they are less than average")

    flag=pattern4(rollturn)
    if diceNumber>4 and faces>diceNumber and flag:
        bonusFactor=bonusFactor + 8
        print(" \n Pattern 4 matched as all dice numbers are different")
        
    if diceNumber<=4 and faces<diceNumber and not(flag):
        print(" \n Pattern 4 doesnot matched!!!! as either number of dice less than 4 or dice number is more than number of faces \n and Dice numbers are not different " )
    else:
        if diceNumber<4 or faces<diceNumber:
            print(" \n Pattern 4 doesnot matched!! as either number of dice less than 4 or dice number is more than number of faces")
        else:
            print("\n Pattern 4 doesnot matched!! as Dice numbers are not different")

    if bonusFactor==0:
        bonusFactor=1
        print(" \n No Patterns matched, Your bonusFactor is "+str(bonusFactor)+ " ")
    else:
        print(" \n Your Bonus factor is "+str(bonusFactor)+" ")

    return bonusFactor


def scorecalc(Sum,maxscore,bonus):
    #ASSUME Sum,bonus,maxscore are positive integers
    return_value= round((((Sum/maxscore)*bonus)+(819787%500)),0)
    return return_value


def nTurn(n):
    #ASSUME n is a positive integer greater than 1
    if n==1:
        print(" \n You played your First turn  COOOL!!!, Let's GO AGAIN")
    elif n==2:
        print(" \n You played your Second turn  AWSOME!!!, Let's DO IT AGAIN")
    elif n==3:
        print(" \n You finished your Third turn  HOORAY!!!, ONCE MORE")
    else:
        print(" \n Not Tired Yet!!! Then, Let's ROCK IT AGAIN")


def validcheck(ans):
    #ASSUME ans is string
     List=["yes","Yes","yEs","yeS","YEs","yES","YeS","YES","no","No","nO","NO"]
     flag=False
     for i in List:
         if ans==i:
            flag=True
        
     return flag

def validcheck1(ans):
    #ASSUME ans is string
    List=["n","N","Y","y"]
    flag=False
    for i in List:
        if ans==i:
            flag=True
        
    return flag


def simp(ans1):
    #ASSUME ans1 is string
    List=["yes","Yes","yEs","yeS","YEs","yES","YeS","YES","Y","y"]
    flag=False
    for i in List:
        if ans1==i:
            flag=True

    return flag



    
        
    
    


    
#main code starts here-->


print("\n\nCOMP 10001-W2020 Final Project by Ranvir Singh, Student Number 000819787 \n Welcome to my dice game, Good Luck!")


message="\n Enter the number of faces [2,20]: "


faces=intcheck(message)
faces=intvalid(2,20,message,faces)



message="\n Enter the number of dice [3,6]: "
diceNumber=intcheck(message)
diceNumber=intvalid(3,6,message,diceNumber)
           
scorelist=[]           
maxscore=faces*diceNumber

rollturn=[]
rollturncopy=[]

turncount=1
reRoll=False
play=True

while play:
    
    print("\n \n TURN No.: "+str(turncount)+"")
    
    if not reRoll:
        rollturn=[]
        rollturncopy=[]
        x=0
        while x<diceNumber:
            rollturn.append(0)
            rollturn[x]=diceroll(faces)
            x=x+1
        
    rollturncopy=rollturn
    
    print("\n \n \n You have rolled : " + str(rollturn))

    Sum=0
    x=0
    while x<(len(rollturn)):
        Sum=Sum + rollturn[x]
        x=x+1

    average=Average(Sum,diceNumber)

    print(" \n These die sum to "+str(Sum)+" and have an average rounded value of "+str(average))

    bonus=bonuscalc(faces,diceNumber,average,rollturn,maxscore,Sum)

    score=scorecalc(Sum,maxscore,bonus)
    if not reRoll:
        scorelist.append(score)
    else:
        scorelist[turncount-1]=score
    

    print(" \n You played it cool, You got "+str(score)+" points")

    

    
    #Reroll code Block
    
    denyFlag=True
    
    message="\n Do you Want to reroll any Dice (Yes , No) "
    rollitflag=strcheckyes(message)
    if rollitflag:
        dicePlace=0
        while dicePlace<diceNumber:
                
            message="  \n Do you want to reroll  dice number " +str(dicePlace+1)+ " which was " + str(rollturn[dicePlace]) +" ? (y,n) "
            
            if strchecky(message):
                rollturn[dicePlace]=diceroll(faces)
                    
            dicePlace=dicePlace+1
            
        message=" \n Are you Sure? (yes,no) "
        denyFlag=strcheckyes(message)
        if not denyFlag:
            rollturn=rollturncopy
            print(" \n OK, previous score will be kept")


    if not denyFlag:
        reRoll=False
    elif not rollitflag:
        reRoll=False
    else:
        reRoll=True
                    
                
     #average of scores  
    if turncount>1 and not reRoll:
        x=0
        scoreSum=0
        avgScore=0
        while x<(len(scorelist)):
            scoreSum=scoreSum + scorelist[x]
            x=x+1
        
        avgScore=Average(scoreSum,(len(scorelist)))
        
        if scorelist[turncount-1]>avgScore :
            print(" \n \n Your score of "+str(scorelist[turncount-1]) +" on turn "+str(turncount)+" is above average.")
        elif scorelist[turncount-1]<avgScore:
            print(" \n \n Your score of "+str(scorelist[turncount-1]) +" on turn "+str(turncount)+" is lower than average.")
        else:
            print(" \n \n Your score of "+str(scorelist[turncount-1]) +" on turn "+str(turncount)+" is average.")
       
    
            

    #end code block
            
    if turncount>1 and not reRoll:
        message="\n Do you want to play another turn (y,n): "
        

        
        if not strchecky(message):
            print(" \n \n You palyed " + str(turncount) +" turns Today with an average score of "+ str(avgScore)+" points ")
            play=False
        else:
            print("\n\n")
            
    if not reRoll and play:
        nTurn(turncount)
        
    if play and reRoll:
        print("\n \n It is a REROLL!!! of turn " +str(turncount)+"!")

        
    if play:
        print("\n\n")
        message=""
    
    if not reRoll:
        turncount=turncount+1

    
