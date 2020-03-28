import Customer
import DB_interface as DB

#DONT USE ONE TIME ONLY -enan

db = DB.DB_Firestore()
drinks = ["6C 6F 6E 67 20 69 73 6C 61 6E 64 20 20 20 20 20", '77 68 69 74 65 63 6C 61 77 20 20 20 20 20 20 20', "62 75 64 6C 69 67 68 74 20 20 20 20 20 20 20 20", "70 62 72 20 20 20 20 20 20 20 20 20 20 20 20 20", "Corona","Smirrnoff","Titos"]

info = [{'name':"Long Island Iced Tea","percent std. drink":1.2,"price":9.5},{'name':"Whiteclaw","percent std. drink":1,"price":10},{'name':"Bud Light","percent std. drink":0.85,"price":5},{'name':"Pabts Blue Ribbon", "percent std. drink":.87,"price":5},{'name':"Corona","percent std. drink":1.3,"price":4},{'name':"Smirrnoff","percent std. drink":.4,"price":3},{'name':"Titos","percent std. drink":1.0,"price":6}]

for i in range(len(drinks)):
    db.add_data('drinks',drinks[i],info[i])
