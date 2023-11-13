from functions.openai import get_result
from functions.twilio import send_message
from functions.teste import teste
from flask import Flask, request


app = Flask(__name__)

def inputM(sender_id, txt):
    send_message(sender_id, txt)
    return request.form['Body']


@app.route("/")
def homepage():
    return "Tudo certo ^_^"

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    try: 
        sender_id = request.form['From']
        print(f'Número de quem enviou: {sender_id}')
        teste(sender_id)
        # try:
        #     result = get_result(message)
        #     print(result)
        #     send_message(sender_id, result)
        # except Exception as e:
        #     print("Erro: ", e)
    except Exception as e:
        print("Erro: ", e)
    return 'OK', 200