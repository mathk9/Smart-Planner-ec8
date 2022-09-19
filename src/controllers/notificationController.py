import webbrowser
from win10toast_click import ToastNotifier
from src.server.instance import server
from src.models.notification import notification

app, api = server.app, server.api

notification_db = [
    {'id': 0, 'name': 'Tomar café da manhã', 'description': 'Uva na geladeira', 'status': 'Em progresso'},
    {'id': 1, 'name': 'Escovar os dentes', 'description': 'Escova azul', 'status': 'Feito'},
    {'id': 2, 'name': 'Remédio Pressão', 'description': 'Capsula azul e branca, caixa 3', 'status': 'Não feito'},
]

tarefa = notification_db['name']
status = notification_db['status']

ITEM_NOT_FOUND = "Task not found."


#Parte de enviar a notificação (no w10)
page_url = 'https://www.youtube.com/watch?v=e9hqMkNvNXA'

def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Abrindo aplicativo')
    except:
        print('Falha ao tentar abrir o aplicativo')

if status == 'Não feito':

    notification = ToastNotifier()

    notification.show_toast(
        "URGENTE",
        "Idoso não concluiu a tarefa",
        #icon_path=, serve para colocar icone na notificação
        duration=10,
        threaded=True,
        callback_on_click=open_url,
    )


#Parte de enviar a notificação (no email)
import smtplib
import email.message

def enviar_email(tarefa):
    corpo_email = f"""
    <p>O idoso não concluíu a tarefa proposta para ele: {tarefa}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Urgente, Idoso não concluiu a tarefa"
    msg['From'] = 'emaildoapp@gmail.com'
    msg['To'] = 'emaildocuidador@gmail.com'
    password = 'senha do email do app'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if status == 'Não feito' :
    enviar_email(tarefa)