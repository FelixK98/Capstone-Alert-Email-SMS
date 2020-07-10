import mysql.connector
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request

import Ozekin_api
msg = MIMEMultipart('alternative')
sender = 'suricata.alert@gmail.com'
receiver = 'khoavmse63048@fpt.edu.vn'
msg['Subject'] = 'DECTECT SERIOUS ATTACK FROM SURICATA'
msg['From'] = sender
msg['To'] = receiver

while True:
    time.sleep(1)
    db = mysql.connector.connect(
        host='192.168.10.111',
        user='suricata',
        password='123456',
        database='barnyard2'
    )
    mycursor = db.cursor()
    mycursor.execute('''select convert(event.timestamp,char), sig_name, inet_ntoa(ip_src), inet_ntoa(ip_dst)
from event,signature, iphdr
where signature.sig_priority = 1
and event.cid = iphdr.cid and event.sid = iphdr.sid
and event.signature = signature.sig_id
and event.timestamp between DATE_SUB(now(), INTERVAL 9 second) and now()''')

    result = mycursor.fetchall()

    if len(result) > 0:
        print(result)
        for alert in result:
            # -------SEND EMAIL--------------
            html = """\
        <html>
  <head></head>
  <body>
    <h2 style="color: green;">DATE: {}</p>
    <h2 style="color: red;">ALERT: {}</p>
    <h2 style="color: blue;">IP SOURCE: {}</p>
    <h2 style="color: orange;">IP DESTINATION: {}</p>
  </body>
</html>
""".format(*alert)
            msg.attach(MIMEText(html, 'html'))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, 'kingOF1998')
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()

        # ----------SEND SMS------------------
        message_body = '''
        DATE: {}
        DETECT: {}        
        IP SOURCE: {}
        IP DESTINATION: {}
        '''.format(*alert)
        Ozekin_api.send_sms(message_body)


    time.sleep(7)
