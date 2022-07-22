



def get_multiple_documents():
  from .. import firebase_core
  
  #get the firestore instance
  fs = firebase_core.firebase.firestore
  #reference to the collection 'test'
  test_ref = fs.get_ref('test') 
  #create a query
  query = fs.query(test_ref, fs.where("capital", "==", True));
  
  #execute the query
  for doc in fs.getDocs(query):
    print(doc)
    print(doc.data())
#   snapshop = await getDocs(q);
#   querySnapshot.forEach((doc) => {
#     // doc.data() is never undefined for query doc snapshots
#     console.log(doc.id, " => ", doc.data());
#   });
  