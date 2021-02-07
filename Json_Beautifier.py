import simplejson as json

with open('messages.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

output_file = open('messages_formatted.json', 'w', encoding='utf-8')
output_file.write(json.dumps(file, indent=2, sort_keys=True, ensure_ascii=False))
output_file.close()
