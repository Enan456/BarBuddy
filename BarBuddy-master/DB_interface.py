import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class DB_Firestore:
    def __init__(self):
        #initialize connection
        cred = credentials.Certificate("barbuddy-e6e6d-367c584fae56.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    #@params
    #Collection:either patrons or drinks
    #Document:
    #   -patrons: it is name
    #   -drinks: name of drink or id
    #Data: in json format
    #
    #Function will update or add entry
    #
    def add_data(self, collection, document, data):
        ref = self.db.collection(collection).document(document)
        ref.set(data, merge=True)

    def read_data(self, collection,document):
        doc_ref = self.db.collection(collection).document(document)
        try:
            doc = doc_ref.get()
            return doc.to_dict()
        except google.cloud.exceptions.NotFound:
            return None
