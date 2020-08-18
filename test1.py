from twilio.rest import Client

account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = '6120cce02a157c3a76eff6ca72d98d76'
client = Client(account_sid, auth_token)


def send_message(message_, from_, to):
    print('whatsapp:' + from_)
    print('whatsapp:' + to)
    message = client.messages \
        .create(
        body=message_,
        from_='whatsapp:' + from_,
        to=to
    )
