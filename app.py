from functions.twilio import send_message
from flask import Flask, request



app = Flask(__name__)

# def filtro(sender_id):
#     send_message("1 ou 2 ?")


@app.route("/")
def homepage():
    return "Tudo certo ^_^"

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    fluxo_conversa = 0
    try: 
        #Mensagem para iniciar conversa
        message = request.form.get('Body', '').strip()
        sender_id = request.form['From']

        if fluxo_conversa==0:
            send_message(sender_id, "Olá, escolha, 1 ou 2")
            fluxo_conversa = 1

        elif fluxo_conversa==1:
            if message.isnumeric() and int(message)==1 or int(message)==2:
                fluxo_conversa = 2    
            else:
                fluxo_conversa = 3

        elif fluxo_conversa==2:
            send_message("Boua (0 _ 0)")

        elif fluxo_conversa==3:
            send_message("Escreve certo burrão, 1 ou 2 ?")
            fluxo_conversa==1
    except Exception as e:
        print("Erro: ", e)
    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True)
