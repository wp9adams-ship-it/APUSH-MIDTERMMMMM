# Add the article-theme-js script to all documents, if not already present

from os import chdir, listdir

chdir('APUSH study')

for file in listdir():
    split = file.split('.')
    if split[len(split) - 1] == 'html':
        with open(file, 'r') as content:
            text = content.read()
            if 'article-theme-js' not in text:
                modified = text.replace('</title>', f'</title>\n    <script src="article-theme-js/theme.js" defer></script>')
                print(f'Added script to "{file}"')
            else:
                modified = text
        with open(file, 'w') as f:
            f.write(modified)
