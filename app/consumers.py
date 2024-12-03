import json
from channels.generic.websocket import AsyncWebsocketConsumer # as same GenricView 

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        self.room_name = "chat_room"
        self.room_group_name = f"chat_{self.room_name}"

        # add channel user to group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        
        await self.accept()

    async def disconnect(self, close_code):

        # remove channel user from group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
      
        text_data_json = json.loads(text_data) # change format from json to python dict
        message = text_data_json['message']

        # send message to all users in group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message', # determine which function runs when message received
                'message': message,
            }
        )

    # when message received django-channels will run this function based on 'type' in receive function
    async def chat_message(self, event):
        
        message = event['message']
        # sent message to client as json
        await self.send(text_data=json.dumps({
            'message': message
        }))
