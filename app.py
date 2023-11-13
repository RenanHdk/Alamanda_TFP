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
        sender_id = request.form['From']
        send_message(sender_id, "1 ou 2")
        message = request.form.get('Body', '').strip()
        message1 = request.form['Body']
        print(f'message: {message}', f'message1: {message1}', sep='\n')
        if message!=1 or message!=2:
            send_message(sender_id, "Apenas 1 ou 2")
        else:
            send_message(sender_id, message)


        # message = request.form['Body']

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


