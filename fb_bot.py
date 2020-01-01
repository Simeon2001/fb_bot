import fbchat
from fbchat import Client
client = fbchat.Client('username','password')
no_of_friends = int(1)
for I in range(no_of_friends):
    name = "friend name to chat"
    friends = client.searchForUsers(name)
    friend = friends [0]
    while True:
        msg = str(input("message :  "))
        sent = client.sendMessage(msg,thread_id=friend.uid)
        if sent:
            print ("message sent")
    else:
        break
        
         