import simplejson as json
from datetime import datetime
import re
from functools import partial

fix_mojibake_escapes = partial(
     re.compile(rb'\\u00([\da-f]{2})').sub,
     lambda m: bytes.fromhex(m.group(1).decode()))

# with open(os.path.join(subdir, file), 'rb') as binary_data:
#     repaired = fix_mojibake_escapes(binary_data.read())
# data = json.loads(repaired.decode('utf8'))

count = 0
stack = []

with open('New_2.txt', 'rb') as input_file:
    repaired = fix_mojibake_escapes(input_file.read())
    text = json.loads(repaired.decode('utf-8'))
    for key in text['messages']:
        my_date = float((key['timestamp_ms']))
        my_date = my_date / 1000
        message = datetime.utcfromtimestamp(my_date).strftime('%I:%M:%S %p, %d/%m/%y -')
        if 'content' in key:
            message = message + ' ' + key['sender_name'] + ': ' + key['content']
            count += 1
            stack.append(message)

with open('Fixed.txt', 'w', encoding='utf-8') as output_file:
    for message in reversed(stack):
        output_file.write(message + '\n')
