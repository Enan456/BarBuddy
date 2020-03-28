#!/usr/bin/python
import CalcBAC
import Customer
#import drink_add
#import DB_interface as db
import serial, string, time, re, datetime
import DB_interface as db
import lcd

inputLine = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
calc = ''
DB = db.DB_Firestore()
lcd = lcd.lcd_display()

def __main__():
    while True:
      print("----")
      inputLine = " "
      currentCard = None
      currentCustomer = None
      currentDrink = None
      button = 0
      calc = ''
      while inputLine != "":
        inputLine = ser.readline()
        print(inputLine)
        checkDrink = re.search(r"b\' [0-9]", str(inputLine)[:4])
        checkLine = True

        while checkLine:

            if (str(inputLine)[:12] == "b\'Card UID: "):
                CardUID = str(inputLine)[12:23]
            if (str(inputLine) == "b\'1\\r\\n\'"):
                button = 1
            if(str(inputLine)[:5] == "b\' 74"):

                currentCustomer = CardUID
#               CalcBAC(currentCustomer)
                calc += 'a'

                print(currentCustomer)

            elif(checkDrink is not None and str(inputLine)[:4] == checkDrink.group(0)):

                currentDrink = str(inputLine)[3:50]
                drink = DB.read_data('drinks', currentDrink)
                print(currentDrink)
                calc += 'a'

            elif(str(inputLine) == "b\'\'"):
                pass
#                print("no input detected...")

            #process the line depending on what fields are available
 


                

            if(currentCustomer != None and currentDrink != None):
                ## TODO: send drink to customer DB entry
                print("send drink")
                person = DB.read_data('patrons', CardUID)
                if(person.get("gender") == "Male"):
                    BODY_WATER = 0.58
                elif(person.get("gender") == "Female"):
                    BODY_WATER = 0.49
                # Declare constnts
                METABOLISM = 0.017
                SWEDISH_FACTOR = 1.2
                WATER_BLOOD = 0.806
                CONVERT_TO_PERCENT = 10.0
                # run the calculations
                bac = (((WATER_BLOOD *( float(drink.get("percent std. drink")) + float(person.get("stdDrink")) )* SWEDISH_FACTOR ) / (BODY_WATER * float(person.get("weight"))) - (METABOLISM * (int(person.get("initDrink").strftime("%H"))-int(datetime.datetime.now().strftime("%H")))) * CONVERT_TO_PERCENT))

                if(int(person.get("Budget")) - int(drink.get("price"))<=0):
                    lcd.display('lack of funds!')
                    print("lack of funds!")
                else:
                    if bac > .09:
                        lcd.display("take a break!")
                        print("lack of time!")
                    else:
                        DB.add_data('patrons', CardUID, {"stdDrink": float(drink.get("percent std. drink")) + float(person.get("stdDrink")),"Budget": int(person.get("Budget")) - int(drink.get("price"))})
                        lcd.display("Cheers!")
                        print("cheers!")
                # clear fields
                currentCard = None
                currentCustomer = None
                currentDrink = None

            elif(currentCard != None):
            ## TODO: check if entry in DB
            # if entry found: pass

                newUser = Customer()
                newUser.processData(inputLine)
                newUser.printData()

        #temp            db.add_data("Patrons", newUser)
                # clear fields
                newUser = None
                currentCard = None
                currentCustomer = None
                currentDrink = None

            while button == 1:
                newUser1 = Customer.Customer()
                DL = input()
                print(DL)
                newUser1.processData(DL)
                newUser1.printData()
                DB.add_data('patrons',CardUID,newUser1.serializeData())

                button = 0
            checkLine = False





        #inputLine = " "
__main__()
