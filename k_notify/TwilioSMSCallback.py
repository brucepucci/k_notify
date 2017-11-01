from twilio.rest import Client

from BaseNotificationCallback import BaseNotificationCallback

class TwilioSMSCallback(BaseNotificationCallback):
    def __init__(self, sid, token, from_number, to_number):
        self.client = Client(sid, token)
        self.from_number = from_number
        self.to_number = to_number
        super().__init__()

    def send(self, message):
        self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=message)
