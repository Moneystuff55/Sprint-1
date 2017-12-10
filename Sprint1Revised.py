print("Robo_Pocalypse")
print("")
print("     By       ")
print("")
print("Jacob Lorenzo")
print("")
print("In a world where an AI has taken over, you are one of the last humans left on"+
"this desolate world with nothing but robots patrolling the streets."+
"Your goal is to take down the AI and save what is remaining of humanity.")
print("")
fName = input("What is your first name?")
print("")
lName = input("What is your last name?")
print("")
print("Hello" + " "+ fName + " " + lName)
print("")

choicesDictionary = {
    'ChoiceINIT' : 'Escape / Fight',
    'Choice0' : 'Play Dead/Negotiate',
    'Choice1' : 'Play Dead/Negotiate',
    'Choice00' : 'Wait/Break Restraints',
    'Choice11' : 'Pickpocket guard/Escape through vent',
    'Choice110' : 'Fight / Find other way',}

storyDictionary = {
    '0':'You climb through the window, but realize the house is surrounded, you are grasped arround the torso by a robot and are carried through the desert.',
    '1':'You swing the door open with a crowbar in hand, but as soon as the door opens, a metallic hand grips your wrist firmly you are then dragged across the desert remains of this world to an unknown place.',
    '10':'You try to play dead, but they thought you actually died, they vaporize your body',
    '01':'You negotiate with them, they let you go, but they said if you cause anymore trouble for them, they will kill you. In return they will make sure no harm comes to you. The AI lives, but you do too, so win win?',
    '00':'You try to play dead, but they kick you to keep you awake, you are being transferred to a laboratory where they experiment on humans. You are restrained in a chair and told the surgeon will be here shortly.',
    '11':'You try to negotiate, but they tell you to keep quiet. You are dragged to a prison, coincidentally the AI is here also. You are put into a single cell with a guard outside, there is a vent, the cover is weakly put on.',
    '001':'You break free from the restraints, the surgeon arrives and you shut down the robot by ripping out its wires. You escape to the desert where you have some options.',
    '110':'You pickpocket the guard, then shoot the guard, bust the cell door by vaporizing it as you walk down the hall, you hear clanking ahead, must be a hall of guards',
    '000':'You decided to wait, the surgeon is actually an undercover robot working for the resistance. He lets you go, but you cannot persue the AI, it is the resistances job now.',
    '111':'You try to climb up ,but the guard rushes in and vaporizes you.'}

ID = []
turnCounter = 0
noteWrite = None

choiceConverted = (''.join(str(ID) for ID in ID))

initialStory = ["While you are sleeping, you wake up hearing a knocking at the door, it might be humans, but it could also be the robots."+" "+
"Then you hear them say"+" " +fName+" "+lName+" "+"are you there?"+" You have a crowbar, but if it is a human, you might injure them, but if its a robot, they will most likely kill you before you damage their machinery."]

print(initialStory)

print(choicesDictionary['ChoiceINIT'])

choiceConverted = (''.join(str(ID) for ID in ID))

def listJoiner():
   print (''.join(str(ID) for ID in ID))

def appendZero():
    generalInput = None
    ID.append(0)

def appendOne():
    generalInput = None
    ID.append(1)

def choiceandStory():
    choiceConverted = (''.join(str(ID) for ID in ID))
    Choice = 'Choice' + choiceConverted   
    a = (storyDictionary[choiceConverted])
    print (a)

    if Choice in choicesDictionary:
        b = (choicesDictionary[Choice])
        print (b)
        
    if choiceConverted == '111' or choiceConverted == '11010' or choiceConverted == '11011' or choiceConverted == '11000' or choiceConverted == '11001' or choiceConverted == '10' or choiceConverted == '01' or choiceConverted == '000' or choiceConverted == '0010' or choiceConverted == '00110' or choiceConverted == '00111':
        quit()
        
while (turnCounter < 3):
    
    turnCounter = turnCounter + 1
    generalInput = input("What is your choice?")
    
    if generalInput == "0":
            appendZero()
            listJoiner()
            choiceandStory()
            
    elif generalInput == "1":
            appendOne()
            listJoiner()
            choiceandStory()
            
    elif generalInput == "2":
            generalInput = None
            notepad = input("What would you like to keep a note of?")
            noteWrite.append(notepad)
            
    elif generalInput == "3":
            print(noteWrite)    
        

