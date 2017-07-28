from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC74ea816ff63cf107bd4026f443becfac"
# Your Auth Token from twilio.com/console
auth_token  = "bf3938d1e41fc317a3a2dc372cc51a97"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14037108679", 
    from_="+4037108679",
    body="Hello from Python!")

print(message.sid)
