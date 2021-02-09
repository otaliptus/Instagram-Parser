import simplejson as json
import os

with open('messages.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

user_nick = input('Enter your nick: ')
dirname = os.path.dirname(__file__)

# There might be more effective ways but I'm sleepy right now :)

for chat in file:
    for key, value in chat.items():
        participants = chat['participants']
        conversation = chat['conversation']
        if len(participants) != 1:
            participants.remove(user_nick)
        file_name = dirname + '/chats/' + participants[0] + '.txt'
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as chat_file:
            chat_file.write(json.dumps(conversation, indent=2, sort_keys=True, ensure_ascii=False))
