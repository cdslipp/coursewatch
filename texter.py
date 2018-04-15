from twilio.rest import Client

def sendtext(phone,message):
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=phone,
        body=message)
    print("Successfully sent SMS to")
