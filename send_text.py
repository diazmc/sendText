from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC16aa94f48317c5301fb2835b3418571d"
# Your Auth Token from twilio.com/console
auth_token  = "49624729da90cad3306f328c000b90fe"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+41555555555", #Your phone number 
    from_="+4155555555", #Your twilio's number
    body="Hello from Python!")

print(message.sid)