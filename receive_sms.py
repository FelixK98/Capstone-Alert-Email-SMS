import urllib.request
import xml.etree.ElementTree as ET

# data = urllib.request.urlopen('http://127.0.0.1:9501/api?action=receivemessage&username=admin&password=123456&folder=inbox&limit=5&afterdownload=delete').read()
sample_data = '''
<response>
<Envelope>
          <ID>93e36b10-1fce-4648-a059-dbf67ddb66a6</ID>
          <Type>SMS:TEXT</Type>
          <Sender>admin</Sender>
          <Receiver>+3600000000</Receiver>
          <Message>Test000000</Message>
          <SentTime>2010-03-01 16:02:06</SentTime>
          <ReceivedTime>2010-03-01 16:02:06</ReceivedTime>
</Envelope>
<Envelope>
          <ID>85fbb591-c7d2-446c-842d-543984da7ad9</ID>
          <Type>SMS:TEXT</Type>
          <Sender>admin</Sender>
          <Receiver>+3600000002</Receiver>
          <Message>Test000002</Message>
          <SentTime>2010-03-01 16:02:06</SentTime>
          <ReceivedTime>2010-03-01 16:02:06</ReceivedTime>
</Envelope>
</response>
'''

tree = ET.fromstring(sample_data)

userList = tree.findall('Envelope')
for item in userList:
    print(item.find('Message').text)
