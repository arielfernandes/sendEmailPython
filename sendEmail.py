import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Configuração
host = 'smtp.gmail.com'
port = 587
user = input("Informe seu usuário: ")
password = input("Informe a senha: ")
subject_msg = input("Informe o assunto: ")
toMail = []

c = True

while c:
    toMail.append(input('Informe o E-mail a ser enviado: '))
    x = input("\nDeseja Continuar? [s/n]\n >>> ")
    if x.lower() == "n":
        c = False
# print(toMail)

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
for i in toMail:
    message = 'Olá, mundo!'
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = i
    email_msg['Subject'] = subject_msg
    # print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()
