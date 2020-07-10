import urllib.parse as parse
import urllib.request as request
from urllib.parse import quote
host = 'http://127.0.0.1:9501/api?'
user_params = {
    'username': 'admin',
    'password': '123456',
}


def get_send_sms_params():

    return parse.urlencode({
        'action': 'sendmessage',
        **user_params,
        'recipient': '+84375697417',
        'messagetype': 'SMS:TEXT',
    })


def send_sms(msg):
    print(host + get_send_sms_params() +'&messagedata=' + quote(msg))
    request.urlopen(host + get_send_sms_params() +'&messagedata=' + quote(msg))



def get_receive_sms_params():
    return parse.urlencode({
        'action': 'getmessagelist',
        **user_params,
        'listName': 'inbox'
    })


def receive_sms():
    return request.urlopen(host + get_receive_sms_params()).read()


def get_delete_sms_by_id_params(id):
    return parse.urlencode({
        **user_params,
        'action': 'deletemessagebyid',
        'msgID': id
    })


def delete_sms_by_id(id):
    return request.urlopen(host + get_delete_sms_by_id_params(id))



