import simplejson as json
import os

dirname = os.path.dirname(__file__)


def combiner(current_path, file):
    # TODO: Fix unicode.
    with open(os.path.join(current_path, file), 'r', encoding='utf-8') as input_file:
        text = json.load(input_file)
        # TODO: Fix facebook user conflict.
        username = current_path[2:-11]
        with open(os.path.join(current_path, 'SIMPLIFIED_' + username + '.json'), 'a', encoding='utf-8') as output_file:
            output_file.write(json.dumps(text, indent=2, sort_keys=True, ensure_ascii=False))


def traveler():
    os.chdir('messages/inbox')
    for current_path, folders, files in os.walk('.'):
        for file in files:
            name, ext = os.path.splitext(file)
            # TODO: Add regex check for file name.
            if name.startswith('message') and ext == '.json':
                combiner(current_path, file)


traveler()
