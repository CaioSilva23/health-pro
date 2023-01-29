from decouple import config
from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def envia_sms(contato):

    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    remetente = config('NUMERO')  # REMETENTE OBS: NÚMERO DA CONTA TWILLO
    destino = contato  # DESTINATÁRIO, NECESSÁRIO CADASTRAR DESTINATÁRIO NO TILLO

    message = client.messages.create(
        from_=remetente,
        body='PRECISO DE AJUDA',
        to=destino
    )
    
