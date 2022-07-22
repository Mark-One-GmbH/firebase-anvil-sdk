



def get_multiple_documents():
  from .. import firebase_core
  
  fs = firebase_core.firebase.firestore
  fs.
  q = fs.query(collection(db, "cities"), where("capital", "==", true));
  

#   const querySnapshot = await getDocs(q);
#   querySnapshot.forEach((doc) => {
#     // doc.data() is never undefined for query doc snapshots
#     console.log(doc.id, " => ", doc.data());
#   });
  