import simplejson as json
import os


def date_time_modifier(date_time_str):
    date = date_time_str[0:10]
    time = date_time_str[11:19]
    return date, time


def type_modifier(my_dict):
    my_str = ''
    if 'heart' in my_dict:
        my_str = '❤'

    if 'text' in my_dict:
        my_str = my_dict['text']
        if my_str is None:
            my_str = ''
        if 'story_share' in my_dict:
            my_str = my_str + ' --- ' + my_dict['story_share']

    if 'media_owner' in my_dict:
        my_str = 'Shared post from ' + my_dict['media_owner'] + ' --> ' + my_dict['media_share_url']

    if 'likes' in my_dict:
        my_str = my_str + ' *** Liked by ' + my_dict['likes'][0]['username'] + ' ***'

    return my_str


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
            text = type_modifier(message)
            simple_message = date_time[0] + ' ' + date_time[1] + ' ' + sender + ': ' + text
            simplified_chat_file.write(simple_message + '\n')
