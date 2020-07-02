from twilio.rest import Client
from credentials import account_id, auth_token, my_cell, my_twilio

client=Client(account_id, auth_token)

# my_msg=' '.join(['Niraj\n' for i in range(10)])
my_msg='Hahhhahahaahahahahaha'

message=client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)


# from twilio.rest import Client
# from credentials import account_id, auth_token, my_cell, my_twilio

# account = "Account number for Twilio"
# token = "Token for Twilio Account"

# client = Client(account, token)

# message = client.messages.create(to="+ReceiverPhone#", from_="+TwilioPhone#",
#                              body="Text message you are sending to receiver")
# #print response back from Twilio
# print message