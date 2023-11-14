from functions.twilio import send_message
from flask import Flask, request


fluxo_conversa = 0


app = Flask(__name__)

# def filtro(sender_id):
#     send_message("1 ou 2 ?")


@app.route("/")
def homepage():
    return "Tudo certo ^_^"

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    global fluxo_conversa
    try: 
        #Mensagem para iniciar conversa
        message = request.form.get('Body', '').strip()
        sender_id = request.form['From']
        print(f"fluxo conversa: {fluxo_conversa}")
        if fluxo_conversa==0:
            send_message(sender_id, "Olá, escolha, 1 ou 2")
            fluxo_conversa = 1

        elif fluxo_conversa==1:
            if message.isnumeric():
                if int(message)==1 or int(message)==2:
                    send_message(sender_id, "Boua (0 _ 0)")
                    fluxo_conversa = 0                
                else:
                    send_message(sender_id, "Escreve certo burrão, 1 ou 2 ?")
            else:
                send_message(sender_id, "Escreve certo burrão, 1 ou 2 ?")

    except Exception as e:
        print("Erro: ", e)
    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True)
