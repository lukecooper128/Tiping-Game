import random

score = 0

def clear_screen():
    for i in range(20):
        print()

def gameOver():
    clear_screen()
    print("BOOM! Game Over!")
    print("Final score: " + str(score))

def runEasy():
    global score
    print("running in easy mode")

    #You can add new letters or anything here
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while True:
        letterString = random.choice(letters)
        
        print(letterString)
        playerInput = input()
        
        if playerInput == letterString:
            print("success! +5 score")
            #change how much score you get on easy mode
            score += 5
        else:
            print("WRONG")
            gameOver()
            break

def runHard():
    global score
    print("running in hard mode")

    #You can add new words here
    words = ["PRINT","LUKE","IS","THE","GOAT","QUICK","BROWN","FOX","JUMPS","OVER","LAZY","DOG","SQUARE","FUNCTION","ROOT","CUBE","THE","AND","THAT","HAVE","FOR","NOT","WITH","YOU","THIS","BUT","HIS","FROM","THEY","SAY","HER","SHE","WILL","ONE","ALL","WOULD","THERE","THEIR","WHAT","OUT","ABOUT","WHO","GET","WHICH","WHEN","MAKE","CAN","LIKE","TIME","JUST","HIM","KNOW","TAKE","PEOPLE","INTO","YEAR","YOUR","GOOD","SOME","COULD","THEM","SEE","OTHER","THAN","THEN","NOW","LOOK","ONLY","COME","ITS","OVER","THINK","ALSO","BACK","AFTER","USE","TWO","HOW","OUR","WORK","FIRST","WELL","WAY","EVEN","NEW","WANT","BECAUSE","ANY","THESE","GIVE","DAY","MOST","WAS","ARE","BEEN","HAS","HAD","WERE","SAID","DID","HAVING","MAY","SHOULD","CALL","WORLD","OVER","SCHOOL","STILL","TRY","LAST","ASK","NEED","TOO","FEEL","THREE","WHEN","STATE","NEVER","BECOME","BETWEEN","HIGH","REALLY","SOMETHING","MOST","ANOTHER","MUCH","FAMILY","OWN","OUT","LEAVE","PUT","OLD","WHILE","MEAN","KEEP","STUDENT","WHY","LET","GREAT","SAME","BIG","GROUP","BEGIN","SEEM","COUNTRY","HELP","TALK","WHERE","TURN","PROBLEM","EVERY","START","HAND","MIGHT","AMERICAN","SHOW","PART","ABOUT","AGAINST","PLACE","OVER","SUCH","AGAIN","FEW","CASE","MOST","WEEK","COMPANY","WHERE","SYSTEM","EACH","RIGHT","PROGRAM","HEAR","QUESTION","DURING","WORK","PLAY","GOVERNMENT","RUN","SMALL","NUMBER","OFF","ALWAYS","MOVE","LIKE","NIGHT","LIVE","POINT","BELIEVE","HOLD","TODAY","BRING","HAPPEN","NEXT","WITHOUT","BEFORE","LARGE","ALL","MILLION","MUST","HOME","UNDER","WATER","ROOM","WRITE","MOTHER","AREA","NATIONAL","MONEY","STORY","YOUNG","FACT","MONTH","DIFFERENT","LOT","RIGHT","STUDY","BOOK","EYE","JOB","WORD","THOUGH","BUSINESS","ISSUE","SIDE","KIND","FOUR","HEAD","FAR","BLACK","LONG","BOTH","LITTLE","HOUSE","YES","AFTER","SINCE","LONG","PROVIDE","SERVICE","AROUND","FRIEND","IMPORTANT","FATHER","SIT","AWAY","UNTIL","POWER","HOUR","GAME","OFTEN","YET","LINE","POLITICAL","END","AMONG","EVER","STAND","BAD","LOSE","HOWEVER","MEMBER","PAY","LAW","MEET","CAR","CITY","ALMOST","INCLUDE","CONTINUE","SET","LATER","COMMUNITY","MUCH","NAME","FIVE","ONCE","WHITE","LEAST","PRESIDENT","LEARN","REAL","CHANGE","TEAM","MINUTE","BEST","SEVERAL","IDEA","KILL","BASIS","HEAR","CUT","SURE","WATCH","COLOR","FACE","WOOD","MAIN","OPEN","SEEM","TOGETHER","NEXT","WHITE","CHILDREN","INTEREST"]

    while True:
        wordString = random.choice(words)
        print(wordString)
        playerInput = input()
        
        if playerInput == wordString:
            print("success! +15 score")
            #change how much score you get on hard mode
            score += 15
        else:
            print("WRONG")
            gameOver()
            break

print("Tiping Game - Luke Cooper :D")
desiredGamemode = input("1=easy, 2=hard: ")

if desiredGamemode == "1":
    runEasy()
elif desiredGamemode == "2":
    runHard()
