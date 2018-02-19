from twilio.rest import Client

def getSymbol(path):
	symbol = path[len("/setAlert?alertSymbol="):-len("&toNumber=2223334444")]
	return symbol

def getPhoneNumber(path):
	splitPath = path.split("&")
	phoneNumberParam = splitPath[1]
	phoneNumber = phoneNumberParam.split("=")[1]
	return phoneNumber

def setAlert(pathWithParams):
	targetSymbol = getSymbol(pathWithParams)
	toNumber = getPhoneNumber(pathWithParams)

	# Your Account SID from twilio.com/console
	account_sid = ""
	# Your Auth Token from twilio.com/console
	auth_token  = ""

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+1"+toNumber, #TODO make this dynamic
	    from_="+12015966491",
	    body="You have set up a price alert for " + targetSymbol +"!")

	print(message.sid)
