
'''
Evaluating a purely firestore user server side:
https://firebase.google.com/docs/auth/admin/verify-id-tokens#web
With this mechanism a truly serverless anvil app would be possible.

TODO: 
- convert js dict to python dict
- optional parameter to pass a callback function to get data async
- callback for logout/login event
- orderby, sort, limit startat, startafter
- make server intializable from outside app
- build demo app
- publish to forum!

DONE:
- authenticate with firebase from the anvil user system
- Build in offline caching option
- Transactions
- merge true optional parameter for set statements
- Storage -> store and retrieve blob objects
- Analytics


'''
