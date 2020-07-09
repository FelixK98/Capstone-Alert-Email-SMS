import urllib.request
import xml.etree.ElementTree as ET
import time
from urllib.parse import quote
while True:
    data = urllib.request.urlopen('http://127.0.0.1:9501/api?action=getmessagelist&username=admin&password=123456&listName=inbox').read()
    modified_data = '<Content>' + data.decode() + '</Content>'

    tree = ET.fromstring(modified_data)

    userList = tree.findall('Envelope')
    for item in userList:
        if 'BLOCK' in item.find('Message').text.upper():
            # get ip to block
            ip = item.find('Message').text.upper().split()[1]
            # call server to block ip
            urllib.request.urlopen('http://192.168.10.10:7000/add/' + ip)

            # Reply after block
            sms_host = "http://127.0.0.1"
            user_name = "admin"
            user_password = "123456"
            recipient = "+84375697417"
            message_body = 'BLOCK SUCCESSFULLY'
            http_req = sms_host
            http_req += ":9501/api?action=sendmessage&username="
            http_req += quote(user_name)
            http_req += "&password="
            http_req += quote(user_password)
            http_req += "&recipient="
            http_req += quote(recipient)

            http_req += "&messagetype=SMS:TEXT&messagedata="

            http_req += quote(message_body)

            get = urllib.request.urlopen(http_req)
            get.close()
        # delete message after read
        delete_result = urllib.request.urlopen('http://127.0.0.1:9501/api?action=deletemessagebyid&username=admin&password=123456&msgID=' + item.find('ID').text)
        print(delete_result.read().decode())
    time.sleep(1)

