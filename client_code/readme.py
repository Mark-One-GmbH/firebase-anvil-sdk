
'''
Evaluating a purely firestore user server side:
https://firebase.google.com/docs/auth/admin/verify-id-tokens#web
With this mechanism a truly serverless anvil app would be possible.

TODO: 
- Transactions
- Analytics
- Storage -> store and retrieve blob objects
- convert js dict to python dict
- optional parameter to pass a callback function to get data async
- callback for logout/login event
- merge true optional parameter for set statements
- orderby, sort, limit startat, startafter

DONE:
- authenticate with firebase from the anvil user system
- Build in offline caching option


'''
