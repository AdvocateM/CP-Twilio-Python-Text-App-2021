from twilio.rest import Client

# go to Readme.md to get direct links to get the details of the

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'

#
client = Client(account_sid, auth_token)

#

def Message():
  global client
  # Message
  Massage = input('Type your message here pleas: ')
  
  
  message = client.messages \
                .create(
                     body= Massage,
                     from_='+18016637963',
                     to='+277287829388'
                 )

  print(message.sid)


Message()
