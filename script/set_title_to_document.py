# Replace the default title in each document to match the document's filename

from os import chdir, listdir

chdir('../APUSH study')

for file in listdir():
    split = file.split()
    if split[len(split) - 1] == 'html':
        with open(file, 'rw') as content:
            if '<title>Document</title>' in content.read():
                modified = content.read().replace('<title>Document</title>', f'<title>{split[0]}</title>')
                file.write(modified)
