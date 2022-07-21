


import anvil.js
initializeApp = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-app.js")
firestore = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-firestore.js")


firebaseConfig = {
  'apiKey': "AIzaSyBv8XOOpjNqOupqY6BOMeMuasWb6okUy-g",
  'authDomain': "markone-qa.firebaseapp.com",
  'projectId': "markone-qa",
  'storageBucket': "markone-qa.appspot.com",
  'messagingSenderId': "133733330920",
  'appId': "1:133733330920:web:0c373a61b08e6273363e5d",
  'measurementId': "G-R08RY8P8YR"
}

app = initializeApp.initializeApp(firebaseConfig)
db = firestore.getFirestore(app)

query = firestore.query(firestore.collection(db, "global_settings")) #, where("capital", "==", true))
querySnapshot = firestore.getDocs(query)

for doc in querySnapshot:
  print(doc)
