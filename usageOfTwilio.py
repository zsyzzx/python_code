#! python3

from twilio.rest import Client

# Twilio 配置
accountSid = 'xxx'
authToken = 'xxx'
myTwilioNumber = 'xxx'
myCellPhone = '+Xxx'


def textMyself(message):
    twilioCli = Client(accountSid, authToken)
    messageobj = twilioCli.messages.create(to=myCellPhone, from_=myTwilioNumber,
                                           body=message)
    return messageobj


textMyself("hello seven")
