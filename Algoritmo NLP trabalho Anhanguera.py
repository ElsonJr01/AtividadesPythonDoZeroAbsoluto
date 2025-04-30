import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob

nltk.download('stopwords')
nltk.download('punkt')

pares = [
    ['Oi', ['Ola', 'Ola, como posso ajudar']],
    ['Como voce esta', ['Estou bem, obrigado. E voce', 'Tudo bem']],
    ['Quem e voce', ['Sou seu professor virtual', 'Me chame de Prof']],
    ['Qual e o seu objetivo', ['Meu objetivo e ajudar a responder suas perguntas', 'Estou aqui para te ensinar']]
]

chatbot = Chat(pares, reflections)

def chat():
    print("Ola Digite 'sair' para encerrar o chat")
    while True:
        mensagem = input("Voce: ")
        if mensagem.lower() == 'sair':
            print("Chat encerrado")
            break
        resposta = chatbot.respond(mensagem)
        if resposta:
            print("Chatbot: ", resposta)
        else:
            print("Chatbot: Desculpe, nao entendi. Pode repetir de outra forma?")

chat()

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    if polaridade > 0:
        return "Isso parece positivo"
    elif polaridade < 0:
        return "Isso parece negativo"
    else:
        return "Nao consigo determinar o sentimento com certeza"

mensagem_usuario = input("Digite algo para analise de sentimento: ")
resultado_sentimento = analisar_sentimento(mensagem_usuario)
print("Analise de Sentimento: ", resultado_sentimento)

