from app import inputM
from functions.twilio import send_message

def teste(sender_id):
    msg = inputM(sender_id, "1 ou 2 ?")
    while(msg!=1 or msg !=2):
        msg = inputM(sender_id, "Entrada inválida, 1 ou 2 APENAS")
    send_message(msg)