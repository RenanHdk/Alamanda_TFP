from flask import request
from functions.twilio import send_message

def entrada(sender_id, txt):
    send_message(sender_id, txt)
    msg = request.form.get('Body', '').strip()
    return msg

def teste(sender_id):
    msg = entrada(sender_id, "1 ou 2")
    while msg!=1 or msg!=2:
        msg = entrada(sender_id, "apenas 1 ou 2")

