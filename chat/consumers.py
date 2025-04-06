from channels.generic.websocket import WebsocketConsumer


class ConversationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
