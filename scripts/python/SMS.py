from twilio.rest import Client

# Parse the path requested to extract the alert symbol to include in the SMS
def getSymbol(path):
	symbol = path[len("/setAlert?alertSymbol="):-len("&toNumber=2223334444")]
	return symbol

# Parse the path requested to extract the phoneNumber to send the SMS to
def getPhoneNumber(path):
	splitPath = path.split("&")
	phoneNumberParam = splitPath[1]
	phoneNumber = phoneNumberParam.split("=")[1]
	return phoneNumber

# Extract the stock symbol and the phone number to send the SMS to
# and then use your Twilio API credentials and phone number to 
# create a message and send it.
def setAlert(pathWithParams):
	targetSymbol = getSymbol(pathWithParams)
	toNumber = getPhoneNumber(pathWithParams)

	# Your Account SID from twilio.com/console
	account_sid = "*********************"
	# Your Auth Token from twilio.com/console
	auth_token  = "*********************"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+1"+toNumber, 
	    from_="+12015966491",
	    body="You have set up a price alert for " + targetSymbol +"!")

	print(message.sid)
