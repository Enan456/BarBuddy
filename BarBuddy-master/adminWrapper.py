import Customer
import DB_interface as DB

db = DB.DB_Firestore()

data =  Customer.Customer()

data.processData()
db.add_data('patrons',data.id,data.serializeData())

#db.add_data('patrons',data.fullName,data.serializeData())

