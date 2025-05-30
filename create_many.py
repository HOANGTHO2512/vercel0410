import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "黎黃壽",
  "mail": "lehoangtho25122004@gmail.com",
  "lab": 933
}
doc_ref = db.collection("靜宜資管").document("jar")
doc_ref.set(doc)
collection_ref = db.collection("靜宜資管")
collection_ref.add(doc)

docs = [
{
  "name": "陳武林",
  "mail": "wlchen@pu.edu.tw",
  "lab": 665
},
{
  "name": "王耀德",
  "mail": "ytwang@pu.edu.tw",
  "lab": 686
},

{
  "name": "康贊清",
  "mail": "tckang@pu.edu.tw",
  "lab": 783
}

]
collection_ref = db.collection("靜宜資管")
for doc in docs:
  collection_ref.add(doc)



