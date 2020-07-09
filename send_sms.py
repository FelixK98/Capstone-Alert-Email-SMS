

import urllib.request
from urllib.parse import quote



host = "http://127.0.0.1"

user_name = "admin"

user_password = "123456"

recipient = "+84901794484"

message_body = "Hello World from Python"






http_req = host

http_req += ":9501/api?action=sendmessage&username="

http_req += quote(user_name)

http_req += "&password="

http_req += quote(user_password)

http_req += "&recipient="

http_req += quote(recipient)

http_req += "&messagetype=SMS:TEXT&messagedata="

http_req += quote(message_body)


print(http_req)


# get = urllib.request.urlopen(http_req)
#
# req = get.read()
#
# get.close()



################################################

###        Verifying the response            ###

################################################

print(req)

# if req.find("Message accepted for delivery") > 1:
#
#     print ("Message successfully sent")
#
# else:
#
#     print ("Message not sent! Please check your settings!")

