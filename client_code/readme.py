
'''
Evaluating a purely firestore user server side:
https://firebase.google.com/docs/auth/admin/verify-id-tokens#web
With this mechanism a truly serverless anvil app would be possible.

Nice To Have:
- optional parameter to pass a callback function to get data async
- callback for logout/login event

TODO:
- get pending write (offline cache)
- wrap tranaction in class and build in conversion
- orderby, sort, limit startat, startafter
- make server intializable from outside app
- check in with official python sdk
- build demo app
 xcfv
 
- publish to forum!

DONE:
- converter js dict to python dict
- authenticate with firebase from the anvil user system
- Build in offline caching option
- Transactions
- merge true optional parameter for set statements
- Storage -> store and retrieve blob objects
- Analytics


'''
