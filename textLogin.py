from twilio.rest import Client
import creds

creds = creds.Credentials()

def sendtext(phone,message):
    account_sid = creds.account_sid
    auth_token = creds.auth_token
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=phone,
        from_=creds.twilionum,
        body=message)
    print("Successfully sent SMS to" + phone)
