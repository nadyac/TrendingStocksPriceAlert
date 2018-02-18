from twilio.rest import Client

def process(path):
	print(path)
def setAlert(params):
	process(params)
	# Your Account SID from twilio.com/console
	account_sid = "AC805fbc5f452cd5a175c2df46b07b70f4"
	# Your Auth Token from twilio.com/console
	auth_token  = "56c2940e7140db799e623a03ec281786"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+12019262482", #TODO make this dynamic
	    from_="+12015966491",
	    body="You have set up a price alert!")

	print(message.sid)
