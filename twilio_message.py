from twilio.rest import TwilioRestClient

account_sid = "AC8c82b8a8bad4219098310d27664c0fa8" # Your Account SID from www.twilio.com/console
auth_token  = "6d27b2410dfdf5748a66ebaef8a69baf"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
                                     to="+12022504356",    # Replace with your phone number
                                     from_="+12196413721") # Replace with your Twilio number

print(message.sid)
