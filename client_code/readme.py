
'''
Evaluating a purely firestore user server side:
https://firebase.google.com/docs/auth/admin/verify-id-tokens#web
With this mechanism a truly serverless anvil app would be possible.

Nice To Have:
- optional parameter to pass a callback function to get data async
- callback for logout/login event

TODO:
- write documentation
- get pending write (offline cache)
- wrap tranaction in class and build in conversion
- startat, startafter
- make server intializable from outside app
- publish to forum!

'''
