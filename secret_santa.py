import smtplib
import random
import json

config = json.load(open('creds.json'))
from_email = config['username']
password = config['password']
admin = config['admin']
subject = "Secret Sanata 2022"
admin_msg=f"Subject: {subject}\n\nHi,\n\nPFB the matches for Secret Sanata 2022\n\n"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)

final_match={}
data=json.load(open('members.json'))

for member in data['members']:
    to_email = member['mail']
    to_name = member['name']
    gift_to = random.choice([i for i in data['members'] if i != member and i['name'] not in final_match])['name']
    final_match[gift_to]=to_name

    body=f"Hi {to_name},\n\nYou will be the secret santa for {gift_to}\n\nRegards,\nSanta"
    message=f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    
for match in final_match:
    admin_msg=admin_msg+final_match[match]+" --> "+match+"\n"
admin_msg=admin_msg+"\n\nRegards,\nSanta"
server.sendmail(from_email, admin, admin_msg)

print('Emails sent')