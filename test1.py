from twilio.rest import Client

account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = '0564dd82c87dedf2c130e8db7f5244a8'
client = Client(account_sid, auth_token)


def send_message(message_, from_, to):
    #print('whatsapp:' + from_)
    #print('whatsapp:' + to)
    message = client.messages \
        .create(
        body=message_,
        from_='whatsapp:' + from_,
        to=to
    )

#send_message("Hi there", "+14155238886", "whatsapp:+19142822807")