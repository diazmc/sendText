from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your twilio account SID"
# Your Auth Token from twilio.com/console
auth_token  = "your Auth token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+41555555555", #Your phone number 
    from_="+4155555555", #Your twilio's number
    body="Hello from Python!")

print(message.sid)