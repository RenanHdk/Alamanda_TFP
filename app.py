from functions.openai import get_result
from functions.twilio import send_message
from functions.teste import teste
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def homepage():
    return "Tudo certo ^_^"

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    try: 
        # message = request.form['Body']
        sender_id = request.form['From']
        teste(sender_id)
        # print(f'Mensagem: {message}', f'Número de quem enviou: {sender_id}')
        # try:
        #     result = get_result(message)
        #     print(result)
        #     send_message(sender_id, result)
        # except Exception as e:
        #     print("Erro: ", e)
    except Exception as e:
        print("Erro: ", e)
    return 'OK', 200