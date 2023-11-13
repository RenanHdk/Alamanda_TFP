from functions.twilio import send_message
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def homepage():
    return "Tudo certo ^_^"

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    try: 
        message = request.form.get('Body', '').strip()
        sender_id = request.form['From']

        send_message(sender_id, "Olá, escolha, 1 ou 2")
        message = request.form.get('Body', '').strip()

        if message.isnumeric()==True:
            message=int(message)
        print(f'message: {message}, tipo: {type(message)}')
        

        if message!=1 or message!=2:
            send_message(sender_id, "Apenas 1 ou 2")
            print(f'message: {message}, tipo: {type(message)}')
        else:
            send_message(sender_id, message)


    except Exception as e:
        print("Erro: ", e)
    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True)

