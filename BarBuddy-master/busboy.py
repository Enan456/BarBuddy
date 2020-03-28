import DB_interface as db
#import lcd
import datetime

DB = db.DB_Firestore()  
inputline = "70 62 72 20 20 20 20 20 20 20 20 20 20 20 20 20"
patron = "lsRrcKiKhN2lWrhF81b7"
drink = DB.read_data('drinks', inputline)
person = DB.read_data('patrons', patron)


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
    lcd.lcd_display("lack of funds!")
    print("lack of funds!")
else:
    if bac > .9:
        lcd.lcd_display("take a break!")
        print("lack of time!")
    else:
        DB.add_data('patrons', patron, {"stdDrink": float(drink.get("percent std. drink")) + float(person.get("stdDrink")),"Budget": int(person.get("Budget")) - int(drink.get("price"))})
        lcd.lcd_display("Cheers!")
        print("cheers!")
