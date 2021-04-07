from twilio.rest import Client

account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = 'b9d35010dbcc4e8747238c8a7fa64222'

client = Client(account_sid, auth_token)

def send_message(message_, from_, to):
    print('whatsappFROM: ' + from_)
    print('whatsappTO: ' + to)

    if 'w' in list(to):
        message = client.messages \
            .create(
            body=message_,
            from_="whatsapp:"+ from_,
            to=to
        )
    else:
        message = client.messages \
            .create(
            body=message_,
            from_="whatsapp:" + from_,
            to="whatsapp:" + to
        )

    '''message = client.messages \
        .create(
        body=message_,
        from_="whatsapp:" + from_,
        to=to
    )'''
