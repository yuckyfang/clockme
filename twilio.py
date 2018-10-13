from twilio.rest import Client
import quickstart as qs

# Your Account SID from twilio.com/console
account_sid = "AC9003d1019e9d78a33134c96a71d544af"
# Your Auth Token from twilio.com/console
auth_token  = "bb4e7ed35970afd05361ac79c2b04558"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19178608933",
    from_="+15162611863",
    body=qs.main())

print(message.sid)
