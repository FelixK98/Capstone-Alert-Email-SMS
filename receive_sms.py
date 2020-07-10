import urllib.request
import xml.etree.ElementTree as ET
import time
from urllib.parse import quote
import Ozekin_api
while True:
    #retrieve msg list
    data = Ozekin_api.receive_sms()
    modified_data = '<Content>' + data.decode() + '</Content>'

    tree = ET.fromstring(modified_data)

    userList = tree.findall('Envelope')
    for item in userList:
        print(item.find('Sender').text)
        if 'BLOCK' in item.find('Message').text.upper() and  item.find('Sender').text == '+84375697417':
            # get ip to block
            ip = item.find('Message').text.upper().split()[1]
            # call server to block ip
            urllib.request.urlopen('http://192.168.10.10:7000/add/' + ip)

            # Reply after block
            Ozekin_api.send_sms(f'BLOCK IP {ip} SUCCESSFULLY')
        # delete message after read
        delete_result = Ozekin_api.delete_sms_by_id(item.find('ID').text)
        print(delete_result.read().decode())
    time.sleep(2)

