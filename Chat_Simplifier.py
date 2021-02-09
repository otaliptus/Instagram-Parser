import simplejson as json
import os


def date_time_modifier(date_time_str):
    date = date_time_str[0:10]
    time = date_time_str[11:19]
    return date, time


user_nick = input('Enter the user nick: ')
dirname = os.path.dirname(__file__)
file_name = dirname + '/chats/' + user_nick + '.txt'
simplified_file_name = dirname + '/chats/SIMPLIFIED_' + user_nick + '.txt'

with open(file_name, 'r', encoding='utf-8') as chat_file:
    json_content = json.load(chat_file)
    with open(simplified_file_name, 'w', encoding='utf-8') as simplified_chat_file:
        for message in json_content:
            date_time = date_time_modifier(message['created_at'])
            sender = message['sender']
            try:
                text = message['text']
            except KeyError:
                # TODO: This part will be edited for other message types.
                text = 'MEDIA || STORY SHARE || LIKE || HEART - FIX REQUIRED'
            simple_message = date_time[0] + ' ' + date_time[1] + ' ' + sender + ': ' + text
            simplified_chat_file.write(simple_message + '\n')
