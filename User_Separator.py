import simplejson as json

with open('messages.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

user_nick = input('Enter your nick:')
for chat in file:
    for key, value in chat.items():
        participants = chat['participants']
        conversation = chat['conversation']
        if len(participants) != 1:
            participants.remove(user_nick)
        file_name = participants[0] + '.txt'
        with open(file_name, 'w', encoding='utf-8') as chat_file:
            # print(type(conversation))
            chat_file.write(str(conversation))
