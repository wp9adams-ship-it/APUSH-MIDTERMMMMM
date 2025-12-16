# Replace the default title in each document to match the document's filename

from os import chdir, listdir

chdir('APUSH study')

for file in listdir():
    split = file.split('.')
    if split[len(split) - 1] == 'html':
        with open(file, 'r') as content:
            text = content.read()
            if '<title>Document</title>' in text:
                modified = text.replace('<title>Document</title>', f'<title>{split[0]}</title>')
                print(f'Updated title in "{file}" to "{split[0]}"')
            else:
                modified = text
        with open(file, 'w') as f:
            f.write(modified)
