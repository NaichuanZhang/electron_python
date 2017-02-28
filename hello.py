
from __future__ import print_function
import time
from flask import Flask, Response, request, render_template, redirect, url_for
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home_page.html")

@app.route("/naiqian")
def hi():
	send_message()
	return "hello from naiqian"

def send_message():
	account_sid = "AC8c82b8a8bad4219098310d27664c0fa8" # Your Account SID from www.twilio.com/console
	auth_token  = "6d27b2410dfdf5748a66ebaef8a69baf"  # Your Auth Token from www.twilio.com/console
	client = TwilioRestClient(account_sid, auth_token)
	message1 = client.messages.create(body="Hello from Python",
                                     to="+12022504356",    # Replace with your phone number
                                     from_="+12196413721") # Replace with your Twilio number
	client = TwilioRestClient(account_sid, auth_token)
	message2 = client.messages.create(body="Hello from Python",
                                     to="+12196285761",    # Replace with your phone number
                                     from_="+12196413721") # Replace with your Twilio number
	print(message1.sid)
	print(message2.sid)


if __name__ == "__main__":
    print('oh hello')
    #time.sleep(5)
    app.run(host='0.0.0.0', port=5000)
